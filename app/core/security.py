import httpx
import socket
from urllib.parse import urlparse
from ipaddress import ip_address

def is_safe_url(url: str) -> bool:
    """
    Validates if a URL resolves to a safe, public IP address to prevent SSRF.
    Checks against private, loopback, link-local, and unspecified IPs.
    """
    try:
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname
        if not hostname:
            return False

        # Resolve the hostname to an IP address
        ip = socket.gethostbyname(hostname)
        ip_obj = ip_address(ip)

        # Check if the IP is private, loopback, link-local, or unspecified
        if ip_obj.is_private or ip_obj.is_loopback or ip_obj.is_link_local or ip_obj.is_unspecified:
            return False

        return True
    except Exception:
        return False

def validate_request_hook(request: httpx.Request):
    """
    HTTPX event hook to validate the URL before a request is made or followed.
    """
    if not is_safe_url(str(request.url)):
        raise ValueError(f"SSRF Attempt detected. Blocked request to: {request.url}")
