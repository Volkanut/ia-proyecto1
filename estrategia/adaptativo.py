# estrategia/adaptativo.py

from agentes.astar import astar
from agentes.bfs import bfs
from agentes.dfs import dfs

def agente_adaptativo(laberinto, inicio, meta):
    """
    Prueba todas las estrategias y elige la de menor costo real.
    """
    estrategias = [
        ("A*", astar),
        ("DFS", dfs),
        ("BFS", bfs),
        
        
    ]

    mejor_camino = None
    mejor_costo = float('inf')
    mejor_explorados = set()
    mejor_nombre = "Ninguna"

    for nombre, algoritmo in estrategias:
        print(f"🔍 Ejecutando {nombre}")
        camino, costo, explorados = algoritmo(laberinto, inicio, meta)
        if camino:
            print(f"✅ {nombre} encontró camino con costo {costo}")
            if costo < mejor_costo:
                mejor_camino = camino
                mejor_costo = costo
                mejor_explorados = explorados
                mejor_nombre = nombre
        else:
            print(f"❌ {nombre} no encontró camino")

    if mejor_camino:
        print(f"\n🏆 Estrategia elegida: {mejor_nombre} con costo {mejor_costo}")
    else:
        print("\n🚫 Ninguna estrategia funcionó.")

    return mejor_camino, mejor_costo, mejor_explorados, mejor_nombre
