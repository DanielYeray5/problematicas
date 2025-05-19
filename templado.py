import math
import random

def distancia(coord1, coord2):
    lat1 = coord1[0]
    lon1 = coord1[1]
    lat2 = coord2[0]
    lon2 = coord2[1]
    
    return math.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)

def eval_ruta(ruta):
    total = 0
    for i in range(0, len(ruta) - 1):
        ciudad1 = ruta[i]
        ciudad2 = ruta[i + 1]
        total += distancia(coord[ciudad1], coord[ciudad2])
    return total

def simulated_annealing(ruta):
    T = 20
    T_MIN = 0
    V_enfiamiento = 100
    
    while T > T_MIN:
        distancia_actual = eval_ruta(ruta)
        for _ in range(1, V_enfiamiento):
            # intercambio de dos ciudades aleatoriamente
            i = random.randint(0, len(ruta) - 1)
            j = random.randint(0, len(ruta) - 1)
            ruta_tmp = ruta[:]
            ciudad_tmp = ruta_tmp[i]
            ruta_tmp[i] = ruta_tmp[j]
            ruta_tmp[j] = ciudad_tmp
            nueva_distancia = eval_ruta(ruta_tmp)
            delta = nueva_distancia - distancia_actual
            if nueva_distancia < distancia_actual:
                ruta = ruta_tmp[:]
                break
        # Enfriar a T linealmente
        T = T - 0.005
    return ruta

if __name__ == "__main__":
    coord = {
        'Jiloyork': (19.916012, -99.580580),
        'Toluca': (19.289165, -99.655697),
        'Atlacomulco': (19.799520, -99.873844),
        'Guadalajara': (20.677754472859146, -103.34625354877137),
        'Monterrey': (25.69161110159454, -100.321838480256),
        'QuintanaRoo': (21.163111924844458, -86.80231502121464),
        'Michohacan': (19.701400113725654, -101.20829680213464),
        'Aguascalientes': (21.87641043660486, -102.26438663286967),
        'CDMX': (19.432713075976878, -99.13318344772986),
        'QRO': (20.59719437542255, -100.38667040246602)
    }
    
    ruta = []
    for ciudad in coord:
        ruta.append(ciudad)
    random.shuffle(ruta)
    print(ruta)
    print("Distancia total: " + str(eval_ruta(ruta)))