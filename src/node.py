
class Node:
    def __init__(self, id, ozelliklerMap=None):
        self.kullaniciNo = id 
        self.ozellikler = ozelliklerMap if ozelliklerMap is not None else {}
        self.bagliKenarlar = []

    def baglantiKaydet(self, kenar):
        self.bagliKenarlar.append(kenar)

    def baglantiSil(self, kenarObjesi):
        if kenarObjesi in self.bagliKenarlar:
            self.bagliKenarlar.remove(kenarObjesi)

    def nitelikDegistir(self, anahtar, yeniDeger):
        self.ozellikler[anahtar] = yeniDeger

    def raporBilgisi(self):
        
        metin = f"Kullanıcı No: {self.kullaniciNo}\n"
        for k, v in self.ozellikler.items():
            metin = metin + f"  - {k}: {v}\n"
        return metin
    
    def __repr__(self):
        return f"Kullanici(No={self.kullaniciNo})"
    
    #kullanıcı düğümünü temsil etmek için kullanılır.
    #kullanıcı düğüme tıklayınca düğüme gösterilecek olan bilgiyi temsil eder
