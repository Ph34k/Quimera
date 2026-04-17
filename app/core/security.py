import socket
import ipaddress
from urllib.parse import urlparse

def is_safe_url(url: str) -> bool:
    """
    🛡️ Sentinel Security Function: Validates URL to prevent Server-Side Request Forgery (SSRF).
    Blocks non-HTTP schemes, private/loopback/link-local IP addresses, and metadata services.
    """
    try:
        parsed = urlparse(url)
        # Block non-HTTP schemes
        if parsed.scheme not in ("http", "https"):
            return False

        hostname = parsed.hostname
        if not hostname:
            return False

        # Block common metadata service hostnames
        if hostname.lower() in ("localhost", "metadata.google.internal"):
            return False

        # Resolve IP to check for private/internal networks
        ip = socket.gethostbyname(hostname)
        ip_obj = ipaddress.ip_address(ip)

        if ip_obj.is_loopback or ip_obj.is_private or ip_obj.is_link_local:
            return False

        return True
    except Exception:
        # Fail securely: if we can't parse or resolve, block it
        return False
