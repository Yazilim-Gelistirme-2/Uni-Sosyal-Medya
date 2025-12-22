import time
from collections import deque
from temelAlgoritma import temelAlgoritma

class aramaBFS(temelAlgoritma):
    def calistir(self, baslangic_id):
        t1 = time.time()
        
        adj = {n['id']: [] for n in self.graf['nodes']}
        for e in self.graf['edges']:
            adj[e['source']].append(e['target'])
            adj[e['target']].append(e['source'])

        if baslangic_id not in adj:
            return {"mesaj": "ID bulunamadı", "sure": 0}

        ziyaret = {baslangic_id}
        kuyruk = deque([baslangic_id])
        siralamalar = []

        while kuyruk:
            curr_id = kuyruk.popleft()
            node_bilgi = next((n for n in self.graf['nodes'] if n['id'] == curr_id), None)
            if node_bilgi:
                siralamalar.append(f"{node_bilgi['name']} ({curr_id})")

            for komsu in adj[curr_id]:
                if komsu not in ziyaret:
                    ziyaret.add(komsu)
                    kuyruk.append(komsu)

        return {
            "sonuc": siralamalar,
            "adet": len(siralamalar),
            "sure": self.sure_olc(t1)
        }
