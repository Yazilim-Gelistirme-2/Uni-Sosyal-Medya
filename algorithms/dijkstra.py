import heapq
import time
from algorithms.baseAlgorithm import temelAlgoritma
from src.utils import get_dynamic_weight


class dijkstra(temelAlgoritma):
    def calistir(self, baslangic_id, hedef_id):
        t1 = time.time()
        if baslangic_id not in self.graph.nodes or hedef_id not in self.graph.nodes:
            return {"mesaj": "ID bulunamadı", "sure": 0}

        mesafeler = {node_id: float('inf') for node_id in self.graph.nodes}
        mesafeler[baslangic_id] = 0
        onceki = {node_id: None for node_id in self.graph.nodes}
        pq = [(0, baslangic_id)]

        while pq:
            mevcut_mesafe, u = heapq.heappop(pq)
            if mevcut_mesafe > mesafeler[u]: continue
            if u == hedef_id: break

            for v in self.graph.nodes[u].neighbors:
                # DİNAMİK AĞIRLIK KULLANIMI
                agirlik = get_dynamic_weight(self.graph.nodes[u], self.graph.nodes[v])
                yeni_mesafe = mesafeler[u] + agirlik

                if yeni_mesafe < mesafeler[v]:
                    mesafeler[v] = yeni_mesafe
                    onceki[v] = u
                    heapq.heappush(pq, (yeni_mesafe, v))

        # Yol yoksa
        if mesafeler[hedef_id] == float('inf'):
            return {"mesaj": "Yol bulunamadı", "sure": self.sure_olc(t1)}

        # En kısa yolun geri çıkarılması
        yol = []
        curr = hedef_id
        while curr is not None:
            node = self.graph.nodes[curr]
            yol.append(f"{node.name} ({curr})")
            curr = onceki[curr]

        yol.reverse()

        return {
            "en_kisa_yol": yol,
            "mesafe": mesafeler[hedef_id],
            "sure": self.sure_olc(t1)
        }
