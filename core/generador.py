import random

def generar_laberinto(filas=6, columnas=10, num_muros=None, num_fantasmas_rojos=None, num_fantasmas_azules=None):
    laberinto = [['.' for _ in range(columnas)] for _ in range(filas)]

    def posiciones_libres():
        return [(i, j) for i in range(filas) for j in range(columnas) if laberinto[i][j] == '.']

    total_celdas = filas * columnas
    num_muros = num_muros if num_muros is not None else int(total_celdas * 0.30)
    num_fantasmas_rojos = num_fantasmas_rojos if num_fantasmas_rojos is not None else max(1, int(total_celdas * 0.07))
    num_fantasmas_azules = num_fantasmas_azules if num_fantasmas_azules is not None else max(1, int(total_celdas * 0.09))

    for _ in range(num_muros):
        x, y = random.choice(posiciones_libres())
        laberinto[x][y] = '#'

    for _ in range(num_fantasmas_rojos):
        x, y = random.choice(posiciones_libres())
        laberinto[x][y] = 'R'

    for _ in range(num_fantasmas_azules):
        x, y = random.choice(posiciones_libres())
        laberinto[x][y] = 'G'

    x, y = random.choice(posiciones_libres())
    laberinto[x][y] = 'S'
    inicio = (x, y)

    x, y = random.choice(posiciones_libres())
    laberinto[x][y] = 'X'
    meta = (x, y)

    return laberinto, inicio, meta
