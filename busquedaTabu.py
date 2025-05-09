import random
import math

def distancia(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    return math.sqrt((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2)

def evalua_ruta(ruta, coord):
    total = 0
    for i in range(len(ruta) - 1):
        total += distancia(coord[ruta[i]], coord[ruta[i + 1]])
    total += distancia(coord[ruta[-1]], coord[ruta[0]])  # Regreso al inicio
    return total

def busqueda_tabu(coord, max_iteraciones=100, tamano_tabu=10):
    # Crear ruta inicial aleatoria
    ruta_actual = list(coord.keys())
    random.shuffle(ruta_actual)
    mejor_ruta = ruta_actual[:]
    mejor_costo = evalua_ruta(mejor_ruta, coord)

    lista_tabu = []

    for _ in range(max_iteraciones):
        vecinos = []
        for i in range(len(ruta_actual)):
            for j in range(i + 1, len(ruta_actual)):
                vecino = ruta_actual[:]
                vecino[i], vecino[j] = vecino[j], vecino[i]  # Intercambiar ciudades
                if vecino not in lista_tabu:
                    vecinos.append((vecino, evalua_ruta(vecino, coord)))

        if not vecinos:
            break

        # Seleccionar el mejor vecino
        vecinos.sort(key=lambda x: x[1])  # Ordenar por costo
        mejor_vecino, costo_vecino = vecinos[0]

        # Actualizar la lista Tabú
        lista_tabu.append(mejor_vecino)
        if len(lista_tabu) > tamano_tabu:
            lista_tabu.pop(0)

        # Actualizar la ruta actual
        ruta_actual = mejor_vecino

        # Actualizar la mejor solución encontrada
        if costo_vecino < mejor_costo:
            mejor_ruta = mejor_vecino
            mejor_costo = costo_vecino

    return mejor_ruta, mejor_costo

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

    mejor_ruta, mejor_costo = busqueda_tabu(coord)
    print("Mejor ruta:", mejor_ruta)
    print("Costo total:", mejor_costo)