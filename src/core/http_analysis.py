import subprocess
import re
import logging

def run_http_scripts(domain):
    scripts = [
        "http-methods",
        "http-headers",
        "http-waf-detect",
        "http-useragent-tester"
    ]
    cmd = ["nmap", "-p", "80,443", "--script=" + ",".join(scripts), domain]

    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=60).decode()
    except subprocess.CalledProcessError as e:
        output = e.output.decode()
    except Exception as e:
        output = str(e)

    parsed = {
        "http_methods": [],
        "headers": {},
        "waf_detected": None,
        "useragent_results": {},
        "raw_output": output
    }

    # Basic parsing heuristics
    methods_match = re.findall(r"Supported Methods: ([A-Z, ]+)", output)
    if methods_match:
        parsed["http_methods"] = [m.strip() for m in methods_match[0].split(",")]

    headers_match = re.findall(r"(?i)(?:http-headers):\s+((?:.+?\n)+?)\n\n", output)
    if headers_match:
        for line in headers_match[0].splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                parsed["headers"][k.strip()] = v.strip()

    if "is behind a WAF" in output:
        parsed["waf_detected"] = True
    elif "No WAF detected" in output:
        parsed["waf_detected"] = False

    return parsed
