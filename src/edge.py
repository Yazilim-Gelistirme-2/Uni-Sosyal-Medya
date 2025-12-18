# İlişki (danışmanlık, ortak proje vb.)

class Edge:
    
    def __init__(self, dugumKaynak, dugumHedef, maliyetDegeri=1.0):
        
        self.kaynak = dugumKaynak
        self.hedef = dugumHedef
        
        self.maliyet = maliyetDegeri 

    def karsidakiDugumuVer(self, mevcutDugum):
        
        if mevcutDugum is self.kaynak:
            return self.hedef
        else:
            return self.kaynak

    def __repr__(self):
       
        return f"Baglanti({self.kaynak.kNo}-{self.hedef.kNo}, Maliyet={self.maliyet:.4f})"
    """iki kullanıcı arasindaki bağlantının veya kenarın tutulmasını sağlar.
    karsidakiDugumuVer fonksiyonuyla verilen düğümün karşısında olanın döndürülmesini sağlar."""
