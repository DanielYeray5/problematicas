from Arbol import Nodo

def buscar_solucion_DSF_rec(nodo_inicial, solucion, visitados):
    visitados.append(nodo_inicial.get_datos())
    if nodo_inicial.get_datos() == solucion:
        return nodo_inicial
    else:
        # Expandir los nodos sucesores (hijos)
        dato_nodo = nodo_inicial.get_datos()
        hijo = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
        hijo_izquierdo = Nodo(hijo)
        hijo = [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]
        hijo_central = Nodo(hijo)
        hijo = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]
        hijo_derecho = Nodo(hijo)
        nodo_inicial.set_hijos([hijo_izquierdo, hijo_central, hijo_derecho])
        
        for nodo_hijo in nodo_inicial.get_hijos():
            if nodo_hijo.get_datos() not in visitados:
                # Llamada recursiva
                S = buscar_solucion_DSF_rec(nodo_hijo, solucion, visitados)
                if S is not None:
                    return S
        return None

if __name__ == "__main__":
    estado_inicial = [4, 2, 3, 1]
    solucion = [1, 2, 3, 4]
    nodo_solucion = None
    visitados = []
    nodo_inicial = Nodo(estado_inicial)
    nodo = buscar_solucion_DSF_rec(nodo_inicial, solucion, visitados)
    
    # mostrar el resultado
    resultado = []
    while nodo.get_padre() is not None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)