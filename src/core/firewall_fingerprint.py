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
    try:
        return subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=15).decode()
    except subprocess.CalledProcessError as e:
        logging.warning(f"Komut hatası: {' '.join(cmd)}")
        return e.output.decode()
    except Exception as e:
        return str(e)

def resolve_ip(target):
    try:
        return socket.gethostbyname(target)
    except:
        return None

def dns_cname_check(domain):
    output = run_command(["dig", domain, "CNAME", "+short"])
    for keyword, name in FIREWALL_SIGNATURES.items():
        if keyword in output.lower():
            return name
    return None

def whois_check(ip):
    if not ip:
        return None
    output = run_command(["whois", ip])
    for keyword, name in FIREWALL_SIGNATURES.items():
        if keyword in output.lower():
            return name
    return None

def detect_firewall(domain):
    ip = resolve_ip(domain)
    return dns_cname_check(domain) or whois_check(ip) or "Bilinmiyor"
