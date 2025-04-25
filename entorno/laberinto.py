# Generar y actualizar mapa
# Código para el archivo entorno/laberinto.py

import random

def actualizar_paredes(laberinto, pacman_pos, meta_pos):
    """
    Añade o elimina una pared aleatoriamente en el laberinto.
    No modifica la posición del agente, la meta ni fantasmas.
    """
    filas = len(laberinto)
    columnas = len(laberinto[0])
    candidatos = []

    for i in range(filas):
        for j in range(columnas):
            if (i, j) in [pacman_pos, meta_pos]:
                continue
            celda = laberinto[i][j]
            if celda == '.':
                candidatos.append((i, j, '#'))  # añadir pared
            elif celda == '#':
                candidatos.append((i, j, '.'))  # quitar pared

    if candidatos:
        i, j, nuevo = random.choice(candidatos)
        laberinto[i][j] = nuevo


def mover_fantasmas(laberinto, pacman_pos, meta_pos):
    """
    Mueve fantasmas rojos (R) y azules (G) a celdas vacías aleatorias.
    No deben moverse a la celda del Pac-Man ni de la meta.
    """
    filas = len(laberinto)
    columnas = len(laberinto[0])
    nuevas_posiciones = []

    for tipo in ['R', 'G']:
        posiciones = [(i, j) for i in range(filas) for j in range(columnas) if laberinto[i][j] == tipo]
        for i, j in posiciones:
            libres = [(x, y) for x in range(filas) for y in range(columnas)
                      if laberinto[x][y] == '.' and (x, y) != pacman_pos and (x, y) != meta_pos]
            if libres:
                x_nuevo, y_nuevo = random.choice(libres)
                laberinto[i][j] = '.'           # Vacía la anterior
                laberinto[x_nuevo][y_nuevo] = tipo  # Nuevo lugar
