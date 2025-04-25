import pygame
import os
from .panel_ui import crear_botones, crear_inputs
from agentes.bfs import bfs
from agentes.dfs import dfs
from agentes.astar import astar
from agentes.greedy import greedy
from estrategia.adaptativo import agente_adaptativo
from entorno.meta import mover_meta
from entorno.laberinto import actualizar_paredes, mover_fantasmas
from core.generador import generar_laberinto
from entorno.personaje import Pacman
from config import CELDAS

CELL_SIZE = 200
MARGIN = 2
LEYENDA_WIDTH = 300
TIEMPO_MOV_META = 1000

# Sprites de fantasmas
sprite_rojo = pygame.transform.scale(pygame.image.load(os.path.join("assets", "ghosts", "red.png")), (CELL_SIZE, CELL_SIZE))
sprite_azul = pygame.transform.scale(pygame.image.load(os.path.join("assets", "ghosts", "blue.png")), (CELL_SIZE, CELL_SIZE))
sprite_meta = pygame.transform.scale(pygame.image.load(os.path.join("assets", "fruits", "strawberry.png")), (CELL_SIZE, CELL_SIZE))
def obtener_costo(celda):
    return CELDAS.get(celda, {}).get("costo", 1)

def dibujar_laberinto(pantalla, laberinto, camino=None, explorados=None):
    for i, fila in enumerate(laberinto):
        for j, celda in enumerate(fila):
            x = LEYENDA_WIDTH + j * (CELL_SIZE + MARGIN)
            y = i * (CELL_SIZE + MARGIN) + 100
            pos = (i, j)
            if celda == 'R':
                pantalla.blit(sprite_rojo, (x, y))
            elif celda == 'G':
                pantalla.blit(sprite_azul, (x, y))
            elif celda == 'X':
                pantalla.blit(sprite_meta, (x, y))
            elif celda == '#':
                color_fondo = CELDAS['#']['color']
                borde = CELDAS['#'].get('borde')
                pygame.draw.rect(pantalla, color_fondo, (x, y, CELL_SIZE, CELL_SIZE))
                if borde:
                    pygame.draw.rect(pantalla, borde, (x+3, y+3, CELL_SIZE-6, CELL_SIZE-6), width=2)

            else:
                if camino and pos in camino and celda not in ['S', 'X']:
                    color = (0, 200, 200)
                elif explorados and pos in explorados and (not camino or pos not in camino) and celda not in ['S', 'X']:
                    color = (180, 180, 255)
                else:
                    color = CELDAS.get(celda, {}).get("color", (100, 100, 100))
                pygame.draw.rect(pantalla, color, (x, y, CELL_SIZE, CELL_SIZE))

