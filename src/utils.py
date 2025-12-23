import math


def get_dynamic_weight(node_i, node_j):
    """
    İki düğüm arasındaki ağırlığı belgedeki formüle göre hesaplar:
    1 + sqrt((Aktiflik_i - Aktiflik_j)^2 + (Etkilesim_i - Etkilesim_j)^2 + (Baglanti_i - Baglanti_j)^2)
    """
    # Özellikler yüklenmemişse varsayılan 1.0 döndür
    if not hasattr(node_i, 'properties') or not hasattr(node_j, 'properties'):
        return 1.0

    p1 = node_i.properties
    p2 = node_j.properties

    # Formül: Madde 4.3
    diff_aktiflik = (p1.get("aktiflik", 0) - p2.get("aktiflik", 0)) ** 2
    diff_etkilesim = (p1.get("etkilesim", 0) - p2.get("etkilesim", 0)) ** 2
    diff_baglanti = (p1.get("baglanti_sayisi", 0) - p2.get("baglanti_sayisi", 0)) ** 2

    return 1 + math.sqrt(diff_aktiflik + diff_etkilesim + diff_baglanti)