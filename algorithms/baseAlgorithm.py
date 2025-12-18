import math
import json
import csv
import os
from node import Node
from edge import Edge
class Graph:
    def __init__(self):
        self.nodes = {} 
        self.edges = []
        self.AGIRLIK_ANAHTARLARI = ['Aktiflik', 'Etkilesim', 'Baglanti']
    def _dinamikMaliyetHesapla(self, dugumI, dugumJ):
        pass
#Tüm düğümleri ve kenarları yöneten ana veri yapısı sınıfı.
