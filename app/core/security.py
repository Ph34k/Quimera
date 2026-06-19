import socket
import ipaddress
import httpx

def validate_request_ip(request: httpx.Request):
    """
    SECURITY: Prevent SSRF by validating the resolved IP address of the request URL.
    This hook runs on the initial request and every redirect.
    """
    host = request.url.host
    if not host:
        raise ValueError("Invalid URL: missing host")

    try:
        # Resolve both IPv4 and IPv6 to prevent bypasses
        addr_info = socket.getaddrinfo(host, None)
    except socket.gaierror:
        # SECURITY: Fail closed if DNS resolution fails
        raise httpx.RequestError(f"DNS resolution failed for {host}", request=request)

    for addr in addr_info:
        ip_str = addr[4][0]
        try:
            ip_obj = ipaddress.ip_address(ip_str)
            # SECURITY: Block private, loopback, link-local, and unspecified (0.0.0.0) IPs
            if (ip_obj.is_private or ip_obj.is_loopback or
                ip_obj.is_link_local or ip_obj.is_unspecified):
                raise httpx.RequestError(f"Access to internal IP {ip_str} is forbidden", request=request)
        except ValueError:
            raise httpx.RequestError(f"Invalid IP address {ip_str}", request=request)

def get_safe_httpx_client(*args, **kwargs) -> httpx.Client:
    event_hooks = kwargs.get("event_hooks", {})
    request_hooks = event_hooks.get("request", [])
    if validate_request_ip not in request_hooks:
        request_hooks.append(validate_request_ip)
    event_hooks["request"] = request_hooks
    kwargs["event_hooks"] = event_hooks
    return httpx.Client(*args, **kwargs)
