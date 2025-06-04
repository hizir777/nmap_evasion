##PROMPT##

**Proje ve Hedefler ve Ozellikler:** Bu proje, hedef sistemin sahip olduğu güvenlik duvarı (firewall) altyapısını analiz etmek ve zafiyetlerini değerlendirmek amacıyla geliştirilmiş bir siber güvenlik aracıdır. Nmap'in sunduğu güçlü tarama ve script desteğinden faydalanarak, sistemde kullanılan firewall markasını (örneğin Cloudflare, Fortinet, AWS WAF gibi) DNS kayıtları ve WHOIS bilgileri üzerinden tespit eder. Ardından, çeşitli ağ seviyesi evasion (atlatma) tekniklerini uygulayarak firewall’un bu saldırılara verdiği tepkiyi ölçer. Kullanılan teknikler arasında TCP fragmentation, MAC spoofing, decoy IP’ler, bad checksum gibi gelişmiş bypass yöntemleri yer alır. Ayrıca HTTP düzeyinde WAF tespiti de gerçekleştirilir. Tüm bu analizler sonucunda elde edilen veriler, okunabilir HTML ve JSON formatlarında detaylı bir şekilde raporlanır. Araç, laboratuvar testlerinde veya izne dayalı pentest çalışmalarında firewall yapılandırmalarının sağlamlığını değerlendirmek için etkili bir çözüm sunar. 


**Görev:** 2025 yılı için [Firewall_evasion, örneğin: 'nmap kullanarak firewall tespiti ve bunlardan kaçınma yolları'] alanındaki en son ve en etkili ilk 10 tekniği/trendi derinlemesine araştır ve belirle. 

**Ozellikler** 

**İstenen Çıktı Detayları:** 
1. Belirlenen her bir teknik/trend için kısa ve öz bir başlık.
2. Her bir tekniğin/trendin ne olduğu, nasıl çalıştığı ve neden önemli olduğuna dair 2-3 cümlelik bir açıklama.
3. Her bir tekniğin/trendin 2025'teki potansiyel etkileri ve uygulama alanları.
4. Mümkünse, her bir teknik/trend için güvenilir bir kaynak veya referans (örneğin, yayın adı, konferans, uzman görüşü).
5. Sonuçları numaralandırılmış bir liste halinde sun. 

**Kısıtlamalar:** 
- Sadece 2025 yılı ve sonrası için öngörülen veya geçerli olacak tekniklere odaklan. 
- Bilgilerin güncel ve doğrulanabilir olmasına özen göster. 
- Spekülatif olmayan, kanıta dayalı bilgiler sun.

**Örnek Alanlar:** 
   -Ağ Güvenliği ve Sızma Testi Yaklaşımları

   -Firewall ve WAF Teknolojilerinin Karşılaştırmalı Analizi

   -Siber Güvenlikte Evasion Teknikleri ve Karşı Önlemler

   -Kritik Altyapılar için Güvenlik Duvarı Dayanıklılık Testleri

   -Eğitim Amaçlı Siber Güvenlik Simülasyon Ortamları (CTF, lab, pfSense vb.)
