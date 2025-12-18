
from temelAlgoritma import TemelAlgoritma
import heapq
import time

class Dijkstra(TemelAlgoritma):

    def calistir(self, baslangicID, hedefID):
        
        baslangicSuresi = time.time()
        
        if baslangicID not in self.graf.nodes or hedefID not in self.graf.nodes:
             
             return {"Sonuclar": [], "Mesafe": float('inf'), "Mesaj": "Hata: Düğüm grafikte mevcut değil.", "SureSaniye": 0.0}
        
        
        mesafeKaydi = {k_id: float('inf') for k_id in self.graf.nodes}
        mesafeKaydi[baslangicID] = 0
        hangiOnceki = {k_id: None for k_id in self.graf.nodes}
        siraliIslem = [(0, baslangicID)] 

        while siraliIslem:
            
            mevcutMesafe, mevcutID = heapq.heappop(siraliIslem)
            
            if mevcutMesafe > mesafeKaydi[mevcutID]: continue
            if mevcutID == hedefID: break

            for kenar in self.graf.nodes[mevcutID].bagliKenarlar:
                komsusu = kenar.karsidakiDugumuVer(self.graf.nodes[mevcutID])
                komsuID = komsusu.kNo
                maliyet = kenar.maliyet

                yeniMesafe = mevcutMesafe + maliyet
                
                if yeniMesafe < mesafeKaydi[komsuID]:
                    mesafeKaydi[komsuID] = yeniMesafe
                    hangiOnceki[komsuID] = mevcutID
                    heapq.heappush(siraliIslem, (yeniMesafe, komsuID))
        
        yolListesi = []
        mevcut = hedefID
        finalMesafe = mesafeKaydi[hedefID]
        
        if finalMesafe == float('inf'):
            gecenSure = self.sureHesapla(baslangicSuresi)
            return {"Sonuclar": [], "Mesafe": float('inf'), "Mesaj": "Başlangıçtan hedefe yol bulunamadı.", "SureSaniye": gecenSure}

        while mevcut is not None:
            yolListesi.append(mevcut)
            mevcut = hangiOnceki[mevcut]

        yolListesi.reverse()
        gecenSure = self.sureHesapla(baslangicSuresi)

        return {
            "Sonuclar": yolListesi,
            "Mesafe": finalMesafe,
            "Mesaj": "En kısa yol bulundu.",
            "SureSaniye": gecenSure
        }
