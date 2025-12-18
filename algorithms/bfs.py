

from temelAlgoritma import TemelAlgoritma
from collections import deque
import time 

class AramaBFS(TemelAlgoritma):
    

    
    
    def calistir(self, baslangicID):
        
        baslangicSuresi = time.time() 
        
        baslangicNode = self.graf.nodes.get(baslangicID)
        
        if baslangicNode is None:
            return {
                "Sonuclar": None,
                "Mesaj": "Hata: Başlangıç düğümü grafikte yok.",
                "SureSaniye": 0.0
            } 

        ziyaretKaydi = set() 
        islemSirasi = deque([baslangicNode]) 
        bulunanDugumler = [] 

        
        while len(islemSirasi) > 0: 
            
            mevcutNode = islemSirasi.popleft()
            
            if mevcutNode.kNo not in ziyaretKaydi:
                
                ziyaretKaydi.add(mevcutNode.kNo)
                bulunanDugumler.append(mevcutNode.kNo)

                for kenar in mevcutNode.bagliKenarlar:
                    
                    komsusu = kenar.karsidakiDugumuVer(mevcutNode)

                    if komsusu.kNo not in ziyaretKaydi:
                        islemSirasi.append(komsusu)
                        
        gecenSure = self.sureHesapla(baslangicSuresi) 
        
        return {
            "Sonuclar": bulunanDugumler,
            "Mesaj": "Genişlik Öncelikli Arama başarıyla tamamlandı.",
            "SureSaniye": gecenSure
        }# __init__ metodu TemelAlgoritma sınıfı tarafından yönetilir.# Süreyi TemelAlgoritma üzerinden hesapla"""Genişlik Öncelikli Arama (BFS). TemelAlgoritma'dan kalıtım alır."""
    """Bir düğümden erişilebilen tüm kullanıcıları bulur (İşlevsel İster, 3.2)."""# BFS kuyruk mantığı
