import socket
from urllib.parse import urlparse
import ipaddress

def is_safe_url(url: str) -> bool:
    try:
        parsed = urlparse(url)
        if parsed.scheme not in ("http", "https"):
            return False

        hostname = parsed.hostname
        if not hostname:
            return False

        addr_info = socket.getaddrinfo(hostname, None)
        for ai in addr_info:
            ip_str = ai[4][0]
            ip_obj = ipaddress.ip_address(ip_str)
            if ip_obj.is_private or ip_obj.is_loopback or ip_obj.is_link_local or ip_obj.is_multicast or ip_obj.is_unspecified:
                return False
        return True
    except Exception as e:
        print(f"Error checking URL {url}: {e}")
        return False

print("http://google.com ->", is_safe_url("http://google.com"))
print("http://localhost ->", is_safe_url("http://localhost"))
print("http://127.0.0.1 ->", is_safe_url("http://127.0.0.1"))
print("http://169.254.169.254 ->", is_safe_url("http://169.254.169.254"))
print("file:///etc/passwd ->", is_safe_url("file:///etc/passwd"))
