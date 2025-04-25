# Clase Estado (posición, costo, heurística, etc.)

class Estado:
    def __init__(self, posicion, padre=None, g=0, h=0):
        """
        Crea un nuevo estado del agente.

        Args:
            posicion (tuple): Coordenadas (x, y) del agente.
            padre (Estado): Estado desde el cual se llegó a este.
            g (int): Costo desde el inicio hasta este nodo.
            h (int): Estimación heurística al objetivo (solo para A*).
        """
        self.pos = posicion
        self.padre = padre
        self.g = g
        self.h = h

    def f(self):
        """
        Valor f para A*: f = g + h
        """
        return self.g + self.h

    def __eq__(self, other):
        """
        Compara dos estados por su posición.
        """
        return self.pos == other.pos

    def __lt__(self, other):
        """
        Para comparar en estructuras como colas de prioridad (A*).
        """
        return self.f() < other.f()

    def reconstruir_camino(self):
        """
        Reconstruye el camino desde el inicio hasta este estado.
        """
        camino = []
        actual = self
        while actual is not None:
            camino.append(actual.pos)
            actual = actual.padre
        camino.reverse()
        return camino
