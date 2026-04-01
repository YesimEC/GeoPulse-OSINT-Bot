import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import time
import random

def istihbarat_topla(hedef_url):
    ua = UserAgent()
    max_deneme = 3
    bekleme_suresi = 2 
    
    for deneme in range(max_deneme):
        insan_beklemesi = random.uniform(1.0, 2.5)
        time.sleep(insan_beklemesi)
        
        kamuflaj = {'User-Agent': ua.random}
        
        try:
            cevap = requests.get(hedef_url, headers=kamuflaj, timeout=10)
            
            if cevap.status_code == 200:
                print("BAŞARILI: Karşı sitenin duvarı aşıldı. Veriler ayıklanıyor...\n")
                
                # BeautifulSoup (Neşter) devreye giriyor. Çöpleri atıp sadece haberleri alacak.
                nester = BeautifulSoup(cevap.text, "xml")
                
                # Sitedeki tüm haber başlıklarını (title) bul
                haberler = nester.find_all("title")
                
                print("--- SON DAKİKA KÜRESEL İSTİHBARAT RAPORU ---")
                # İlk haber genelde sitenin adıdır, onu atlayıp son 5 haberi alıyoruz
                for i in range(1, 6):
                    # Eğer 5'ten az haber varsa hata vermesin diye kontrol ediyoruz
                    if i < len(haberler):
                        print(f"[#] {haberler[i].text}")
                
                print("-" * 42)
                return True # Başarılı oldu, çık.
                
            else:
                print(f"DİKKAT: Duvara çarptık. Hata Kodu: {cevap.status_code}")
                
        except Exception as hata:
            print(f"HATA: Hedefe ulaşılamadı. {hata}")
            
        time.sleep(bekleme_suresi)
        bekleme_suresi = bekleme_suresi * 2 
        
    print("SİSTEM: İstihbarat toplanamadı.")
    return False

# --- GERÇEK SAHA OPERASYONU ---
print("GEOPULSE 4.0: DÜNYA HABERLERİ SENSÖRÜ AKTİF EDİLİYOR...\n")

# Hedef: BBC Dünya Haberleri Canlı Akışı (Bedava, yasal ve anlık)
gercek_hedef = "http://feeds.bbci.co.uk/news/world/rss.xml" 

istihbarat_topla(gercek_hedef)