def iniciar_visualizacion(laberinto, inicio, meta):
    pygame.init()
    filas, columnas = len(laberinto), len(laberinto[0])
    ancho = columnas * (CELL_SIZE + MARGIN) + LEYENDA_WIDTH
    alto_total = filas * (CELL_SIZE + MARGIN) + 250
    pantalla = pygame.display.set_mode((ancho, alto_total))
    pygame.display.set_caption("Laberinto IA - Visual")

    pacman_animado = Pacman()

    botones = crear_botones(ancho, alto_total)
    input_filas, input_columnas = crear_inputs(ancho)
    camino = []
    explorados = set()
    boton_start_activo = False
    pacman_pos = None
    camino_actual = []
    animando = False
    indice_animacion = 0
    tiempo_ultimo_paso = 0
    dinamico_activado = False
    tiempo_ultimo_cambio = pygame.time.get_ticks()
    historial_recorrido = []
    costo_total_recorrido = 0
    algoritmo_actual = ""

    reloj = pygame.time.Clock()
    corriendo = True

    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

            input_filas.handle_event(evento)
            input_columnas.handle_event(evento)

            for boton in botones:
                if boton.fue_clickeado(evento):
                    if boton.texto == "BFS":
                        camino, _, explorados = bfs(laberinto, inicio, meta)
                        boton_start_activo = True
                        algoritmo_actual = "BFS"
                    elif boton.texto == "DFS":
                        camino, _, explorados = dfs(laberinto, inicio, meta)
                        boton_start_activo = True
                        algoritmo_actual = "DFS"
                    elif boton.texto == "A*":
                        camino, _, explorados = astar(laberinto, inicio, meta)
                        boton_start_activo = True
                        algoritmo_actual = "A*"
                    elif boton.texto == "AVARA":
                        camino, _, explorados = greedy(laberinto, inicio, meta)
                        boton_start_activo = True
                        algoritmo_actual = "AVARA"
                    elif boton.texto == "ADAPT":
                        camino, _, explorados, algoritmo_actual = agente_adaptativo(laberinto, inicio, meta)
                        boton_start_activo = True
                    elif boton.texto == "F/C":
                        nuevas_filas = input_filas.obtener_valor()
                        nuevas_columnas = input_columnas.obtener_valor()
                        if nuevas_filas and nuevas_columnas:
                            laberinto, inicio, meta = generar_laberinto(nuevas_filas, nuevas_columnas)
                            filas, columnas = nuevas_filas, nuevas_columnas
                            ancho = columnas * (CELL_SIZE + MARGIN) + LEYENDA_WIDTH
                            alto_total = filas * (CELL_SIZE + MARGIN) + 250
                            pantalla = pygame.display.set_mode((ancho, alto_total))

                            # Reiniciar todos los estados
                            botones = crear_botones(ancho, alto_total)
                            input_filas, input_columnas = crear_inputs(ancho)
                            camino = []
                            explorados = set()
                            boton_start_activo = False
                            pacman_pos = None
                            camino_actual = []
                            animando = False
                            indice_animacion = 0
                            tiempo_ultimo_paso = 0
                            dinamico_activado = False
                            tiempo_ultimo_cambio = pygame.time.get_ticks()
                            historial_recorrido = []
                            costo_total_recorrido = 0
                            algoritmo_actual = ""
                    elif boton.texto == "R":
                        camino = []
                        explorados = set()
                        pacman_pos = inicio
                        camino_actual = []
                        historial_recorrido = []
                        costo_total_recorrido = 0
                        algoritmo_actual = ""
                        animando = False
                        indice_animacion = 0
                        tiempo_ultimo_paso = 0
                        dinamico_activado = False
                        tiempo_ultimo_cambio = pygame.time.get_ticks()
                        print("🔄 Reset del entorno completo.")

  
                    elif boton.texto == "DYN":
                        dinamico_activado = not dinamico_activado
                        print("🔁 Dinámico activado:", dinamico_activado)
                        if dinamico_activado:
                            pacman_pos = inicio
                            tipo_inicial = laberinto[pacman_pos[0]][pacman_pos[1]]
                            historial_recorrido = [(pacman_pos, tipo_inicial)]
                            costo_total_recorrido = 0
                            camino, _, explorados, algoritmo_actual = agente_adaptativo(laberinto, pacman_pos, meta)
                            camino_actual = camino or []
                            indice_animacion = 0
                            tiempo_ultimo_paso = pygame.time.get_ticks()
                            animando = bool(camino_actual)
                    elif boton.texto == "START" and camino and boton_start_activo:
                        camino_actual = camino[:]
                        pacman_pos = camino_actual[0]
                        tipo_inicial = laberinto[pacman_pos[0]][pacman_pos[1]]
                        historial_recorrido = [(pacman_pos, tipo_inicial)]
                        costo_total_recorrido = 0
                        animando = True
                        indice_animacion = 0
                        tiempo_ultimo_paso = pygame.time.get_ticks()

        ahora = pygame.time.get_ticks()

        if dinamico_activado and ahora - tiempo_ultimo_cambio > TIEMPO_MOV_META:
            meta = mover_meta(laberinto, meta)
            actualizar_paredes(laberinto, pacman_pos, meta)
            mover_fantasmas(laberinto, pacman_pos, meta)
            camino, _, explorados, algoritmo_actual = agente_adaptativo(laberinto, pacman_pos, meta)
            camino_actual = camino or []
            indice_animacion = 0
            tiempo_ultimo_paso = ahora
            animando = bool(camino_actual)
            tiempo_ultimo_cambio = ahora

        if animando and camino_actual:
            if ahora - tiempo_ultimo_paso > 250:
                indice_animacion += 1
                if indice_animacion < len(camino_actual):
                    siguiente_pos = camino_actual[indice_animacion]
                    pacman_animado.actualizar_direccion(pacman_pos, siguiente_pos)
                    pacman_pos = siguiente_pos
                    tipo_celda = laberinto[pacman_pos[0]][pacman_pos[1]]
                    historial_recorrido.append((pacman_pos, tipo_celda))
                    costo_total_recorrido += obtener_costo(tipo_celda)
                    tiempo_ultimo_paso = ahora
                    if pacman_pos == meta:
                        animando = False
                        dinamico_activado = False
                        print("🎯 Pac-Man alcanzó la meta dinámica.")
                        print("📌 Historial completo:", historial_recorrido)
                        print("💰 Costo total real acumulado:", costo_total_recorrido)
                        print(f"🧠 Algoritmo utilizado: {algoritmo_actual}")
                        print("tamaño historial recorrido:", len(historial_recorrido))
                        print("🔎 Detalle paso a paso:")
                        acumulado = 0
                        for i in range(1, len(historial_recorrido)):
                            pos, tipo = historial_recorrido[i]
                            nombre = CELDAS.get(tipo, {}).get("nombre", "desconocido")
                            costo = obtener_costo(tipo)
                            acumulado += costo
                            print(f"Paso {i}: {pos} → {tipo} ({nombre}) → costo: {costo} → acumulado: {acumulado}")
                else:
                    animando = False

        pantalla.fill((0, 0, 0))
        dibujar_laberinto(pantalla, laberinto, camino, explorados)

        if pacman_pos:
            pacman_animado.dibujar(pantalla, pacman_pos)

        for boton in botones:
            if boton.texto == "START" and not boton_start_activo:
                pygame.draw.rect(pantalla, (100, 100, 100), boton.rect, border_radius=8)
                fuente = pygame.font.SysFont("Arial", 20)
                texto = fuente.render(boton.texto, True, (180, 180, 180))
                pantalla.blit(texto, texto.get_rect(center=boton.rect.center))
            else:
                boton.dibujar(pantalla, pygame.mouse.get_pos())

        input_filas.dibujar(pantalla)
        input_columnas.dibujar(pantalla)

        fuente_leyenda = pygame.font.SysFont("Arial", 30)
        leyenda = [
            ("Inicio", (0, 255, 0)),
            ("Meta", (255, 0, 0)),
            ("Fantasma Azul (5)", (0, 0, 255)),
            ("Fantasma Rojo (10)", (255, 0, 0)),
            ("Camino Final", (0, 200, 200)),
            ("Explorados", (180, 180, 255)),
        ]
        for i, (texto, color) in enumerate(leyenda):
            y_offset = 20 + i * 30
            pygame.draw.rect(pantalla, color, (10, y_offset, 20, 20))
            etiqueta = fuente_leyenda.render(texto, True, (255, 255, 255))
            pantalla.blit(etiqueta, (40, y_offset))

        if algoritmo_actual:
            fuente_algo = pygame.font.SysFont("Arial", 24, bold=True)
            etiqueta_algo = fuente_algo.render(f"Algoritmo: {algoritmo_actual}", True, (255, 255, 255))
            pantalla.blit(etiqueta_algo, (ancho - 250, 10))
            font_info = pygame.font.SysFont("Arial", 22)
            texto_costo = font_info.render(f"Costo total: {costo_total_recorrido}", True, (255, 255, 255))
            pantalla.blit(texto_costo, (ancho - 250, 40))
            
            # 🧩 Mostrar información en el lateral izquierdo
            fuente_info = pygame.font.SysFont("Arial", 20)
            info_y = 240 + len(leyenda) * 30

            info_items = [
                f"🎯 Meta: {meta if meta else '-'}",
                f"📍 Posición actual: {pacman_pos if pacman_pos else '-'}",
                f"🧠 Algoritmo: {algoritmo_actual or '-'}",
                f"🌀 Dinámico: {'Sí' if dinamico_activado else 'No'}",
                f"💰 Costo acumulado: {costo_total_recorrido}"
            ]

            for item in info_items:
                texto = fuente_info.render(item, True, (255, 255, 255))
                pantalla.blit(texto, (10, info_y))
                info_y += 25

            # 🪵 Últimos pasos del historial
            if historial_recorrido:
                pantalla.blit(fuente_info.render("🧾 Últimos pasos:", True, (255, 255, 255)), (10, info_y))
                info_y += 25
                fuente_hist = pygame.font.SysFont("Courier", 18)
                for paso in historial_recorrido[-50:]:
                    pos, tipo = paso
                    nombre = CELDAS.get(tipo, {}).get("nombre", "desconocido")
                    costo = obtener_costo(tipo)
                    linea = f"{pos} → {tipo} → +{costo}"
                    pantalla.blit(fuente_hist.render(linea, True, (200, 200, 200)), (10, info_y))
                    info_y += 22

        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()
