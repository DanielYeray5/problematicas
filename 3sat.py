import math
import random

def poblacion_inicial(max_poblacion, num_vars):
    # Crear población inicial aleatoria
    poblacion = []
    for i in range(max_poblacion):
        gen = []
        for j in range(num_vars):
            if random.random() > 0.5:
                gen.append(1)
            else:
                gen.append(0)
        poblacion.append(gen[:])
    return poblacion


def adaptacion_3sat(gen, solucion):
    # Contar Cláusulas correctas
    n = 3
    cont = 0
    clausula_ok = True
    for i in range(len(gen)):
        n = n - 1
        if gen[i] != solucion[i]:
            clausula_ok = False
        if n == 0:
            if clausula_ok:
                cont = cont + 1
            n = 3
            clausula_ok = True
    return cont


def evalua_poblacion(poblacion, solucion):
    # Evalua todos los genes de la poblacion.
    adaptacion = []
    for i in range(len(poblacion)):
        adaptacion.append(adaptacion_3sat(poblacion[i], solucion))
    return adaptacion


def seleccion(poblacion, solucion):
    adaptacion = evalua_poblacion(poblacion, solucion)
    # Suma todas las puntuaciones
    total = sum(adaptacion)
    # Seleccionar dos elementos
    val1 = random.randint(0, total - 1)
    val2 = random.randint(0, total - 1)
    sum_sel = 0
    gen1 = None
    gen2 = None
    for i in range(len(adaptacion)):
        sum_sel += adaptacion[i]
        if gen1 is None and sum_sel > val1:
            gen1 = poblacion[i][:]
        if gen2 is None and sum_sel > val2:
            gen2 = poblacion[i][:]
        if gen1 is not None and gen2 is not None:
            break
    return gen1, gen2


def cruce(gen1, gen2):
    # Cruza dos genes y obtiene dos descendientes
    corte = random.randint(1, len(gen1) - 1)
    nuevo_gen1 = gen1[:corte] + gen2[corte:]
    nuevo_gen2 = gen2[:corte] + gen1[corte:]
    return nuevo_gen1, nuevo_gen2


def mutacion(prob, gen):
    # Muta el gen con una probabilidad Prob.
    if random.random() < prob:
        cromosoma = random.randint(0, len(gen) - 1)
        gen[cromosoma] = 1 - gen[cromosoma]
    return gen


def elimina_peores_genes(poblacion, solucion):
    # Elimina los dos peores genes.
    adaptacion = evalua_poblacion(poblacion, solucion)
    for _ in range(2):
        i = adaptacion.index(min(adaptacion))
        del poblacion[i]
        del adaptacion[i]


def mejor_gen(poblacion, solucion):
    # Devuelve el mejor gen de la población.
    adaptacion = evalua_poblacion(poblacion, solucion)
    return poblacion[adaptacion.index(max(adaptacion))]


def algoritmo_genetico():
    max_iter = 10
    max_poblacion = 50
    num_vars = 10
    fin = False
    solucion = poblacion_inicial(1, num_vars)[0]
    poblacion = poblacion_inicial(max_poblacion, num_vars)

    iteraciones = 0
    while not fin:
        iteraciones = iteraciones + 1
        for i in range(len(poblacion) // 2):
            gen1, gen2 = seleccion(poblacion, solucion)
            nuevo_gen1, nuevo_gen2 = cruce(gen1, gen2)
            nuevo_gen1 = mutacion(0.1, nuevo_gen1)
            nuevo_gen2 = mutacion(0.1, nuevo_gen2)
            poblacion.append(nuevo_gen1)
            poblacion.append(nuevo_gen2)
            elimina_peores_genes(poblacion, solucion)

        if iteraciones >= max_iter:
            fin = True

    print("Solución: " + str(solucion))
    mejor = mejor_gen(poblacion, solucion)
    return mejor, adaptacion_3sat(mejor, solucion)


if __name__ == "__main__":
    random.seed()
    mejor_gen_result = algoritmo_genetico()
    print("Mejor gen encontrado: " + str(mejor_gen_result[0]))
    print("Función de adaptación: " + str(mejor_gen_result[1]))