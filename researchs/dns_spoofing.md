# **Kali Linux ile DNS Spoofing: Kapsamlı Bir Teknik İnceleme ve Etik Hususlar**

## **I. Kali Linux Ortamında DNS Spoofing'e Giriş**

Bu bölüm, DNS spoofing saldırılarının temel mekanizmalarını, siber suçluların hedeflerini ve bu tür faaliyetler için Kali Linux platformunun neden tercih edildiğini incelemektedir. Ayrıca, bu tür araç ve tekniklerin kullanımında etik ve yasal sorumlulukların altı çizilecektir.

### **A. DNS Spoofing'in Tanımı: Mekanizma ve Kötü Amaçlı Hedefler**

Alan Adı Sistemi (DNS), internet kullanıcılarının www.ornek.com gibi alan adlarını, bilgisayarların iletişim kurmak için kullandığı sayısal IP adreslerine çeviren hayati bir internet altyapısı bileşenidir. Standart bir DNS çözümleme sürecinde, kullanıcının cihazı bir alan adı için DNS sorgusu yaptığında, bu sorgu genellikle bir özyinelemeli (recursive) DNS sunucusuna gönderilir. Bu sunucu, eğer cevabı kendi önbelleğinde bulamazsa, yetkili (authoritative) DNS sunucularına başvurarak doğru IP adresini bulur ve kullanıcıya iletir.

DNS spoofing, "bir ağda DNS sorgularını manipüle ederek kullanıcıları sahte bir web sitesine yönlendirmek için kullanılan bir siber saldırı yöntemidir." Bu saldırı türünde, saldırgan, kurbanın DNS sorgularını ele geçirir ve bu sorgulara, meşru alan adını kötü amaçlı bir IP adresine yönlendiren sahte yanıtlar verir. Bu sürecin başarılı olabilmesi için saldırganın, kurbanın DNS isteklerini görebileceği ve meşru DNS sunucusundan önce yanıt verebileceği bir konumda olması gerekir.

DNS spoofing saldırılarının yaygın hedefleri arasında kullanıcıları kimlik avı (phishing) sitelerine yönlendirerek oturum açma bilgilerini veya hassas verileri çalmak, kötü amaçlı yazılım dağıtmak, belirli web sitelerine erişimi engelleyerek sansür uygulamak veya genel ağ trafiğini kesintiye uğratmak bulunur.

### **B. Kali Linux: Güvenlik Değerlendirmeleri ve Penetrasyon Testleri için Öncü Platform**

Kali Linux, dijital adli bilişim ve penetrasyon testleri için özel olarak tasarlanmış, Debian tabanlı bir Linux dağıtımıdır. Ağ saldırılarıyla ilgili, DNS spoofing için kullanılanlar da dahil olmak üzere, önceden yüklenmiş geniş bir araç yelpazesi sunmasıyla bilinir. "Kali Linux, bu tür saldırıları gerçekleştirmek için çeşitli araçlar sunar."

Kali Linux'un siber güvenlik uzmanları tarafından tercih edilmesinin başlıca nedenleri arasında, tümleşik ve kullanıma hazır bir araç seti sunması, paket enjeksiyonu gibi özel görevler için yamalanmış çekirdeklere sahip olması ve güvenlik uzmanları için kullanım kolaylığı sağlaması yer alır. Bu özellikler, Kali Linux'u DNS spoofing gibi saldırı tekniklerini öğrenmek ve kontrollü ortamlarda test etmek için ideal bir platform haline getirir.

### **C. Vazgeçilmez Ön Koşul: Etik Hackerlık İlkeleri ve Yasal Sınırlar**

Bu raporda sunulan tüm bilgilerin **yalnızca eğitim ve araştırma amaçlı** olduğu ve etik olmayan veya yasa dışı faaliyetler için kullanılmaması gerektiği kesin bir dille vurgulanmalıdır. "Bu bilgiler yalnızca eğitim amaçlıdır ve etik olmayan kullanımlar için uygun değildir. Herhangi bir ağda bu tür işlemleri yapmadan önce izin almanız gerektiğini unutmayın". Bu uyarı, raporun tamamında temel bir ilke olarak kabul edilecektir.

Etik hackerlık, sistemlerdeki güvenlik açıklarını belirlemek amacıyla, sistem sahiplerinden alınan yetkiyle gerçekleştirilen sızma girişimleridir. Yetkisiz DNS spoofing girişimleri ise ağa izinsiz erişim, dolandırıcılık, veri hırsızlığı ve hizmet kesintisi gibi ciddi suçlamalara yol açabilir ve ağır yasal yaptırımları beraberinde getirebilir. Bu nedenle, test edilecek ağların veya sistemlerin sahibinden açık ve yazılı izin almak, bu tür işlemleri gerçekleştirmeden önceki mutlak bir zorunluluktur.

Kali Linux gibi güçlü bir penetrasyon testi dağıtımında DNS spoofing araçlarının bulunması ve detaylı bir şekilde belgelenmesi, önemli bir ikilemi ortaya koymaktadır: Bu teknikler kötü niyetli aktörler tarafından aktif olarak kullanılmaktadır, dolayısıyla güvenlik uzmanlarının etkili savunma mekanizmaları geliştirebilmeleri için bu yöntemleri derinlemesine anlamaları şarttır. Bu durum, söz konusu araçların öğrenilmesinin kötü niyetli faaliyetleri teşvik etmek yerine, sağlam siber güvenlik duruşları oluşturmayı amaçladığını ve eğitimsel gerekçeyi haklı çıkardığını gösterir. "İzin almanız gerektiğini unutmayın" şeklindeki tekrarlanan vurgu, bir siber güvenlik testinin meşruiyeti ile suç teşkil eden bir eylem arasındaki temel ayrımın yetkilendirme olduğunu net bir şekilde ortaya koyar. Kullanılan araçlar ve teknikler aynı olsa da, kullanım bağlamı (yetkili veya yetkisiz) eylemin yasallığını ve etiğini belirleyen tek faktördür. Bu durum, siber güvenlik eğitiminin sadece teknik "nasıl yapılır" bilgisine değil, aynı zamanda güçlü araçların kullanımını çevreleyen etik çerçeveye de yoğun bir şekilde odaklanması gerektiğini ima eder.

