# GeoPulse-OSINT-Bot
# 🌍 GeoPulse 4.0 - Otonom OSINT Ajanı

GeoPulse, açık kaynaklı ağları (BBC World vb.) 7/24 dinleyen, verileri parçalayan ve sadece önceden belirlenmiş kritik jeopolitik/finansal tetikleyiciler (Savaş, Yaptırım, Petrol, Fed vb.) tespit ettiğinde özel Telegram hattına anlık rapor geçen otonom bir yapay zeka istihbarat botudur.

## 🚀 Özellikler
* **Keskin Nişancı Filtresi:** Hedef kelimeler geçmiyorsa sessiz kalır, bilgi kirliliği yaratmaz.
* **Gerilla Mimarisi:** AWS veya Azure gibi bulut sunuculara ihtiyaç duymaz. Doğrudan bir Android telefonun içindeki Termux (Linux) terminalinde, sıfır maliyetle çalışacak şekilde tasarlanmıştır.
* **Anti-Blokaj:** İnsan taklidi yapan `fake-useragent` altyapısı sayesinde bot algılayıcılara takılmaz.

## 🛠️ Kullanılan Teknolojiler
* Python 3
* BeautifulSoup4 & lxml (Veri Kazıma ve Ayrıştırma)
* Requests (Ağ Sızma)
* Telegram Bot API (Şifreli İletişim)

*(Not: Sistemin detaylı mimari analiz raporu repo içindeki PDF dosyasında mevcuttur. 
