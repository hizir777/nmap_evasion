"""Utilities for detecting firewall vendors protecting a target domain."""

import socket
import subprocess
import logging

FIREWALL_SIGNATURES = {
    "cloudflare": "Cloudflare",
    "fortinet": "Fortinet",
    "akamai": "Akamai",
    "palo alto": "Palo Alto",
    "incapsula": "Imperva Incapsula",
    "barracuda": "Barracuda",
    "sucuri": "Sucuri",
    "f5": "F5 BIG-IP",
    "netscaler": "Citrix NetScaler",
    "amazon": "AWS WAF",
    "microsoft": "Azure WAF",
    "google": "Google Cloud Armor"
}

def run_command(cmd):
    """Run a shell command and capture its output.

    Parameters
    ----------
    cmd : list[str]
        Command and arguments to execute.

    Returns
    -------
    str
        Decoded standard output from the command or the error output if the
        command fails.
    """

    try:
        return subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=15).decode()
    except subprocess.CalledProcessError as e:
        logging.warning(f"Komut hatası: {' '.join(cmd)}")
        return e.output.decode()
    except Exception as e:
        return str(e)

def resolve_ip(target):
    """Resolve a domain name to its IP address.

    Parameters
    ----------
    target : str
        Domain name to resolve.

    Returns
    -------
    str | None
        The IP address or ``None`` if resolution fails.
    """

    try:
        return socket.gethostbyname(target)
    except Exception:
        return None

def dns_cname_check(domain):
    """Look for known firewall providers in the CNAME record of a domain.

    Parameters
    ----------
    domain : str
        Target domain to query.

    Returns
    -------
    str | None
        Detected firewall name or ``None`` if no match is found.
    """

    output = run_command(["dig", domain, "CNAME", "+short"])
    for keyword, name in FIREWALL_SIGNATURES.items():
        if keyword in output.lower():
            return name
    return None

def whois_check(ip):
    """Perform a WHOIS lookup for firewall vendor clues.

    Parameters
    ----------
    ip : str | None
        IP address of the target host.

    Returns
    -------
    str | None
        Firewall name extracted from the WHOIS information, or ``None`` if not
        identifiable.
    """

    if not ip:
        return None
    output = run_command(["whois", ip])
    for keyword, name in FIREWALL_SIGNATURES.items():
        if keyword in output.lower():
            return name
    return None

def detect_firewall(domain):
    """Identify a firewall protecting the specified domain.

    Parameters
    ----------
    domain : str
        Domain to inspect.

    Returns
    -------
    str
        Name of the detected firewall vendor or ``"Bilinmiyor"`` (unknown) if no
        match is found.
    """

    ip = resolve_ip(domain)
    return dns_cname_check(domain) or whois_check(ip) or "Bilinmiyor"