## **II. Kali Linux'ta Öne Çıkan DNS Spoofing Araçları ve Teknikleri**

Bu bölümde, Kali Linux ortamında DNS spoofing gerçekleştirmek için kullanılan başlıca araçlar ve yöntemler detaylı bir şekilde incelenecektir. Her bir araç, özel yaklaşımı, güçlü yönleri ve adım adım operasyonel süreçleri ile birlikte sunulacaktır. Platformun Kali Linux olduğu ve gereksinimlerin genellikle ağ erişimi, potansiyel bağımlılıklar ve bir yardımcı web sunucusu içerdiği varsayılmaktadır.

### **A. Ettercap: Çok Yönlü Man-in-the-Middle (Ortadaki Adam) Çerçevesi**

#### **1\. Genel Bakış ve Güçlü Yönleri**

Ettercap, "güçlü bir man-in-the-middle (MITM) aracıdır ve DNS spoofing için sıkça kullanılır." Entegre bir MITM saldırı paketi sunması, grafiksel kullanıcı arayüzü (ettercap \-G) seçeneği ve dns\_spoof gibi eklenti tabanlı mimarisi başlıca güçlü yönlerindendir.

#### **2\. Platform ve Gereksinimler**

* **Platform:** Kali Linux (genellikle önceden yüklü gelir). Yüklü değilse, sudo apt update && sudo apt install ettercap-graphical komutuyla kurulabilir.  
* **Gereksinimler:**  
  * Kök yetkileri (sudo).  
  * Trafiği saldırganın makinesi üzerinden yönlendirmek için etter.conf dosyasının iptables entegrasyonu için yapılandırılması. Özellikle aşağıdaki satırların başındaki \# işaretinin kaldırılması gerekmektedir:  
    redir\_command\_on \= "iptables \-t nat \-A PREROUTING \-i %iface \-p tcp \--dport %port \-j REDIRECT \--to-ports %rport"  
    redir\_command\_off \= "iptables \-t nat \-D PREROUTING \-i %iface \-p tcp \--dport %port \-j REDIRECT \--to-ports %rport"  
    Bu yapılandırma, MITM saldırılarında trafiği yakalamak ve yönlendirmek için kritik öneme sahiptir.  
  * Hedef alan adlarını sahte IP'ye eşlemek için yapılandırılmış bir etter.dns dosyası. Örneğin: facebook.com A 192.168.1.100.  
  * Saldırganın makinesinde (192.168.1.100) sahte içeriği sunan bir web sunucusu (örneğin, Apache).

#### **3\. DNS Spoofing için Adım Adım Kullanım**

1. **Ettercap Başlatma:** Grafiksel arayüz için terminalde ettercap \-G komutunu çalıştırın.  
2. **Hedef Belirleme:** **Targets \> Select Targets** menüsünden kurban IP adresini ve ağ geçidi IP adresini belirleyin.  
3. **ARP Poisoning (ARP Zehirlenmesi):** MITM için temel adımdır. **MitM \> ARP Poisoning** seçeneğini tıklayın ve “Sniff remote connections” kutucuğunu işaretleyin. Bu adım, ağdaki trafiği saldırganın makinesine yönlendirecektir.  
4. **DNS Spoofing Eklentisini Aktive Etme:** **Plugins \> Manage Plugins** menüsünden dns\_spoof eklentisine çift tıklayarak etkinleştirin.  
5. **Web Sunucusunu Başlatma:** Sahte bir web sitesi barındırmak için Apache sunucusunu sudo systemctl start apache2 komutuyla başlatın ve sahte web sayfasını /var/www/html/index.html dizinine yerleştirin.  
6. **Saldırıyı Başlatma:** Ettercap arayüzünde **Start \> Start Sniffing** seçeneğini tıklayın.

#### **4\. Öne Çıkan Özellikler**

* Grafiksel ve komut satırı arayüzleri.  
* Aktif ve pasif trafik dinleme desteği.  
* DNS spoofing dışında çeşitli MITM saldırıları için geniş eklenti kütüphanesi.  
* Birçok protokolü ayrıştırabilme yeteneği.

#### **5\. Referans Verilen Kaynaklar:**

Ettercap'in dns\_spoof eklentisinin etkinliği, doğrudan ARP zehirleme modülünün başarısına bağlıdır. Eğer ARP zehirlenmesi, örneğin Dinamik ARP Denetimi (DAI) gibi ağ savunmaları nedeniyle başarısız olursa, Ettercap aracılığıyla DNS spoofing de başarısız olacaktır. Çünkü bu durumda saldırgan, kurbanın DNS sorgularını ele geçirip manipüle edecek konumda olamaz. etter.conf dosyasındaki iptables kurallarını düzenleme gerekliliği, Ettercap'in güçlü olmasına rağmen, özellikle trafik yönlendirmesi gibi belirli işlevler için bazen daha derin sistem düzeyinde yapılandırma gerektirdiğini ortaya koyar. Bu, her senaryo için tamamen "tak ve çalıştır" bir araç olmadığını ve kullanıcıların temel Linux ağ bilgisine sahip olmalarının, basit ARP spoofing'in ötesine geçerek gelişmiş kullanım için önemli olduğunu gösterir.

### **B. Dnsspoof (Dsniff Suite): Odaklanmış DNS Sorgu Sahteciliği**

#### **1\. Genel Bakış ve Güçlü Yönleri**

Dsniff paketinin bir parçası olan Dnsspoof, "basit bir şekilde DNS sorgularını spoof etmek için kullanılır." Basitliği, hafifliği ve doğrudan komut satırı üzerinden çalıştırılabilmesi başlıca avantajlarıdır.

#### **2\. Platform ve Gereksinimler**

