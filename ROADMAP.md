
# Firewall & HTTP Evasion Toolkit (Nmap Tabanlı)

## 📌 Projenin Amacı

Bu proje, modern web uygulamalarında kullanılan güvenlik duvarı (firewall) ve WAF (Web Application Firewall) çözümlerini tespit etmek ve bu sistemler üzerinde farklı evasion (atlatma) tekniklerinin etkisini gözlemlemek amacıyla geliştirilmiştir. Python ve Nmap tabanlı bu araç, çeşitli testleri otomatik olarak gerçekleştirir ve çıktıları okunabilir HTML/JSON raporları şeklinde sunar.

> **UYARI**: Bu araç yalnızca eğitim ve araştırma amaçlı geliştirilmiştir. İzinsiz sistemler üzerinde kullanımı yasa dışı ve etik dışıdır.

---

## 🧠 Teknik Arka Plan

Güvenlik duvarları, gelen-giden trafiği filtreleyerek saldırıların önüne geçer. Ancak bu sistemler de atlatılabilir. Nmap gibi güçlü tarama araçlarıyla, çeşitli evasion teknikleri kullanarak bu güvenlik önlemlerinin zayıf noktaları test edilebilir.

### Kullanılan Ana Teknikler:
- **TCP Fragmentation**: Paketleri bölerek firewall'ları kandırma.
- **Decoy IP'ler**: Sahte kaynak IP'lerle tarama.
- **MAC Spoofing**: Sahte MAC adresi ile trafik oluşturma.
- **Kaynak Port Manipülasyonu**: Güvenilir portlar (DNS gibi) üzerinden geçme.
- **Bad Checksum**: Bozuk paketlerle güvenlik sistemini test etme.
- **Zamanlama Manipülasyonu**: Trafiği "yavaşlatma" ile analizden kaçma.

---

## 🧰 Kullanılan Modüller

### 🔎 `firewall_fingerprint.py`
- DNS CNAME kayıtları ve WHOIS sorguları ile firewall marka ve sağlayıcılarını tespit eder.
- Desteklenen sistemler: Cloudflare, Fortinet, AWS WAF, Azure, F5 BIG-IP, vb.

### 🛡️ `evasion_analyzer.py`
- 8 farklı evasion tekniği dener.
- Her teknik için:
  - Açık port durumu
  - Süresi
  - Etkinlik sonucu (Engellendi / Bypass Başarılı / Etkisiz)

### 🌐 `http_analysis.py`
- `nmap` script’leri ile HTTP katmanı analiz edilir:
  - Kullanılabilir HTTP metodları (GET, POST, PUT, DELETE…)
  - HTTP başlıkları
  - WAF tespiti (`http-waf-detect`)
  - User-agent davranış testleri

### 📄 `report_engine.py`
- Tüm analiz sonuçları:
  - JSON formatında makine okunabilir halde
  - HTML formatında okunabilir görsel rapor olarak dışa aktarılır

---

## 🧪 Kurulum ve Kullanım

### Gereksinimler
- Python 3.8+
- Nmap (sistem PATH'ine eklenmiş olmalı)

### Kurulum
```bash
git clone https://github.com/hizir777/nmap_evasion.git
cd nmap_evasion
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Kullanım
```bash
python main.py hedefsite.com
```

Raporlar `output/` klasörüne otomatik kaydedilir.

---

## 💡 Örnek Çıktı

**HTML Rapor Özeti:**

- Hedef: example.com  
- Tespit edilen Firewall: Cloudflare  
- Baseline açık portlar: 80, 443  
- Teknik: MAC Spoofing → **Bypass Başarılı** (Port 80 görünür oldu)  
- Teknik: Bad Checksum → **Engellendi**

---

## 🧪 Sanal Test Ortamı Kurulumu (pfSense ile)

1. **VirtualBox veya VMware** ile 3 makine kurun:
   - Saldırgan (Kali veya Ubuntu)
   - Kurban (Windows veya herhangi bir OS)
   - Güvenlik Duvarı: pfSense

2. Ağ Bağlantısı:
   - Host-only ve internal ağ karışımı önerilir
   - pfSense üzerinden NAT veya paket filtreleme ayarları yapılandırılabilir

3. **Test Adımları:**
   - pfSense üzerinden port filtreleri oluşturun
   - `main.py` aracını saldırgan makinadan çalıştırarak hedefi analiz edin
   - Raporları HTML/JSON olarak gözlemleyin

---

## 🛡️ Etik ve Yasal Uyarı

Bu proje yalnızca araştırma ve eğitim amaçlıdır. Gerçek dünyada uygulamadan önce:
- Açık izin alın,
- Test ortamı oluşturun,
- Trafiği izole edin.

---

## 📌 Sonuç

Bu araç sayesinde, farklı evasion tekniklerinin firewall/WAF sistemleri üzerinde ne ölçüde etkili olduğunu görebilir; ağ güvenliğinizi test etmek için profesyonel bir temel elde edebilirsiniz.
