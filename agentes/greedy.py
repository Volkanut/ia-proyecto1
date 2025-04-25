import heapq
from core.estado import Estado
from core.operador import generar_sucesores
from core.prueba_meta import es_meta
from core.costo import costo

def heuristica(pos, meta):
    """Distancia Manhattan como heurística"""
    return abs(pos[0] - meta[0]) + abs(pos[1] - meta[1])

def greedy(laberinto, inicio_pos, meta_pos):
    """
    Búsqueda Avara (Greedy Best-First Search).
    Usa únicamente la heurística h(n) para elegir los caminos.

    Returns:
        camino: lista de posiciones hasta la meta
        costo_total: suma de costos reales del camino
        explorados: conjunto de nodos visitados
    """
    estado_inicial = Estado(posicion=inicio_pos, h=heuristica(inicio_pos, meta_pos))
    frontera = [(estado_inicial.h, estado_inicial)]
    visitados = set()
    explorados = set()

    while frontera:
        _, actual = heapq.heappop(frontera)
        explorados.add(actual.pos)

        if es_meta(actual, meta_pos):
            camino = actual.reconstruir_camino()
            try:
                costo_total = sum(
                    costo(camino[i], camino[i + 1], laberinto)
                    for i in range(len(camino) - 1)
                )
            except Exception as e:
                print("⚠️ Error al calcular costo del camino en GREEDY:", camino)
                print("❌ Detalle:", e)
                costo_total = float('inf')
            return camino, costo_total, explorados

        for sucesor in generar_sucesores(actual, laberinto):
            if sucesor.pos not in visitados:
                visitados.add(sucesor.pos)
                h = heuristica(sucesor.pos, meta_pos)
                nuevo_estado = Estado(posicion=sucesor.pos, padre=actual, h=h)
                heapq.heappush(frontera, (nuevo_estado.h, nuevo_estado))

    return None, float('inf'), explorados
