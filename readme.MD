* Hergele Case

---
* Yüksek Trafik ve Indexleme

MongoDB'de veri trafiği artarsa performans düşüklüğü olabileceği için sorguların daha hızlı sonuçlanması amacı ile indexleme yaptım.
Matchlemeler yapılırken kullanılan, sorgularda en çok kullanılan alanlardan GUID, CC_no, user_NO gibi alanları indexledim.
Bunun dışında birden fazla sunucuyu ayağa kaldırmak, sistem'e yüksek trafik gelse bile sistemi stabil tutar.
Performansı arttırmakı için başka yapılabilecek şey de cacheig. Bellekte tutarak bazı alanları, veritabanı üzerindeki
maaliyeti düşürebiliriz.


---
* DB

cards, counter, responses, transactions ve users olmak üzere 5 adet collection'dan oluşuyor.

![image](https://user-images.githubusercontent.com/96119894/235516720-a7685807-12fd-4e3a-843a-002a98434a43.png)
![image](https://user-images.githubusercontent.com/96119894/235515078-5c065c87-7d9b-49c2-91cc-46bd21923767.png)
![image](https://user-images.githubusercontent.com/96119894/235515117-ef672b1a-db2e-425b-b2cd-7568c475068f.png)
![image](https://user-images.githubusercontent.com/96119894/235515191-1cbd4ed6-bddd-4729-8c5e-1d05dc238797.png)
![image](https://user-images.githubusercontent.com/96119894/235515220-9878d525-b2fd-4e1b-8997-6315c1c94ec0.png)


* API
API 5 adet endpointten oluşuyor. 4 tanesi case'de verilen endpointler. Bir tanesi de login olup token almak için /login
endpinti.

Auth olarak, UserNo ve AuthCode'u username ve password parametreleri olarak alıyor ve token oluşuyor,
Login dışındaki işlemlerde ise Header'da Authorization, UserNo ve Filo zorunlu alandır.
Token süreleri 30 gün olarak ayarlı. Header'da {Authorization : Bearer <TOKEN>} olarak verilmeli.

Endpointe gelen isteğin data tipinin doğru olup olmadığı Cerberus ile schema.py dosyasında tanımlanmlanan şemaya göre
kontrol ediliyor.

---

* AWS

AWS üzerinden 2 adet ec2 instance'ı ayağa kaldırdım ve ikisine de projemi ssh ile bağlanıp yükledim. İkinci instance health check'e bağlı.
Tanımlanan health check ana instance'a düzenli olarak ping atıyor health check için.

80 Port'ta güvenli bir şekilde çalışması için NGINX kurulumu yaptım.

İkinci instance'a crob job tanımlandı ve ayağa kalktığında otomatik olarak nginx'i ve api'yi ayağa kaldırmak için.

![image](https://user-images.githubusercontent.com/96119894/235514851-1dff4ea5-dbb0-4c82-852a-718278414d71.png)

![image](https://user-images.githubusercontent.com/96119894/235515400-7a9a65ae-34a6-4095-8f9c-4752dfb52f38.png)


---

* NOT

1. "Kart Saklama Listesi" api endpointi'nin dökümantasyonunu tam olarak anlayamadım ve ordakinden farklı bir şekilde tasarladım. Kullanıcının GUID'sini alıp bütün kartları dönüyor.
2. User collection'unda balance değeri o kullanıcının sadece selected_card'ında bulunan balance miktarıdır.








