* **Platform:** Kali Linux (Dsniff paketi genellikle önceden yüklüdür). Yüklü değilse, sudo apt install dsniff ile kurulabilir.  
* **Gereksinimler:**  
  * Kök yetkileri.  
  * Eşlemeleri belirten özel bir "hosts" dosyası (örneğin, /usr/share/dsniff/dnsspoof.hosts veya kullanıcı tanımlı bir dosya): 192.168.1.100 facebook.com.  
  * Bağımsız olarak gerçekleştirilen ARP zehirlenmesi (örneğin, aynı Dsniff paketindeki arpspoof kullanılarak). Kaynak metinde şu komutlar gösterilmektedir:  
    Bash  
    sudo arpspoof \-i eth0 \-t 192.168.1.11 192.168.1.1   
    sudo arpspoof \-i eth0 \-t 192.168.1.1 192.168.1.11  
    Bu, dnsspoof'un MITM işlemini kendisinin yapmadığını açıkça gösterir.  
  * Sahte site için bir web sunucusu.

#### **3\. Adım Adım Kullanım**

1. **Hosts Dosyası Oluşturma:** Örneğin, echo "192.168.1.100 example.com" \> fakehosts.txt komutuyla bir hosts dosyası oluşturun.  
2. **ARP Zehirlenmesini Başlatma:** Yukarıda belirtildiği gibi arpspoof komutlarını kullanarak ARP zehirlenmesini başlatın.  
3. **Dnsspoof'u Çalıştırma:** sudo dnsspoof \-i eth0 \-f fakehosts.txt komutuyla Dnsspoof'u başlatın.

#### **4\. Öne Çıkan Özellikler**

* Sahte girişleri tanımlamak için basit bir hosts dosyası formatına dayanır.  
* arpspoof gibi diğer araçlarla birlikte çalışmak üzere tasarlanmıştır.  
* Yalnızca DNS yanıtı sahteciliğine odaklanır.

#### **5\. Önemli Not**

"Dnsspoof’un çalışması için gerçek DNS yanıtından önce sahte yanıtın ulaşması gerekir. Bu nedenle ağda düşük gecikme önemlidir." Bu, kritik bir operasyonel kısıtlamadır.

#### **6\. Referans Verilen Kaynaklar:**

Dnsspoof, Unix benzeri sistemlerde yaygın olan modüler bir araç tasarım felsefesini örnekler. Tek bir iş yapar (DNS yanıtı sahteciliği) ve diğer gerekli işlevler (MITM konumlandırması) için başka araçlara (örneğin arpspoof) güvenir. Bu, Ettercap gibi entegre paketlerle tezat oluşturur ve esneklik (örneğin, arpspoof uygun değilse farklı bir MITM tekniği kullanma) sunarken, saldırıyı düzenleme karmaşıklığını da artırır. Dnsspoof'un meşru DNS sunucusunu yenmesi için gereken "düşük gecikme" koşulu önemli bir faktördür. Hızlı DNS çözümleyicileri olan veya saldırganın gecikmesinin yüksek olduğu ağlarda Dnsspoof'un etkinliği azalır. Bu, Dnsspoof'un en çok saldırganın kurbana doğrudan, düşük gecikmeli bir bağlantıya sahip olduğu LAN ortamları için uygun olduğunu gösterir.

### **C. DNSChef: Gelişmiş DNS Proxy ile Spoofing**

#### **1\. Genel Bakış ve Güçlü Yönleri**

DNSChef, "DNS sorgularını özelleştirilmiş bir şekilde spoof etmek için kullanılan gelişmiş bir araçtır." Bir DNS proxy gibi davranması, yüksek düzeyde yapılandırılabilir olması, belirli alan adlarını hedefleyebilmesi veya tüm sorguları spoof edebilmesi ve çeşitli kayıt türlerini desteklemesi başlıca avantajlarıdır.

#### **2\. Platform ve Gereksinimler**

* **Platform:** Kali Linux. Kurulum gerekebilir: sudo apt install dnschef.  
* **Gereksinimler:**  
  * Kök yetkileri.  
  * Saldırganın makinesinde IP yönlendirmenin etkinleştirilmesi: sudo sysctl \-w net.ipv4.ip\_forward=1. Bu, DNSChef'in kendisi ağ geçidi değilse ancak meşru sorguları iletmesi gerekiyorsa gereklidir.  
  * Kurbanın DNS ayarlarının DNSChef çalıştıran makineye yönlendirilmesi gerekir (ARP spoofing, DHCP spoofing veya manuel yapılandırma ile sağlanır).  
  * Sahte site için bir web sunucusu.

#### **3\. Adım Adım Kullanım ve Yapılandırma Seçenekleri**

* **Belirli Alan Adlarını Spoof Etme:** sudo dnschef \--fakeip 192.168.1.100 \--fakedomains facebook.com,www.facebook.com. Diğer sorgular gerçek bir DNS sunucusuna yönlendirilir.  
* **Tüm Alan Adlarını Spoof Etme:** sudo dnschef \--fakeip 192.168.1.100.  
* **Detaylı Eşlemeler için Hosts Dosyası Kullanma:** echo "example.com=192.168.1.100" \> dnschef\_hosts.txt komutuyla bir hosts dosyası oluşturun, ardından sudo dnschef \--file dnschef\_hosts.txt komutuyla çalıştırın.

#### **4\. Öne Çıkan Özellikler**

* Proxy gibi davranır: Hedeflenmeyen sorguları meşru DNS sunucularına iletir.  
* Hangi alan adlarının spoof edileceği üzerinde ayrıntılı kontrol sağlar.  
* Birden fazla DNS kayıt türünü (A, MX, CNAME vb.) destekler.  
* Sahte kayıtları tanımlamak için harici bir dosya kullanabilir.

#### **5\. Referans Verilen Kaynaklar:**

