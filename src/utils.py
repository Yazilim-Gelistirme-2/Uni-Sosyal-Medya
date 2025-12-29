import math


def get_dynamic_weight(node_i, node_j):
    p_i = node_i.properties if hasattr(node_i, 'properties') else {}
    p_j = node_j.properties if hasattr(node_j, 'properties') else {}

    try:
        diff_sq_sum = (
                (float(p_i.get('aktiflik', 0)) - float(p_j.get('aktiflik', 0))) ** 2 +
                (float(p_i.get('etkilesim', 0)) - float(p_j.get('etkilesim', 0))) ** 2 +
                (float(p_i.get('baglanti_sayisi', 0)) - float(p_j.get('baglanti_sayisi', 0))) ** 2
        )
        denominator = 1 + math.sqrt(diff_sq_sum)
        weight = 1 / denominator

        return round(weight, 4)
    except (ValueError, TypeError, ZeroDivisionError):
        return 1.0