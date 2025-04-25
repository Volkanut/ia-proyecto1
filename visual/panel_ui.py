import pygame

# Configuración de botones
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 80
BUTTON_MARGIN = 20
COLOR_BOTON = (70, 130, 180)
COLOR_HOVER = (100, 180, 240)
COLOR_TEXTO = (255, 255, 255)

# Configuración de inputs
COLOR_INPUT = (255, 255, 255)
COLOR_INPUT_BORDER = (180, 180, 180)
COLOR_INPUT_TEXT = (0, 0, 0)
INPUT_WIDTH = 100
INPUT_HEIGHT = 50

class Boton:
    def __init__(self, x, y, texto, fuente):
        self.rect = pygame.Rect(x, y, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.texto = texto
        self.fuente = fuente
        self.activo = True

    def dibujar(self, pantalla, mouse_pos):
        color = COLOR_HOVER if self.rect.collidepoint(mouse_pos) else COLOR_BOTON
        pygame.draw.rect(pantalla, color, self.rect, border_radius=8)
        texto_surface = self.fuente.render(self.texto, True, COLOR_TEXTO)
        texto_rect = texto_surface.get_rect(center=self.rect.center)
        pantalla.blit(texto_surface, texto_rect)

    def fue_clickeado(self, evento):
        return self.activo and evento.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(evento.pos)

class InputBox:
    def __init__(self, x, y, text='', label=''):
        self.rect = pygame.Rect(x, y, INPUT_WIDTH, INPUT_HEIGHT)
        self.color = COLOR_INPUT_BORDER
        self.text = text
        self.txt_surface = pygame.font.SysFont("Arial", 32).render(text, True, COLOR_INPUT_TEXT)
        self.active = False
        self.label = label

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                self.active = False
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.unicode.isnumeric():
                self.text += event.unicode
            self.txt_surface = pygame.font.SysFont("Arial", 32).render(self.text, True, COLOR_INPUT_TEXT)

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, COLOR_INPUT, self.rect)
        pygame.draw.rect(pantalla, self.color, self.rect, 3)
        pantalla.blit(self.txt_surface, (self.rect.x + 10, self.rect.y + 10))

        fuente_label = pygame.font.SysFont("Arial", 20, bold=True)
        label_surface = fuente_label.render(self.label, True, (50, 50, 50))
        pantalla.blit(label_surface, (self.rect.x + 5, self.rect.y - 25))

    def obtener_valor(self):
        try:
            return int(self.text)
        except:
            return None

def crear_botones(ancho_pantalla, alto_pantalla):
    fuente = pygame.font.SysFont("Arial", 35)
    textos = ["BFS", "DFS", "A*","AVARA" ,"F/C","R", "DYN", "ADAPT", "START"]
    total_ancho = len(textos) * BUTTON_WIDTH + (len(textos) - 1) * BUTTON_MARGIN
    x_inicial = (ancho_pantalla - total_ancho) // 2
    y = alto_pantalla - BUTTON_HEIGHT - 40

    botones = []
    for i, texto in enumerate(textos):
        x = x_inicial + i * (BUTTON_WIDTH + BUTTON_MARGIN)
        botones.append(Boton(x, y, texto, fuente))

    return botones

def crear_inputs(ancho_pantalla):
    x_input = ancho_pantalla // 2 - 120
    y_input = 20
    input_filas = InputBox(x_input, y_input, label="Filas")
    input_columnas = InputBox(x_input + 140, y_input, label="Columnas")
    return input_filas, input_columnas