DNSChef'in proxy yeteneği ve seçici spoofing (örneğin, \--fakedomains parametresi) genel spoofing'e göre daha sofistike bir yaklaşım sunar. Bu, ilgisiz hizmetleri kesintiye uğratarak kullanıcıları veya Saldırı Tespit Sistemlerini (IDS) uyarabilecek daha az hedefli saldırılara kıyasla daha gizli ve hedefli saldırılara olanak tanır. DNSChef saldırganın makinesinde bir DNS sunucusu olarak çalışsa da, kurbanın DNSChef'i kendi DNS sunucusu olarak kullanmasını sağlamak, başarının kritik önkoşuludur. Bu genellikle, kurbanın DNS ayarlarını değiştirmek için ARP spoofing (gerçek DNS sunucusunu veya ağ geçidini taklit etmek) veya DHCP spoofing (DNSChef'in IP'sini DNS sunucusu olarak atamak) gibi ayrı bir saldırı vektörüne dayanır, bu da genel saldırı başarısı için bir bağımlılık zincirini vurgular.

### **D. Bettercap: Modern, Modüler MITM Güç Merkezi**

#### **1\. Genel Bakış ve Güçlü Yönleri**

Bettercap, "modern ve esnek bir MITM aracıdır ve DNS spoofing için güçlü bir seçenektir." Yüksek düzeyde modüler olması ("caplet" adı verilen betiklerle görev otomasyonu), aktif geliştirme süreci, çeşitli MITM tekniklerini desteklemesi ve güçlü interaktif oturumu başlıca avantajlarıdır.

#### **2\. Platform ve Gereksinimler**

* **Platform:** Kali Linux (genellikle önceden yüklüdür). Yüklü değilse, sudo apt install bettercap.  
* **Gereksinimler:**  
  * Kök yetkileri.  
  * IP yönlendirme: sudo sysctl \-w net.ipv4.ip\_forward=1.  
  * Sahte site için bir web sunucusu.

#### **3\. Adım Adım Kullanım**

1. **Bettercap Başlatma:** sudo bettercap \-iface eth0.  
2. **Parametreleri Ayarlama (Bettercap interaktif oturumunda):**  
   set arp.spoof.targets 192.168.1.11   
   set dns.spoof.domains facebook.com,\*.facebook.com  
   set dns.spoof.address 192.168.1.100 

3. **Modülleri Aktive Etme:**  
   arp.spoof on  
   dns.spoof on

4. **Saldırıyı Sonlandırma:** dns.spoof off; arp.spoof off.

#### **4\. Öne Çıkan Özellikler**

* Görevleri otomatikleştirmek için "caplet"lerle modüler tasarım.  
* Dahili ARP spoofer, DNS spoofer ve diğer ağ saldırı modülleri.  
* Dinamik kontrol için interaktif komut satırı arayüzü.  
* Aktif olarak bakımı yapılan ve yeni özelliklerle güncellenen bir araçtır.

#### **5\. Referans Verilen Kaynaklar:**

Bettercap, Ettercap gibi eski araçlardan evrimleşmiş bir araç olup, karmaşık MITM senaryoları için daha akıcı, betiklenebilir ve genellikle daha kararlı bir deneyim sunar. Caplet sistemi, otomasyon için önemli bir ilerlemedir ve daha karmaşık saldırı zincirlerinin kolayca tanımlanıp yürütülmesine olanak tanır. Bettercap içinde ARP spoof hedeflerini, DNS spoof alan adlarını ve sahte adresi ayarlayabilme ve ardından modülleri açıp kapatabilme yeteneği, son derece entegre bir yaklaşımı gösterir. Bu, Dnsspoof'un harici arpspoof komutuna ihtiyaç duymasına kıyasla, temel MITM ve DNS spoofing işlemleri için harici araçlara olan bağımlılığı azaltır ve saldırı yürütme sürecini kullanıcı için basitleştirir.

### **E. DDSpoof: DHCP Manipülasyonu ile DNS Spoofing**

#### **1\. Genel Bakış ve Güçlü Yönleri**

"DDSpoof, DHCP protokolünü kullanarak DNS spoofing yapmak için özel bir araçtır." DHCP sunucularını manipüle ederek istemcilere sahte bir DNS sunucusu atar. Bu yaklaşımın gücü, DHCP üzerinden IP yapılandırması alan ağdaki daha geniş bir cihaz yelpazesini potansiyel olarak etkileyebilmesidir.

#### **2\. Platform ve Gereksinimler**

* **Platform:** Kali Linux. GitHub'dan manuel kurulum gerektirir: git clone https://github.com/akamai/ddspoof, ardından pip install \-r requirements.txt.  
* **Gereksinimler:**  
  * Kök yetkileri.  
  * Python 3 ve pip.  
  * Saldırganın, hedef DHCP sunucusu ve istemcilerle aynı yayın alanında (broadcast domain) olması gerekir.  
  * İstemcilere sağlanan IP adresinde (örnekte 192.168.1.100) çalışan ayrı bir DNS sunucusu (DNSChef veya özel bir sunucu gibi). DDSpoof'un kendisi sahte DNS yanıtlarını sunmaz, sadece istemcilere DNS için nereye gideceklerini söyler.  
  * Sahte site için bir web sunucusu.

#### **3\. Adım Adım Kullanım**

1. **Ağ Taraması (DHCP sunucularını bulmak için):** sudo python3 ddspoof.py \--interface eth0 \--scan.  
2. **DHCP DNS Saldırısı:** sudo python3 ddspoof.py \--interface eth0 \--dns 192.168.1.100. Bu komut, istemcilerin DNS sunucusu olarak 192.168.1.100 adresini kullanmasını sağlamaya çalışır.

#### **4\. Öne Çıkan Özellikler**

* DNS ayarlarını kontrol etmek için DHCP altyapısına saldırmaya odaklanır.  
* Mevcut DHCP sunucularını tarayabilir.  
* DHCP istemcilerine kötü amaçlı bir DNS sunucusu IP'si sağlamayı hedefler.

#### **5\. Referans Verilen Kaynaklar:**

