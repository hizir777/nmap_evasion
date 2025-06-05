"""Command line interface for running firewall detection and evasion tests.

This module ties together the different parts of the project.  It resolves the
target domain provided by the user, detects the firewall technology in use,
executes evasion techniques and HTTP analysis, and finally saves the results to
HTML and JSON reports.
"""

import argparse
import logging
from core.firewall_fingerprint import detect_firewall
from core.evasion_analyzer import run_all_evasion_tests
from core.http_analysis import run_http_scripts
from core.report_engine import save_html_report, save_json_report

def main() -> None:
    """Execute the full analysis workflow.

    The function parses the command line argument for the target domain and
    sequentially performs firewall detection, evasion technique tests and HTTP
    analysis.  After the analysis, HTML and JSON reports are created.

    Returns
    -------
    None
        The results are written to disk; no value is returned.
    """

    parser = argparse.ArgumentParser(
        description="Firewall & HTTP Evasion Test Aracı"
    )
    parser.add_argument("target", help="Hedef domain (örnek: example.com)")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")

    domain = args.target
    logging.info(f"Hedef: {domain}")

    logging.info("Firewall tespiti yapılıyor...")
    firewall = detect_firewall(domain)
    logging.info(f"Tespit edilen Firewall: {firewall}")

    logging.info("Evasion teknikleri uygulanıyor...")
    evasion_data = run_all_evasion_tests(domain)

    logging.info("HTTP analiz modülleri çalıştırılıyor...")
    http_data = run_http_scripts(domain)

    logging.info("Raporlar oluşturuluyor...")
    html_path = save_html_report(domain, firewall, evasion_data, http_data)
    json_path = save_json_report(domain, firewall, evasion_data, http_data)

    logging.info(f"HTML Rapor: {html_path}")
    logging.info(f"JSON Rapor: {json_path}")
    logging.info("Tüm işlemler tamamlandı.")