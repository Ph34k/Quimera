import socket
import ipaddress
from urllib.parse import urlparse
import httpx

def is_safe_url(url_str: str) -> bool:
    try:
        parsed = urlparse(url_str)
        hostname = parsed.hostname
        if not hostname:
            return False

        # resolve hostname
        addrinfo = socket.getaddrinfo(hostname, None)
        for info in addrinfo:
            ip_str = info[4][0]
            ip = ipaddress.ip_address(ip_str)
            if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_unspecified or ip.is_multicast:
                return False
        return True
    except Exception as e:
        print(f"Exception: {e}")
        return False

def verify_request(request: httpx.Request):
    if not is_safe_url(str(request.url)):
        raise httpx.RequestError("Blocked by SSRF protection", request=request)

client = httpx.Client(event_hooks={"request": [verify_request]})

try:
    print("Testing http://localhost")
    client.get("http://localhost")
except Exception as e:
    print(f"Error: {e}")

try:
    print("Testing http://google.com")
    client.get("http://google.com")
except Exception as e:
    print(f"Error: {e}")