DDSpoof, DNS yanıtlarını transit halindeyken doğrudan taklit etmek (Ettercap veya ARP zehirlenmesi ile Dnsspoof gibi) yerine, istemcinin *ilk ağ yapılandırmasını* bozarak oyunu değiştirir. Bu, DNS için daha temel bir uzlaşma düzeyidir ve kurbanın sonraki tüm DNS sorgularının meşru bir şekilde saldırganın DNS sunucusuna gitmesi anlamına gelir; bu sorgular için DNS paketlerinin daha fazla ele geçirilmesine gerek kalmaz. Ancak DDSpoof'un kendisi yalnızca DNS trafiğini saldırgan kontrolündeki bir IP'ye yönlendirir. Saldırganın ayrıca, sahte DNS kayıtlarını gerçekten sunmak için bu IP adresinde ayrı bir DNS spoofing sunucusu (DNSChef veya kötü amaçlı olarak yapılandırılmış BIND gibi) çalıştırması gerekir. DDSpoof, DNS için "yük sunucusu" değil, "teslimat mekanizmasıdır", bu da DDSpoof saldırısını çok bileşenli bir kurulum haline getirir.

### **F. Social Engineering Toolkit (SET): DNS Spoofing ile Kimlik Bilgisi Toplama Entegrasyonu**

#### **1\. Genel Bakış ve Güçlü Yönleri**

"SET, sosyal mühendislik saldırıları için kullanılır ve DNS spoofing ile birlikte phishing sayfaları oluşturmak için idealdir." İnandırıcı kimlik avı web sitelerinin oluşturulmasını otomatikleştirmesi, çeşitli saldırı vektörlerini entegre etmesi ve sosyal mühendislik kampanyalarında yaygın olarak kullanılması başlıca avantajlarıdır.

#### **2\. Platform ve Gereksinimler**

* **Platform:** Kali Linux (genellikle önceden yüklüdür). sudo setoolkit ile başlatılır.  
* **Gereksinimler:**  
  * Kök yetkileri.  
  * Kurbanları SET tarafından barındırılan kimlik avı sitesine yönlendirmek için ayrı bir DNS spoofing mekanizması (örneğin, Ettercap, Bettercap). SET öncelikle web sitesi klonlama ve kimlik bilgisi toplama işlemlerini yapar, DNS yönlendirmesini kendisi yapmaz.

#### **3\. Adım Adım Kullanım (Site Klonlama için)**

1. **SET Başlatma:** sudo setoolkit.  
2. **Menülerde Gezinme:** **Social Engineering Attacks \> Website Attack Vectors \> Credential Harvester Attack Method \> Site Cloner** seçeneklerini izleyin.  
3. **Hedef URL'yi Girme:** Klonlamak için hedef web sitesinin URL'sini (örneğin, facebook.com) girin. SET, klonu otomatik olarak oluşturur ve Apache'yi bunu sunacak şekilde yapılandırır.  
4. **Entegrasyon:** Kurbanın orijinal siteye (örneğin, facebook.com) yönelik isteklerini, SET'in klonlanmış siteyi barındırdığı IP adresine (genellikle saldırganın Kali makinesi) yönlendirmek için daha önce bahsedilen DNS spoofing araçlarından birini kullanın.

#### **4\. Öne Çıkan Özellikler**

* Otomatik web sitesi klonlama.  
* Kimlik bilgisi toplama yetenekleri.  
* Geniş bir sosyal mühendislik saldırı vektörleri yelpazesi.  
* Kimlik avı kampanyalarının kurulumunu basitleştirir.

#### **5\. Referans Verilen Kaynaklar:**

SET, *yükü* (sahte web sitesi) oluşturmak için güçlüdür ancak *teslimat mekanizması* (DNS spoofing) için diğer araçlara güvenir. Bu, "DNS spoofing görevleri"ndeki rolünün, genel saldırıyı daha etkili hale getiren kötü amaçlı uç noktayı sağlamak olduğunu gösterir. SET'in dahil edilmesi, DNS spoofing gibi teknik istismarların genellikle insan psikolojisini hedefleyen daha büyük saldırıların (sosyal mühendislik) bileşenleri olduğunu vurgular. Nihai amaç genellikle bir kullanıcıyı bilgi ifşa etmeye veya kötü amaçlı yazılım çalıştırmaya kandırmaktır; bu, teknik yönlendirme (DNS spoof) ve psikolojik manipülasyon (SET'ten gelen inandırıcı sahte site) katmanlı bir saldırıyı gösterir.

## **III. Karşılaştırmalı Analiz ve Araç Seçim Rehberi**

Bu bölüm, Kali Linux'ta bulunan DNS spoofing araçlarının güçlü yönlerini ve ideal kullanım senaryolarını özetleyerek, kullanıcıların belirli ihtiyaçlarına en uygun aracı seçmelerine yardımcı olmayı amaçlamaktadır. Ayrıca, araçların temel operasyonel özelliklerini karşılaştıran bir matris sunulacaktır.

### **A. Araçların Güçlü Yönleri ve İdeal Senaryolara Genel Bakış**

Her bir aracın temel avantajları ve en uygun olduğu durumlar aşağıda özetlenmiştir:

* **Ettercap:** Hepsi bir arada MITM GUI/CLI aracıdır; genel LAN tabanlı saldırılar ve MITM konseptlerini keşfetmek için iyidir.  
* **Dnsspoof:** Basit, hafif bir CLI aracıdır; hızlı DNS kaydı sahteciliği için uygundur, ancak harici bir ARP spoofer gerektirir. Basit DNS kayıt testleri için idealdir.  
* **DNSChef:** Gelişmiş bir DNS proxy'sidir; hassas kontrol sağlar ve hedeflenmiş spoofing veya özel DNS yanıtları oluşturmak için mükemmeldir. Gelişmiş DNS manipülasyon laboratuvarları için uygundur.  
* **Bettercap:** Modern, modüler, betiklenebilir bir MITM çerçevesidir; güçlü ve esnektir. Betiklenmiş/otomatikleştirilmiş MITM testleri için tercih edilebilir.  
* **DDSpoof:** İstemci DNS ayarlarını kontrol etmek için DHCP'yi hedefler; ağ yapılandırması yoluyla daha geniş etki için kullanılır. DHCP güvenlik açıklarını anlamak için faydalıdır (ayrı bir kötü amaçlı DNS sunucusu gerektirir).  
* **SET (Social Engineering Toolkit):** Kimlik avı/kimlik bilgisi toplama odaklıdır; DNS spoofing araçlarını, kötü amaçlı web içeriği sağlayarak tamamlar. Kimlik avı kampanya simülasyonları için kullanılır (başka bir DNS spoofing aracıyla birlikte).

