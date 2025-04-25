from agentes.bfs import bfs
from agentes.dfs import dfs
from agentes.astar import astar
from agentes.greedy import greedy
from estrategia.adaptativo import agente_adaptativo  # ✅ Nuevo import
from config import CELDAS
from core.generador import generar_laberinto
from visual.renderer import iniciar_visualizacion

def imprimir_camino(mapa, camino, explorados=None):
    for i, fila in enumerate(mapa):
        fila_str = ""
        for j, celda in enumerate(fila):
            pos = (i, j)
            if pos in camino and celda not in ['S', 'X', 'G', 'R']:
                fila_str += '✓ '
            elif explorados and pos in explorados and pos not in camino:
                fila_str += '+ '
            else:
                fila_str += celda + ' '
        print(fila_str)
    print()

def imprimir_detalle_camino(camino, laberinto):
    print("========Detalle del camino========")
    costo_total = 0
    for i in range(len(camino) - 1):
        actual = camino[i]
        siguiente = camino[i + 1]
        tipo = laberinto[siguiente[0]][siguiente[1]]
        nombre = CELDAS.get(tipo, {}).get("nombre", "desconocido")
        costo = CELDAS.get(tipo, {}).get("costo", 1)
        costo_total += costo
        print(f"Paso {i+1}: {actual} → {siguiente} → {tipo} ({nombre}) → costo: {costo} → acumulado: {costo_total}")

if __name__ == "__main__":
    laberinto, inicio_pos, meta_pos = generar_laberinto(
        filas=6,
        columnas=10,
        num_muros=15,
        num_fantasmas_rojos=2,
        num_fantasmas_azules=3
    )

    print("=== LABERINTO GENERADO ===")
    for fila in laberinto:
        print(" ".join(fila))
    print()

    print("=== BFS ===")
    camino_bfs, costo_bfs, explorados_bfs = bfs(laberinto, inicio_pos, meta_pos)
    if camino_bfs:
        imprimir_camino(laberinto, camino_bfs, explorados_bfs)
        print("Camino BFS:", camino_bfs)
        print("Costo total BFS:", costo_bfs)
        imprimir_detalle_camino(camino_bfs, laberinto)
    else:
        print("No se encontró camino con BFS.")

    print("=== DFS ===")
    camino_dfs, costo_dfs, explorados_dfs = dfs(laberinto, inicio_pos, meta_pos)
    if camino_dfs:
        imprimir_camino(laberinto, camino_dfs, explorados_dfs)
        print("Camino DFS:", camino_dfs)
        print("Costo total DFS:", costo_dfs)
        imprimir_detalle_camino(camino_dfs, laberinto)
    else:
        print("No se encontró camino con DFS.")

    print("=== A* ===")
    camino_astar, costo_astar, explorados_astar = astar(laberinto, inicio_pos, meta_pos)
    if camino_astar:
        imprimir_camino(laberinto, camino_astar, explorados_astar)
        print("Camino A*:", camino_astar)
        print("Costo total A*:", costo_astar)
        imprimir_detalle_camino(camino_astar, laberinto)
    else:
        print("No se encontró camino con A*.")

    print("=== Agente adaptativo ===")
    camino_adap, costo_adap, explorados_adap, estrategia_usada = agente_adaptativo(laberinto, inicio_pos, meta_pos)
    if camino_adap:
        imprimir_camino(laberinto, camino_adap, explorados_adap)
        print(f"Estrategia usada: {estrategia_usada}")
        print("Camino Adaptativo:", camino_adap)
        print("Costo total Adaptativo:", costo_adap)
        imprimir_detalle_camino(camino_adap, laberinto)
    else:
        print("No se encontró camino con ninguna estrategia.")
    print("=== GREEDY ===")
    camino_greedy, costo_greedy, explorados_greedy = greedy(laberinto, inicio_pos, meta_pos)
    if camino_greedy:
        imprimir_camino(laberinto, camino_greedy, explorados_greedy)
        print("Camino GREEDY:", camino_greedy)
        print("Costo total GREEDY:", costo_greedy)
        imprimir_detalle_camino(camino_greedy, laberinto)
    else:
        print("No se encontró camino con GREEDY.")



    iniciar_visualizacion(laberinto, inicio_pos, meta_pos)
