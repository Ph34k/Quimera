import ipaddress
import socket
from urllib.parse import urlparse

def is_safe_url(url: str) -> bool:
    """
    Validates if a given URL is safe to make requests to.
    Prevents SSRF by checking against private, loopback, and other restricted IP ranges.
    """
    try:
        parsed = urlparse(url)
        # Only allow http and https
        if parsed.scheme not in ("http", "https"):
            return False
        hostname = parsed.hostname
        if not hostname:
            return False

        # Resolve hostname to IP using getaddrinfo (supports IPv4 and IPv6)
        addr_info = socket.getaddrinfo(hostname, None)

        # Check all resolved IPs
        for addr in addr_info:
            ip = addr[4][0]
            parsed_ip = ipaddress.ip_address(ip)
            if parsed_ip.is_private or parsed_ip.is_loopback or parsed_ip.is_link_local or parsed_ip.is_multicast or parsed_ip.is_reserved:
                return False
        return True
    except Exception:
        return False
