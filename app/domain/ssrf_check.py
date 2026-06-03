import urllib.parse
import socket
import ipaddress

def is_safe_url(url: str) -> bool:
    try:
        parsed_url = urllib.parse.urlparse(url)
        hostname = parsed_url.hostname

        if not hostname:
            return False

        # Resolve hostname to IP(s)
        try:
            addr_info = socket.getaddrinfo(hostname, None)
        except socket.gaierror:
            return False

        for addr in addr_info:
            ip_str = addr[4][0]
            ip_obj = ipaddress.ip_address(ip_str)

            # Prevent loopback, private, and reserved IPs (like 169.254.169.254)
            if not ip_obj.is_global:
                return False

        return True
    except Exception:
        return False
