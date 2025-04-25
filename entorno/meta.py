# Posición/meta dinámica
# entorno/meta.py

def mover_meta(laberinto, meta_actual):
    import random

    filas = len(laberinto)
    columnas = len(laberinto[0])

    posibles = [(i, j) for i in range(filas) for j in range(columnas)
                if laberinto[i][j] == '.' and (i, j) != meta_actual]

    if posibles:
        nueva_meta = random.choice(posibles)

        # Limpiar antigua meta
        x_ant, y_ant = meta_actual
        laberinto[x_ant][y_ant] = '.'

        # Colocar nueva
        x_nueva, y_nueva = nueva_meta
        laberinto[x_nueva][y_nueva] = 'X'

        return nueva_meta

    return meta_actual