Araç seçimi yapılırken dikkate alınması gerekenler:

* GUI ile kullanım kolaylığı ve entegre MITM için: **Ettercap**.  
* Hızlı, komut satırı tabanlı spesifik DNS kaydı enjeksiyonu (manuel MITM ile) için: **Dnsspoof**.  
* Sofistike DNS proxy'leme ve seçici spoofing için: **DNSChef**.  
* Modern, güçlü ve betiklenebilir bir MITM çerçevesi için: **Bettercap**.  
* İstemci DNS ayarlarını kontrol etmek amacıyla DHCP'ye yönelik saldırılar için: **DDSpoof**.  
* Birincil amaç klonlanmış bir site aracılığıyla kimlik avı ve kimlik bilgisi toplama ise: **SET** (başka bir DNS spoofing aracıyla birlikte).

Bu karşılaştırma, tek bir "en iyi" aracın olmadığını ortaya koymaktadır. "En iyi" araç, büyük ölçüde saldırı senaryosuna, istenen kontrol düzeyine ve SET ile kimlik avı gibi diğer saldırı aşamalarıyla entegrasyon ihtiyacına bağlı olarak bağlamsaldır. Etkili DNS spoofing'in genellikle tek bir komuttan ziyade bir eylemler/araçlar zincirini içerdiği de anlaşılmaktadır. Örneğin, ARP spoofing \+ DNS yanıtı oluşturma \+ sahte web içeriği sunma. Araçlar, bu zincirin ne kadarını dahili olarak yönettikleri konusunda farklılık gösterir.

### **B. Kali Linux'ta DNS Spoofing Araçları: Karşılaştırmalı Özellik Matrisi**

Aşağıdaki tablo, kullanıcıların araçları temel operasyonel özelliklerine göre hızlı bir şekilde karşılaştırmasına olanak tanıyarak, belirli bağlamları ve beceri düzeyleri için bilinçli bir seçim yapmalarını kolaylaştırmayı amaçlamaktadır. Bu tablo, kullanıcının "en iyi araçlar" sorgusuna, kendi eğitim amaçları veya penetrasyon testi senaryoları için hangi aracın/araçların "en iyi" olduğuna karar vermelerine yardımcı olarak doğrudan yanıt verir.

| Araç Adı | Birincil Mekanizma | MITM Yeteneği | Kullanım/Kurulum Kolaylığı | Temel Özellikler | Bağımlılıklar/Ön Koşullar | İdeal Kullanım Senaryosu (Eğitim Bağlamı) | Çıktı/Günlükleme |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Ettercap | MITM ve DNS eklentisi | Dahili (ARP, ICMP) | Başlangıç dostu GUI | GUI, dns\_spoof eklentisi, çeşitli protokoller | Kök erişimi, etter.conf düzenlemesi (iptables için), Web Sunucusu | Genel LAN MITM keşfi, entegre saldırı senaryoları | Arayüzde canlı trafik, eklentiye bağlı olarak günlükler |
| Dnsspoof | Bağımsız DNS sahteciliği | Harici araca dayanır (örn: arpspoof) | Orta seviye CLI | Hosts dosyası tabanlı, hafif | Kök erişimi, ARP Spoofing, Web Sunucusu, Hosts dosyası | Basit DNS kayıt testleri, modüler saldırı zincirleri | Standart çıktıya sınırlı bilgi, genellikle ARP spoofer'dan ayrı izleme gerekir |
| DNSChef | DNS proxy | Harici araca dayanır (kurbanı yönlendirmek için) | Orta-İleri seviye CLI | Seçici spoofing, proxy'leme, çeşitli kayıt türleri | Kök erişimi, IP Yönlendirme, Web Sunucusu, Kurbanın DNS'ini yönlendirme mekanizması | Gelişmiş DNS manipülasyon laboratuvarları, hedeflenmiş spoofing | Konsola ayrıntılı sorgu ve yanıt bilgileri |
| Bettercap | Modern MITM çerçevesi | Dahili (ARP, vb.) | Orta seviye CLI (interaktif) | Modüler, capletler (betikleme), aktif geliştirme | Kök erişimi, IP Yönlendirme, Web Sunucusu | Betiklenmiş/otomatikleştirilmiş MITM testleri, modern MITM teknikleri keşfi | Kapsamlı interaktif oturum geri bildirimi, olay günlüğü |
| DDSpoof | DHCP manipülasyonu | N/A (DHCP saldırısı) | Orta seviye CLI (Python) | DHCP sunucu hedefleme, ağ taraması | Kök erişimi, Python, Ayrı Sahte DNS Sunucusu, Web Sunucusu | DHCP güvenlik açıklarını anlama, ağ yapılandırma saldırıları | Konsola tarama ve saldırı durumu hakkında bilgi |
| SET | Web sitesi klonlayıcı / Sosyal Mühendislik Aracı | N/A (DNS spoofing için harici araca dayanır) | Menü tabanlı (kolay) | Site klonlama, kimlik bilgisi toplama, geniş sosyal mühendislik vektörleri | Kök erişimi, Harici DNS Spoofing Aracı | Kimlik avı kampanya simülasyonu, sosyal mühendislik teknikleri uygulaması | Toplanan kimlik bilgileri için dosya tabanlı günlükleme, Apache günlükleri |

## **IV. DNS Spoofing Operasyonlarında Kritik Hususlar**

