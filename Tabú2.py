import random
import math

def distancia(coord1, coord2):
    """Calcula la distancia euclidiana entre dos coordenadas."""
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    return math.sqrt((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2)

def evalua_ruta(ruta, coord):
    """Evalúa el costo total de una ruta."""
    total = 0
    for i in range(len(ruta) - 1):
        total += distancia(coord[ruta[i]], coord[ruta[i + 1]])
    total += distancia(coord[ruta[-1]], coord[ruta[0]])  # Regreso al inicio
    return total

def peso_ruta(ruta, pedidos):
    """Calcula el peso total de una ruta."""
    return sum(pedidos[cliente] for cliente in ruta)

def generar_vecinos(ruta, coord, pedidos, max_carga):
    """Genera vecinos válidos intercambiando dos clientes en la ruta."""
    vecinos = []
    for i in range(len(ruta)):
        for j in range(i + 1, len(ruta)):
            vecino = ruta[:]
            vecino[i], vecino[j] = vecino[j], vecino[i]  # Intercambiar clientes
            if peso_ruta(vecino, pedidos) <= max_carga:
                vecinos.append(vecino)
    return vecinos

def busqueda_tabu(coord, pedidos, almacen, max_carga, max_iter=100, tamaño_tabu=10):
    """Búsqueda Tabú para resolver el problema de ruteo de vehículos."""
    # Crear ruta inicial aleatoria
    ruta_actual = list(coord.keys())
    random.shuffle(ruta_actual)
    mejor_ruta = ruta_actual[:]
    mejor_costo = evalua_ruta(mejor_ruta, coord)

    lista_tabu = []

    for _ in range(max_iter):
        vecinos = generar_vecinos(ruta_actual, coord, pedidos, max_carga)
        vecinos = [v for v in vecinos if v not in lista_tabu]

        if not vecinos:
            break

        # Evaluar vecinos y seleccionar el mejor
        vecino_costos = [(v, evalua_ruta(v, coord)) for v in vecinos]
        vecino_costos.sort(key=lambda x: x[1])  # Ordenar por costo
        mejor_vecino, mejor_vecino_costo = vecino_costos[0]

        # Actualizar la lista Tabú
        lista_tabu.append(mejor_vecino)
        if len(lista_tabu) > tamaño_tabu:
            lista_tabu.pop(0)

        # Actualizar la ruta actual
        ruta_actual = mejor_vecino

        # Actualizar la mejor solución encontrada
        if mejor_vecino_costo < mejor_costo:
            mejor_ruta = mejor_vecino
            mejor_costo = mejor_vecino_costo

    return mejor_ruta, mejor_costo

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

    mejor_ruta, mejor_costo = busqueda_tabu(coord, pedidos, almacen, max_carga)
    print("Mejor ruta:", mejor_ruta)
    print("Costo total:", mejor_costo)