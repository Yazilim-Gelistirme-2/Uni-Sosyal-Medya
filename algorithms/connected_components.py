
from temelAlgoritma import TemelAlgoritma 
from collections import deque
import time

class BagliBilesenler(TemelAlgoritma):

    def calistir(self):
        baslangicSuresi = time.time() 
        
        ziyaretKaydi = set()
        toplulukListesi = [] 

        for kID, dugum in self.graf.nodes.items():
            
            if kID not in ziyaretKaydi:
                
                mevcutTopluluk = []
                islemSirasi = deque([dugum]) 
                
                ziyaretKaydi.add(kID)
                mevcutTopluluk.append(kID)

                while len(islemSirasi) > 0: 
                    mevcut = islemSirasi.popleft()
                    
                    for kenar in mevcut.bagliKenarlar:
                        komsusu = kenar.karsidakiDugumuVer(mevcut)
                        komsuID = komsusu.kNo

                        if komsuID not in ziyaretKaydi:
                            ziyaretKaydi.add(komsuID)
                            mevcutTopluluk.append(komsuID)
                            islemSirasi.append(komsusu)
                            
                toplulukListesi.append(mevcutTopluluk)
                
        gecenSure = self.sureHesapla(baslangicSuresi) 
        
        return {
            "Sonuclar": toplulukListesi,
            "Mesaj": f"Toplam {len(toplulukListesi)} farklı topluluk (bileşen) bulundu.",
            "SureSaniye": gecenSure
        }