DNS spoofing saldırılarının planlanması ve yürütülmesi sırasında dikkate alınması gereken önemli teknik ve çevresel faktörler bulunmaktadır. Bu faktörler, saldırının başarısını doğrudan etkileyebilir ve aynı zamanda potansiyel savunma mekanizmalarını anlamak için de kritik öneme sahiptir.

### **A. HTTPS/SSL/TLS Zorluğu**

HTTPS (Güvenli HTTP), trafiği şifrelemek ve sunucunun kimliğini doğrulamak için SSL/TLS sertifikalarını kullanır. Bu, DNS spoofing saldırıları için önemli bir engel teşkil eder. Bir kullanıcı HTTPS kullanan bir siteye yönlendirildiğinde, tarayıcı, talep edilen alan adı için geçerli bir SSL sertifikası bekler. Saldırganın sahte sitesi genellikle bu geçerli sertifikaya sahip olmayacaktır. Sonuç olarak, tarayıcılar belirgin güvenlik uyarıları (sertifika uyuşmazlığı, güvenilmeyen yayıncı vb.) göstererek çoğu kullanıcıyı caydırır. "HTTPS kullanan sitelerde DNS spoofing yapmak daha zordur çünkü SSL sertifikaları sahte siteleri tespit edebilir".

sslstrip veya sslstrip+ gibi araçlar, HTTPS bağlantılarını HTTP'ye düşürmeye veya araya girip sahte bir sertifika sunmaya çalışır. Ancak, HSTS (HTTP Strict Transport Security) ve tarayıcı sabitleme (browser pinning) gibi mekanizmalar nedeniyle bu tür araçlar giderek daha az etkili olmaktadır. Kullanıcıya gösterilen uyarı mesajları, saldırının başarısı önünde önemli bir engeldir: "bu kullanıcıda uyarı mesajlarına neden olabilir."

### **B. Ağ Ortamı Ön Koşulları ve Sınırlamaları**

Bu raporda açıklanan DNS spoofing tekniklerinin çoğu, özellikle ARP zehirlenmesine dayananlar, saldırganın kurbanla aynı ağ segmentinde olmasını gerektiren Yerel Alan Ağı (LAN) saldırılarıdır. "DNS spoofing genellikle yerel ağda (LAN) çalışır ve saldırganın hedefle aynı ağda olması gerekir". Uzak DNS spoofing (harici DNS sunucularına yönelik önbellek zehirlenmesi) farklı ve daha karmaşık bir saldırı türüdür ve bu Kali araçları tarafından doğrudan kapsanmaz; bu araçlar daha çok istemci tarafı veya yerel DNS manipülasyonuna odaklanır.

Ağ savunmalarının etkisi de önemlidir. Dinamik ARP Denetimi (DAI) gibi ARP zehirlenmesi tespiti/önlenmesi mekanizmaları, port güvenliği ve Saldırı Tespit/Önleme Sistemleri (IDS/IPS), bu tür saldırıları engelleyebilir veya zorlaştırabilir.

### **C. Savunma Önlemleri ve Tespit Teknikleri**

DNS spoofing saldırılarına karşı korunmak ve bu tür girişimleri tespit etmek için çeşitli yöntemler mevcuttur:

* **DNSSEC (DNS Güvenlik Eklentileri):** DNSSEC, DNS yanıtları için kaynak doğrulaması ve veri bütünlüğü sağlayarak, sahte yanıtların doğrulayıcı çözümleyiciler tarafından kabul edilmesini engeller. "DNSSEC kullanarak DNS sorgularını doğrulayın".  
* **HTTPS Farkındalığı:** Kullanıcılara her zaman HTTPS aramaları ve tarayıcı sertifika uyarılarına dikkat etmeleri tavsiye edilir. "HTTPS kullanın ve sertifika uyarılarını dikkate alın."  
* **ARP Spoofing Tespit Araçları:** arpwatch, Snort veya diğer Ağ Saldırı Tespit Sistemleri (NIDS) gibi araçlar, ARP anomalilerini tespit edebilir. "ARP spoofing tespit araçları (örneğin, Snort) kullanın."  
* **Güvenli DHCP:** DHCP gözetimi (snooping) ve DAI uygulamak, sahte DHCP sunucularını (DDSpoof ile ilgili) ve ARP zehirlenmesini önleyebilir.  
* **VPN'ler (Sanal Özel Ağlar):** Güvenilir bir VPN kullanmak, DNS sorgularını şifreleyebilir ve güvenli bir tünel üzerinden yönlendirerek yerel ağ manipülasyon girişimlerini atlatabilir.  
* **Güvenilir Özyinelemeli DNS Sunucuları Kullanmak:** İstemcileri, DNSSEC doğrulaması ve filtreleme uygulayan saygın DNS çözümleyicilerini (örneğin, Quad9, Cloudflare DNS) kullanacak şekilde yapılandırmak.

