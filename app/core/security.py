import socket
import ipaddress
from urllib.parse import urlparse

def is_safe_url(url: str) -> bool:
    """
    Validates if a URL is safe to be requested (prevents SSRF).
    Checks that the URL scheme is http/https and resolves to a public IP address.
    """
    try:
        parsed = urlparse(url)
        if parsed.scheme not in ("http", "https"):
            return False

        hostname = parsed.hostname
        if not hostname:
            return False

        # Resolve hostname to IPs to check for internal/private addresses
        addrinfo = socket.getaddrinfo(hostname, None)

        for info in addrinfo:
            ip_str = info[4][0]
            ip = ipaddress.ip_address(ip_str)
            if (ip.is_private or ip.is_loopback or ip.is_link_local or
                ip.is_multicast or ip.is_unspecified or ip.is_reserved):
                return False

        return True
    except Exception:
        # Fail securely on any parsing or resolution error
        return False
