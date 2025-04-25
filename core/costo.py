# Funciones de costo de ruta
from config import CELDAS

def costo(paso_actual, paso_siguiente, laberinto):
    x, y = paso_siguiente
    celda = laberinto[x][y]
    return CELDAS.get(celda, {}).get('costo', 1)  # valor por defecto = 1

