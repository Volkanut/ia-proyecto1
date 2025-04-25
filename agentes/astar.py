import heapq
from core.estado import Estado
from core.operador import generar_sucesores
from core.prueba_meta import es_meta
from core.costo import costo

def heuristica(pos, meta):
    """Calcula la distancia Manhattan entre dos posiciones"""
    return abs(pos[0] - meta[0]) + abs(pos[1] - meta[1])

def astar(laberinto, inicio_pos, meta_pos):
    estado_inicial = Estado(posicion=inicio_pos, g=0, h=heuristica(inicio_pos, meta_pos))
    frontera = [(estado_inicial.f(), estado_inicial)]
    visitados = {}
    explorados = set()

    while frontera:
        _, actual = heapq.heappop(frontera)
        explorados.add(actual.pos)

        if es_meta(actual, meta_pos):
            return actual.reconstruir_camino(), actual.g, explorados

        sucesores = generar_sucesores(actual, laberinto)

        for sucesor in sucesores:
            nuevo_costo = actual.g + costo(actual.pos, sucesor.pos, laberinto)

            if sucesor.pos not in visitados or nuevo_costo < visitados[sucesor.pos]:
                visitados[sucesor.pos] = nuevo_costo
                h = heuristica(sucesor.pos, meta_pos)
                nuevo_estado = Estado(posicion=sucesor.pos, padre=actual, g=nuevo_costo, h=h)
                heapq.heappush(frontera, (nuevo_estado.f(), nuevo_estado))

    return None, float('inf'), explorados
