import os
import json
from datetime import datetime

def save_json_report(domain, firewall, evasion_data, http_data):
    os.makedirs("output", exist_ok=True)
    data = {
        "target": domain,
        "firewall_detected": firewall,
        "baseline_ports": evasion_data.get("baseline_ports", []),
        "evasion_results": evasion_data.get("results", []),
        "http_analysis": http_data
    }
    filename = f"output/{domain.replace('.', '_')}_{datetime.now().strftime('%Y%m%d_%H%M')}.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    return filename

def save_html_report(domain, firewall, evasion_data, http_data):
    os.makedirs("output", exist_ok=True)
    filename = f"output/{domain.replace('.', '_')}_{datetime.now().strftime('%Y%m%d_%H%M')}.html"
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    def color_status(status):
        return {
            "Bypass Başarılı": "green",
            "Etkisiz": "orange",
            "Engellendi": "red",
            "Şüpheli Etki": "gray"
        }.get(status, "black")

    with open(filename, "w") as f:
        f.write(f"""<!DOCTYPE html>
<html lang='tr'>
<head>
<meta charset='UTF-8'>
<title>Firewall & Evasion Raporu</title>
<style>
body {{ font-family: Arial; background: #f0f0f0; padding: 20px; }}
.box {{ background: #fff; padding: 15px; border-radius: 10px; margin-bottom: 20px; }}
pre {{ background: #eee; padding: 10px; border-radius: 5px; }}
</style>
</head>
<body>
<h1>Firewall & Evasion Raporu</h1>
<div class='box'><strong>Hedef:</strong> {domain}<br><strong>Tarih:</strong> {now}<br><strong>Firewall:</strong> {firewall}</div>
<div class='box'><h2>Baseline Açık Portlar</h2><pre>{", ".join(evasion_data.get("baseline_ports", []))}</pre></div>
<div class='box'><h2>Evasion Teknikleri</h2><pre>""")

        for r in evasion_data.get("results", []):
            color = color_status(r["status"])
            f.write(f"<span style='color:{color};'>{r['technique']}: {r['status']}</span> | Portlar: {', '.join(r['observed_ports'])} | Süre: {r['duration_sec']}s\n")

        f.write("</pre></div>")

        # HTTP Analysis Section (raw only)
        f.write("<div class='box'><h2>HTTP Analizi (Ham Çıktı)</h2><pre>{}</pre></div>".format(http_data.get("raw_output", "Yok")))

        f.write("</body></html>")

    return filename
