# Acciones posibles desde un estado
from core.estado import Estado
from core.costo import costo
from config import CELDAS

MOVIMIENTOS = [(-1, 0), (0, 1), (1, 0), (0, -1)] #sentido de reloj

def generar_sucesores(estado_actual, laberinto, meta=None, usar_heuristica=False):
    sucesores = []
    filas = len(laberinto)
    columnas = len(laberinto[0])
    x, y = estado_actual.pos

    for dx, dy in MOVIMIENTOS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < filas and 0 <= ny < columnas:
            celda = laberinto[nx][ny]
            if CELDAS.get(celda, {}).get('pasable', True):
                nueva_pos = (nx, ny)
                nuevo_g = estado_actual.g + costo(estado_actual.pos, nueva_pos, laberinto)
                nuevo_h = 0
                if usar_heuristica and meta is not None:
                    nuevo_h = abs(nx - meta[0]) + abs(ny - meta[1])
                sucesores.append(Estado(nueva_pos, estado_actual, nuevo_g, nuevo_h))

    return sucesores
