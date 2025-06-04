<div align="center">
  <img src="https://img.shields.io/github/languages/count/hizir777/nmap_evasion?style=flat-square&color=blueviolet" alt="Language Count">
  <img src="https://img.shields.io/github/languages/top/hizir777/nmap_evasion?style=flat-square&color=1e90ff" alt="Top Language">
  <img src="https://img.shields.io/github/last-commit/hizir777/nmap_evasion?style=flat-square&color=ff69b4" alt="Last Commit">
  <img src="https://img.shields.io/github/license/hizir777/nmap_evasion?style=flat-square&color=yellow" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-green?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=flat-square" alt="Contributions">
</div>

# nmap_evasion

A Python-based penetration testing tool that identifies firewall technologies and evaluates multiple evasion techniques using Nmap.  
**Nmap tabanlı, güvenlik duvarlarını tespit eden ve farklı atlatma tekniklerini analiz eden Python aracı.**

---

## Features / *Özellikler*

- 🔍**Firewall Vendor Detection**: Recognizes common solutions such as Cloudflare, Fortinet, AWS, and Azure.
- 🔍*Güvenlik Duvarı Sağlayıcı Tespiti:  Cloudflare, Fortinet, AWS, Azure gibi yaygın çözümleri tanır.*
////////////////////////////////////////////////////////////////////////////////////////////////////
- 🛡️**HTTP WAF Analysis**: Nmap NSE scripts such as http-methods, http-waf-detect for WAF detection.
- 🛡️*HTTP WAF Analizi: `http-methods`, `http-waf-detect` gibi Nmap NSE script'leri ile WAF tespiti.*
////////////////////////////////////////////////////////////////////////////////////////////////////
- 🎯**8+ Evasion Techniques**: Performs testing with techniques such as TCP fragmentation, decoy, spoofed MAC, and slow timing.
- 🎯*8+ Kaçınma Tekniği: TCP fragmentation, decoy, spoofed MAC, slow timing vb. tekniklerle test yapar.*
////////////////////////////////////////////////////////////////////////////////////////////////////
- 📊**HTML + JSON Reports**: Generates output in visual HTML and machine-readable JSON formats.
- 📊*HTML + JSON Raporları: Görsel HTML ve makine okunabilir JSON formatlarında çıktı üretir.*
////////////////////////////////////////////////////////////////////////////////////////////////////
- 🔧**Fully Automated**: Detection, analysis, and reporting are completed with a single command.
- 🔧*Tamamen Otomatik: Tek komutla tespit, analiz ve raporlama işlemleri tamamlanır.*
  

---

## Team / *Ekip*

- **24....1008** - Can Ekizoğlu: *coding and researching*  
  *Can ekizoğlu: kodlama ve araştırma*
- **another** - Ömer Berk Eriş: *coding and researching*  
  *Ömer Berk Eriş: kodlama ve araştırma*

---

## Roadmap / *Yol Haritası*

See our plans in [ROADMAP.md](ROADMAP.md).  
*Yolculuğu görmek için [ROADMAP.md](ROADMAP.md) dosyasına göz atın.*

---

## Research / *Araştırmalar*

| Topic / *Başlık*        | Link                                    | Description / *Açıklama*                        |
|-------------------------|-----------------------------------------|------------------------------------------------|
| Nmap deep dive          | [researchs/aircrack.md](researchs/aircrack.md) | In-depth analysis of Aircrack-ng suite. / *Aircrack-ng paketinin derinlemesine analizi.* |
| Example Research Topic  | [researchs/your-research-file.md](researchs/your-research-file.md) | Brief overview of this research. / *Bu araştırmanın kısa bir özeti.* |
| Add More Research       | *Link to your other research files*     | *Description of the research*                  |

---

## Installation / *Kurulum*

1. **Clone the Repository / *Depoyu Klonlayın***:  
   ```bash
   git clone https://github.com/hizir777/nmap_evasion.git
   cd nmap_evasion
   ```

2. **Set Up Virtual Environment / *Sanal Ortam Kurulumu*** (Recommended):  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies / *Bağımlılıkları Yükleyin***:  
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage / *Kullanım*

Run the project:  
*Projeyi çalıştırın:*

```bash
python main.py example.com
```

**Steps**:  

1. Specify the target website. Write it without mentioning the protocol :
    *cloudflare.com*  
3. Run directly by typing:
  ```bash
  python main.py example.com
  ```
5. You can find the outputs in HTML and JSON formats inside the *core/source/* folder.

   
*Adımlar*:  
1. Hedef websitesini yazın. Protokol belirtmeden:
    *cloudflare.com*  
3. Bu şekilde direkt olarak çalışır:
  ```bash
  python main.py example.com
  ```  
5. Çıktıları HTML ve JSON formatlarında core/source/ klasörünün içinde bulabilirsiniz.

---

## Contributing / *Katkıda Bulunma*

We welcome contributions! To help:  
1. Fork the repository.  
2. Clone your fork (`git clone git@github.com:hizir777/nmap_evasion.git`).  
3. Create a branch (`git checkout -b feature/your-feature`).  
4. Commit changes with clear messages.  
5. Push to your fork (`git push origin feature/your-feature`).  
6. Open a Pull Request.  

Follow our coding standards (see [CONTRIBUTING.md](CONTRIBUTING.md)).  

*Topluluk katkilerini memnuniyetle karşılıyoruz! Katkıda bulunmak için yukarıdaki adımları izleyin ve kodlama standartlarımıza uyun.*

---

## License / *Lisans*

Licensed under the [MIT License](LICENSE.md).  
*MIT Lisansı altında lisanslanmıştır.*

---

## Acknowledgements / *Teşekkürler* (Optional)

Thanks to:  
- Awesome Library: For enabling X.  
- Inspiration Source.  
- Special thanks to...  

*Teşekkürler: Harika kütüphaneler ve ilham kaynakları için.*

---

## Contact / *İletişim* (Optional)

Project Maintainer: [Your Name/Org Name] - [your.email@example.com]  
Found a bug? Open an issue.  

*Proje Sorumlusu: [Adınız/Kuruluş Adınız] - [e-posta.adresiniz@ornek.com]. Hata bulursanız bir sorun bildirin.*

---

*Replace placeholders (e.g., YOUR_USERNAME/YOUR_REPO) with your project details.*
