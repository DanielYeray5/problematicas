# Vuelos con búsqueda con la profundidad iterativa
from Arbol import Nodo

def DFS_prof_iter(nodo, solucion):
    for limite in range(0, 100):
        visitados = []  # Inicializar visitados en cada iteración
        sol = buscar_solucion_DFS_rec(nodo, solucion, visitados, limite)
        if sol is not None:
            return sol
    return None

def buscar_solucion_DFS_rec(nodo, solucion, visitados, limite):
    if limite >= 0:
        visitados.append(nodo)
        if nodo.get_datos() == solucion:
            return nodo
        else:
            # Expandir los nodos hijos (ciudades con conexión)
            dato_nodo = nodo.get_datos()
            lista_hijos = []
            if dato_nodo in conexiones:  # Verificar si el nodo tiene conexiones
                for un_hijo in conexiones[dato_nodo]:
                    hijo = Nodo(un_hijo)
                    if not hijo.en_lista(visitados):
                        lista_hijos.append(hijo)
            nodo.set_hijos(lista_hijos)
            for nodo_hijo in nodo.get_hijos():  # Corregido el método
                # Llamada recursiva
                sol = buscar_solucion_DFS_rec(nodo_hijo, solucion, visitados, limite - 1)
                if sol is not None:
                    return sol
    return None

if __name__ == '__main__':
    conexiones = {
        'EDO.MÉX': ['QRO', 'SLP', 'SONORA'],
        'PUEBLA': ['HIDALGO', 'SLP'],
        'CDMX': ['MICHOACAN'],
        'MICHOACAN': ['SONORA'],
        'SLP': ['QRO', 'PUEBLA', 'EDO.MÉX', 'SONORA', 'GUADALAJARA'],
        'QRO': ['EDO.MÉX', 'SLP'],
        'HIDALGO': ['PUEBLA', 'GUADALAJARA', 'SONORA'],
        'MONTERREY': ['HIDALGO', 'SLP'],
        'SONORA': ['MONTERREY', 'HIDALGO', 'SLP', 'EDO.MÉX', 'MICHOACAN']
    }
    
    estado_inicial = 'EDO.MÉX'
    solucion = 'HIDALGO'
    nodo_inicial = Nodo(estado_inicial)
    nodo = DFS_prof_iter(nodo_inicial, solucion)

    # Mostrar el resultado
    if nodo is not None:
        resultado = []
        while nodo.get_padre() is not None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        resultado.append(estado_inicial)
        resultado.reverse()
        print(resultado)
    else:
        print('No hay solución')