import socket
from urllib.parse import urlparse
import ipaddress

def is_safe_url(url: str) -> bool:
    """Valida se uma URL é segura contra Server-Side Request Forgery (SSRF)."""
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
    except Exception:
        return False