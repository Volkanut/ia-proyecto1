# Agente móvil (estado actual)
import pygame
import os

CELL_SIZE = 200
ANIM_INTERVAL = 150  # Milisegundos entre frames

class Pacman:
    def __init__(self):
        self.direccion = 'right'  # dirección inicial
        self.frames = {
            'up': self.cargar_frames('pacman-up'),
            'down': self.cargar_frames('pacman-down'),
            'left': self.cargar_frames('pacman-left'),
            'right': self.cargar_frames('pacman-right')
        }
        self.frame_actual = 0
        self.tiempo_ultimo_frame = pygame.time.get_ticks()

    def cargar_frames(self, carpeta):
        ruta = os.path.join('assets', carpeta)
        return [
            pygame.transform.scale(pygame.image.load(os.path.join(ruta, f"{i}.png")), (CELL_SIZE, CELL_SIZE))
            for i in range(1, 4)
        ]

    def actualizar_direccion(self, actual, siguiente):
        if not siguiente:
            return
        di, dj = siguiente[0] - actual[0], siguiente[1] - actual[1]
        if di == -1: self.direccion = 'up'
        elif di == 1: self.direccion = 'down'
        elif dj == -1: self.direccion = 'left'
        elif dj == 1: self.direccion = 'right'

    def obtener_frame_actual(self):
        ahora = pygame.time.get_ticks()
        if ahora - self.tiempo_ultimo_frame > ANIM_INTERVAL:
            self.frame_actual = (self.frame_actual + 1) % len(self.frames[self.direccion])
            self.tiempo_ultimo_frame = ahora
        return self.frames[self.direccion][self.frame_actual]

    def dibujar(self, pantalla, posicion):
        i, j = posicion
        x = j * (CELL_SIZE + 2) + 300 + CELL_SIZE // 2
        y = i * (CELL_SIZE + 2) + 100 + CELL_SIZE // 2
        imagen = self.obtener_frame_actual()
        rect = imagen.get_rect(center=(x, y))
        pantalla.blit(imagen, rect)
