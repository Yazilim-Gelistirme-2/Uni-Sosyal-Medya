import time
from collections import deque
from algorithms.baseAlgorithm import temelAlgoritma


class aramaBFS(temelAlgoritma):
    def calistir(self, baslangic_id):
        t1 = time.time()

        if baslangic_id not in self.graph.nodes:
            return {"mesaj": "ID bulunamadı", "sure": 0}

        ziyaret = set()
        kuyruk = deque([baslangic_id])
        siralamalar = []

        ziyaret.add(baslangic_id)

        while kuyruk:
            curr_id = kuyruk.popleft()
            curr_node = self.graph.nodes[curr_id]

            siralamalar.append(f"{curr_node.name} ({curr_id})")

            for komsu_id in curr_node.neighbors:
                if komsu_id not in ziyaret:
                    ziyaret.add(komsu_id)
                    kuyruk.append(komsu_id)

        return {
            "sonuc": siralamalar,
            "adet": len(siralamalar),
            "sure": self.sure_olc(t1)
        }
