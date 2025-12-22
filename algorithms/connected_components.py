import time
from collections import deque
from temelAlgoritma import temelAlgoritma

class BagliBilesenler(temelAlgoritma):
    def calistir(self):
        t1 = time.time()
        adj = {n['id']: [] for n in self.graf['nodes']}
        for e in self.graf['edges']:
            adj[e['source']].append(e['target'])
            adj[e['target']].append(e['source'])

        ziyaret = set()
        gruplar = []

        for node in self.graf['nodes']:
            nid = node['id']
            if nid not in ziyaret:
                grup = []
                q = deque([nid])
                ziyaret.add(nid)
                while q:
                    curr = q.popleft()
                    info = next(x for x in self.graf['nodes'] if x['id'] == curr)
                    grup.append(info['name'])
                    for k in adj[curr]:
                        if k not in ziyaret:
                            ziyaret.add(k)
                            q.append(k)
                gruplar.append(grup)

        return {"gruplar": gruplar, "adet": len(gruplar), "sure": self.sure_olc(t1)}
