# Configuración general
# Diccionario central de tipos de celdas
CELDAS = {
    '.': {'nombre': 'camino', 'costo': 1, 'pasable': True, 'color': (4, 4, 4)},
    '#': {
    'nombre': 'muro',
    'costo': float('inf'),
    'pasable': False,
    'color': (0, 0, 0),
    'borde': (0, 150, 255)
},
    'R': {'nombre': 'fantasma rojo', 'costo': 10, 'pasable': True, 'color': (255, 0, 0)},
    'G': {'nombre': 'fantasma azul', 'costo': 5, 'pasable': True, 'color': (0, 0, 255)},
    'S': {'nombre': 'inicio', 'costo': 1, 'pasable': True, 'color': (0, 255, 0)},
    'X': {'nombre': 'meta', 'costo': 0, 'pasable': True, 'color': (255, 255, 0)}
}

