# Verifica si el objetivo fue alcanzado
def es_meta(estado, meta_pos):
    """
    Verifica si un estado es el objetivo.

    Args:
        estado (Estado): El estado actual del agente.
        meta_pos (tuple): Coordenadas (x, y) del objetivo (queso).

    Returns:
        bool: True si el estado es el objetivo.
    """
    return estado.pos == meta_pos
