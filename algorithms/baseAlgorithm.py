import time

class temelAlgoritma:
    def __init__(self, veri):
        self.graf = veri

    def calistir(self, *args, **kwargs):
        raise NotImplementedError("Bu metod alt sınıflarda tanımlanmalı.")

    def sure_olc(self, start):
        return round(time.time() - start, 5)
