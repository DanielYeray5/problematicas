# Archivo VRP

import math
from operator import itemgetter

def distancia(coord1, coord2):
    """Calcula la distancia euclidiana entre dos coordenadas."""
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    return math.sqrt((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2)

def en_ruta(rutas, cliente):
    """Verifica si un cliente ya está en alguna ruta."""
    for ruta in rutas:
        if cliente in ruta:
            return ruta
    return None

def peso_ruta(ruta):
    """Calcula el peso total de una ruta."""
    return sum(pedidos[cliente] for cliente in ruta)

def vrp_voraz():
    """Algoritmo voraz para resolver el problema de ruteo de vehículos."""
    # Calcular ahorros
    ahorros = {}
    for c1 in coord:
        for c2 in coord:
            if c1 != c2 and (c2, c1) not in ahorros:
                d_c1_c2 = distancia(coord[c1], coord[c2])
                d_c1_almacen = distancia(coord[c1], almacen)
                d_c2_almacen = distancia(coord[c2], almacen)
                ahorros[(c1, c2)] = d_c1_almacen + d_c2_almacen - d_c1_c2

    # Ordenar ahorros en orden descendente
    ahorros = sorted(ahorros.items(), key=itemgetter(1), reverse=True)

    rutas = []
    for (c1, c2), _ in ahorros:
        ruta_c1 = en_ruta(rutas, c1)
        ruta_c2 = en_ruta(rutas, c2)

        if ruta_c1 is None and ruta_c2 is None:
            # Ninguno de los clientes tiene ruta, crear una nueva
            if peso_ruta([c1, c2]) <= max_carga:
                rutas.append([c1, c2])
        elif ruta_c1 is not None and ruta_c2 is None:
            # Cliente 1 tiene ruta, agregar cliente 2
            if ruta_c1[0] == c1 and peso_ruta(ruta_c1 + [c2]) <= max_carga:
                ruta_c1.insert(0, c2)
            elif ruta_c1[-1] == c1 and peso_ruta(ruta_c1 + [c2]) <= max_carga:
                ruta_c1.append(c2)
        elif ruta_c1 is None and ruta_c2 is not None:
            # Cliente 2 tiene ruta, agregar cliente 1
            if ruta_c2[0] == c2 and peso_ruta(ruta_c2 + [c1]) <= max_carga:
                ruta_c2.insert(0, c1)
            elif ruta_c2[-1] == c2 and peso_ruta(ruta_c2 + [c1]) <= max_carga:
                ruta_c2.append(c1)
        elif ruta_c1 is not None and ruta_c2 is not None and ruta_c1 != ruta_c2:
            # Ambos clientes tienen rutas diferentes, intentar unirlas
            if ruta_c1[-1] == c1 and ruta_c2[0] == c2 and peso_ruta(ruta_c1 + ruta_c2) <= max_carga:
                ruta_c1.extend(ruta_c2)
                rutas.remove(ruta_c2)
            elif ruta_c1[0] == c1 and ruta_c2[-1] == c2 and peso_ruta(ruta_c2 + ruta_c1) <= max_carga:
                ruta_c2.extend(ruta_c1)
                rutas.remove(ruta_c1)

    return rutas

if __name__ == "__main__":
    coord = {
        'EDO.MEX': (19.293640310142514, -99.65370965026779),
        'QRO': (20.59353748944623, -100.39005130417503),
        'CDMX': (19.432676340933284, -99.133319394754),
        'SLP': (22.152600894282806, -100.97646886531842),
        'MTY': (25.6752139374842, -100.28760729053225),
        'PUE': (19.079809264771754, -98.31909530279367),
        'GDL': (20.677234735648103, -103.34704837718459),
        'MICH': (19.70259469395305, -101.19233996186851),
        'SON': (29.07524505818489, -110.95966769041577)
    }
    
    pedidos = {
        'EDO.MEX': 10,
        'QRO': 13,
        'CDMX': 7,
        'SLP': 11,
        'MTY': 15,
        'PUE': 8,
        'GDL': 6,
        'MICH': 7,
        'SON': 8
    }
    
    almacen = (19.432676340933284, -99.133319394754)
    max_carga = 40
    
    rutas = vrp_voraz()
    for ruta in rutas:
        print(ruta)