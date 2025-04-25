# Búsqueda por profundidad

from collections import deque
from core.estado import Estado
from core.operador import generar_sucesores
from core.prueba_meta import es_meta
from core.costo import costo  

def dfs(laberinto, inicio_pos, meta_pos):
    """
    Algoritmo de búsqueda por profundidad (DFS).

    
    """
    estado_inicial = Estado(posicion=inicio_pos)
    frontera = deque([estado_inicial])
    visitados = set()
    visitados.add(inicio_pos)

    while frontera:
        actual = frontera.pop()  # DFS usa LIFO

        if es_meta(actual, meta_pos):
            camino = actual.reconstruir_camino()
            costo_total = sum(
                costo(camino[i], camino[i+1], laberinto) for i in range(len(camino) - 1)
            )
            return camino, costo_total, visitados

        sucesores = generar_sucesores(actual, laberinto)

        for sucesor in sucesores:
            if sucesor.pos not in visitados:
                frontera.append(sucesor)
                visitados.add(sucesor.pos)

    return None, 0, set() # No se encontró camino