HTTPS ile ilgili zorluklar ve DNSSEC gibi savunmaların geliştirilmesi, saldırganlar ve savunmacılar arasında süregelen bir "silahlanma yarışını" göstermektedir. Saldırı teknikleri geliştikçe, koruyucu önlemler de gelişir ve eski saldırı yöntemlerini zamanla daha az etkili hale getirir. Tek bir savunmanın kusursuz olmadığı anlaşılmalıdır. Karşı önlemler listesi (DNSSEC, HTTPS, ARP tespiti, VPN'ler), DNS spoofing ve ilgili MITM saldırılarına karşı sağlam bir koruma için katmanlı bir güvenlik yaklaşımının (derinlemesine savunma) gerekli olduğunu ima eder.

## **V. Etik Zorunluluklar ve Sorumlu Uygulama**

DNS spoofing gibi güçlü siber saldırı araç ve tekniklerinin incelenmesi, beraberinde ciddi etik ve yasal sorumluluklar getirir. Bu bölüm, bu sorumlulukların altını çizerek, bu tür bilgilerin yalnızca meşru ve kontrollü ortamlarda kullanılmasının önemini vurgulamaktadır.

### **A. Yasal ve Etik Sorumlulukların Tekrar Vurgulanması**

Yetkisiz DNS spoofing girişimlerinin yasa dışı ve etik dışı olduğu kesin bir dille bir kez daha vurgulanmalıdır. "DNS spoofing, izinsiz yapıldığında yasa dışıdır ve ciddi etik sorunlar doğurur". Bu tür eylemler, birçok ülkede siber suçlarla ilgili yasalar kapsamında değerlendirilir ve ciddi yaptırımlara tabidir. Örneğin, ABD'deki Bilgisayar Dolandırıcılığı ve Kötüye Kullanım Yasası (CFAA) ve benzeri uluslararası mevzuatlar, yetkisiz erişim, bilgisayar hizmetlerinin kesintiye uğratılması ve (kimlik avı için kullanıldığında) elektronik dolandırıcılık gibi suçlamaları içerebilir.

### **B. Yetkisiz Kullanımın Sonuçları**

DNS spoofing tekniklerinin yetkisiz ve kötü niyetli kullanımı, hem bireysel hem de kurumsal düzeyde ciddi sonuçlar doğurabilir. Kişisel olarak, fail cezai kovuşturma, para cezaları, hapis cezası, iş kaybı ve itibar zedelenmesi gibi sonuçlarla karşılaşabilir. Kurbanlar açısından ise finansal kayıp, kimlik hırsızlığı, kötü amaçlı yazılım bulaşması ve kurumlara veya hizmetlere olan güvenin sarsılması gibi olumsuz etkiler söz konusu olabilir.

### **C. Kontrollü Ortamların Zorunluluğu**

Bu raporda açıklanan araçlar ve teknikler *yalnızca* aşağıdaki kontrollü ortamlarda kullanılmalıdır:

* Öğrenme amacıyla oluşturulmuş özel kişisel laboratuvar ortamları (örneğin, üretim ağlarından izole edilmiş sanal makineler).  
* Sistem sahibinden açık, yazılı kapsam ve izin alınarak yürütülen yetkili penetrasyon testi çalışmaları.  
* Eğitmen gözetiminde resmi siber güvenlik eğitim ortamları.

Kaynak metindeki özet bu noktayı pekiştirmektedir: "Bu teknikleri yalnızca eğitim veya izinli penetrasyon testleri için kullanmanız gerektiğini tekrar hatırlatırım."

Bu saldırı araçları hakkındaki ayrıntılı bilgi, savunmacılar için gerekli olmakla birlikte, kötüye kullanılması durumunda doğal olarak risk taşır. Rapor boyunca yapılan güçlü etik vurgu sadece bir formalite değil, sorumlu siber güvenlik eğitiminin kritik bir bileşenidir. Orijinal kaynak metnin kendisinin etik uyarılarla bu kadar yoğun bir şekilde donatılmış olması, siber güvenlik topluluğu içinde kötüye kullanım potansiyeli ve özdenetim ile net rehberlik ihtiyacı hakkında olgun bir anlayış olduğunu göstermektedir. Bu, Kali Linux ve araçlarını kullananların etik ilkelere aşina olmaları ve bunlara uymaları yönünde bir beklenti olduğunu ima eder.

## **VI. Sonuç: Etkili ve Etik Kullanım için Bilginin Sentezlenmesi**

Bu rapor, Kali Linux ortamında DNS spoofing gerçekleştirmek için kullanılan temel araçları ve teknikleri ayrıntılı bir şekilde incelemiş, operasyonel adımlarını, güçlü yönlerini ve potansiyel zorluklarını ele almıştır. Ancak, bu teknik bilginin ötesinde, etik ve yasal sorumlulukların her zaman öncelikli olması gerektiği vurgulanmıştır.

### **A. Birincil Araçların ve Kontrollü Değerlendirmelerdeki Stratejik Değerlerinin Özeti**

İncelenen altı temel araç ve yaklaşım – **Ettercap, Dnsspoof, DNSChef, Bettercap, DDSpoof** ve **SET** – her biri farklı senaryolara ve hedeflere uygun benzersiz avantajlar sunmaktadır. Ettercap ve Bettercap, kapsamlı MITM yetenekleri sunarken; Dnsspoof ve DNSChef, daha odaklanmış veya özelleştirilmiş DNS manipülasyonu sağlar. DDSpoof, DHCP protokolünü hedef alarak farklı bir saldırı vektörü sunarken, SET, DNS spoofing'i sosyal mühendislik ve kimlik avı kampanyalarıyla entegre eder. Bu araçların *eğitimsel keşif ve yetkili testler* bağlamındaki stratejik değeri, siber güvenlik uzmanlarının saldırganların kullandığı yöntemleri anlamalarına ve dolayısıyla daha etkili savunma mekanizmaları tasarlamalarına yardımcı olmalarından kaynaklanır.

### **B. Sorumlu Keşif ve Sürekli Öğrenmeye Son Vurgu**

Siber güvenlik, sürekli gelişen bir alandır. Tehditler ve savunmalar sürekli bir evrim içindedir, bu da profesyonellerin ve meraklıların bilgilerini güncel tutmalarını gerektirir. Bu öğrenme süreci, her zaman güçlü bir etik pusula ile eşleştirilmelidir. Bu raporda sunulan bilgilerin amacı, yetkisiz bir şekilde sistemleri kırmak değil, güvenliği inşa etmektir.

Bu raporun yalnızca bu araçların *nasıl* kullanılacağını değil, aynı zamanda siber güvenlik uzmanları için bunları anlamanın *neden* önemli olduğunu (yani onlara karşı savunmak için) ve bunları kullanmanın *ne zaman* uygun olduğunu (etik ve yasal olarak) açıklaması hedeflenmiştir. Nihayetinde, bu saldırı araç ve tekniklerini güçlü bir etik çerçeve içinde detaylandırarak, okuyucuların daha iyi savunmacılar olmaları için güçlendirilmesi amaçlanmaktadır. Saldırganın zihniyetini ve araç setini anlamak, tehditleri öngörmek ve azaltmak için hayati öneme sahiptir.
