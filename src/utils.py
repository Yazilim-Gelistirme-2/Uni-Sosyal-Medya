import math

def get_dynamic_weight(node_i, node_j):
    """
    Döküman 4.3'teki Dinamik Ağırlık formülünü hesaplar.
    Ahmet(1)-Mehmet(3) arası: 0.0328
    Ahmet(1)-Elif(2) arası: 0.0212
    """
    p_i = node_i.properties if hasattr(node_i, 'properties') else {}
    p_j = node_j.properties if hasattr(node_j, 'properties') else {}
    
    try:
        # Formül: (P1i - P1j)^2 + (P2i - P2j)^2 + (P3i - P3j)^2 
        diff_sq_sum = (
            (float(p_i.get('aktiflik', 0)) - float(p_j.get('aktiflik', 0)))**2 +
            (float(p_i.get('etkilesim', 0)) - float(p_j.get('etkilesim', 0)))**2 +
            (float(p_i.get('baglanti_sayisi', 0)) - float(p_j.get('baglanti_sayisi', 0)))**2
        )
        
        # Payda hesabı (Uzaklık arttıkça büyür) [cite: 59, 62]
        denominator = 1 + math.sqrt(diff_sq_sum)
        
        # Final Ağırlık/Maliyet: 1 / Payda 
        # Bu değer benzerlik arttıkça yükselir [cite: 61]
        weight = 1 / denominator
        
        return round(weight, 4)
    except (ValueError, TypeError, ZeroDivisionError):
        return 1.0
