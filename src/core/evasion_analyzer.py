"""Run Nmap evasion techniques and summarise their effectiveness."""

import subprocess
import re
import time
import logging

EVASION_TECHNIQUES = [
    {"name": "Fragmentation", "args": ["-f"]},
    {"name": "Decoy", "args": ["-D", "RND:10"]},
    {"name": "MAC Spoofing", "args": ["--spoof-mac", "0"]},
    {"name": "Source Port 53", "args": ["--source-port", "53"]},
    {"name": "Data Length Padding", "args": ["--data-length", "100"]},
    {"name": "Bad Checksum", "args": ["--badsum"]},
    {"name": "Slow Timing (T2)", "args": ["-T2"]},
    {"name": "Combined Evasion", "args": ["-f", "-D", "RND:5", "--spoof-mac", "0", "--source-port", "53", "--data-length", "50", "-T2"]}
]

def run_nmap(target: str, extra_args: list[str] | None = None) -> str:
    """Execute an Nmap scan with optional evasion parameters.

    Parameters
    ----------
    target : str
        Domain or IP address to scan.
    extra_args : list[str] | None, optional
        Additional arguments for Nmap representing evasion options.

    Returns
    -------
    str
        Raw output produced by Nmap.
    """

    cmd = ["nmap", "-Pn", "-sS", "-p", "80,443", target]
    if extra_args:
        cmd = cmd[:1] + extra_args + cmd[1:]
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=60).decode()
        return output
    except subprocess.CalledProcessError as e:
        return e.output.decode()
    except Exception as e:
        return str(e)
    
def parse_open_ports(nmap_output: str) -> list[str]:
    """Extract a list of open TCP port numbers from Nmap output."""

    return re.findall(r"(\d+)/tcp\s+open", nmap_output)

def run_all_evasion_tests(target: str) -> dict:
    """Run every predefined Nmap evasion technique against a target.

    Parameters
    ----------
    target : str
        Host or domain name to scan.

    Returns
    -------
    dict
        Dictionary containing the baseline open ports and the result list for
        each evasion attempt.
    """

    baseline_output = run_nmap(target)
    baseline_ports = parse_open_ports(baseline_output)
    results = []

    for technique in EVASION_TECHNIQUES:
        start_time = time.time()
        output = run_nmap(target, technique["args"])
        ports = parse_open_ports(output)
        elapsed = round(time.time() - start_time, 2)

        if not ports:
            status = "Engellendi"
        elif set(ports) - set(baseline_ports):
            status = "Bypass Başarılı"
        elif ports == baseline_ports:
            status = "Etkisiz"
        else:
            status = "Şüpheli Etki"

        results.append({
            "technique": technique["name"],
            "status": status,
            "observed_ports": ports,
            "duration_sec": elapsed
        })