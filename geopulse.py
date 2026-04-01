import os
import time
import random
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from dotenv import load_dotenv

load_dotenv()
GIZLI_ANAHTAR = os.getenv("TELEGRAM_TOKEN").strip()
HEDEF_KOORDINAT = os.getenv("CHAT_ID").strip()

def siyah_terminale_bildir(mesaj_icerigi):
    url = f"https://api.telegram.org/bot{GIZLI_ANAHTAR}/sendMessage"
    paket = {"chat_id": HEDEF_KOORDINAT, "text": mesaj_icerigi, "parse_mode": "HTML"}
    try:
        requests.post(url, data=paket, timeout=10)
    except:
        print("SİSTEM: Mesaj gönderilemedi, hat kopuk.")

KIRMIZI_BULTEN = [
    "war", "strike", "missile", "attack", "nuclear", "military", "troops",
    "oil", "gas", "energy", "barrel", "opec",
    "sanctions", "embargo", "tariff", "ban",
    "rate", "fed", "inflation", "central bank",
    "putin", "biden", "iran", "israel", "china", 
    "taiwan", "russia", "quantum", "technology"
]

def istihbarat_operasyonu():
    print(f"\n[SCAN] {time.strftime('%H:%M:%S')} - Tarama başlatıldı...")
    ua = UserAgent()
    hedef_url = "http://feeds.bbci.co.uk/news/world/rss.xml"
    
    try:
        kamuflaj = {'User-Agent': ua.random}
        cevap = requests.get(hedef_url, headers=kamuflaj, timeout=15)
        if cevap.status_code == 200:
            nester = BeautifulSoup(cevap.text, "xml")
            haberler = nester.find_all("title")
            kritik_haberler = []
            
            for i in range(1, len(haberler)):
                haber_metni = haberler[i].text
                if any(kelime in haber_metni.lower() for kelime in KIRMIZI_BULTEN):
                    kritik_haberler.append(haber_metni)
            
            if kritik_haberler:
                rapor = "🔴 <b>GEOPULSE KRİTİK ANALİZ</b> 🔴\n\n"
                for haber in kritik_haberler[:5]:
                    rapor += f"⚠️ <i>{haber}</i>\n\n"
                siyah_terminale_bildir(rapor)
                print("SİSTEM: Anomali tespit edildi ve raporlandı!")
            else:
                print("SİSTEM: Olağanüstü bir durum yok.")
    except Exception as e:
        print(f"HATA: Tarama yapılamadı. {e}")

# --- ANA DÖNGÜ (SONSUZ NÖBET) ---
if __name__ == "__main__":
    print("--- GEOPULSE 4.0 OTONOM MOD AKTİF ---")
    print("Sistem her 60 dakikada bir dünyayı tarayacak. Kapatmak için CTRL+C yapın.")
    
    while True:
        istihbarat_operasyonu()
        
        # 20 Dakika (1200 saniye) bekleme süresi
        # Sert gerçek: Çok sık tararsan BBC seni banlar. 20-30 dk idealdir.
        time.sleep(3600)