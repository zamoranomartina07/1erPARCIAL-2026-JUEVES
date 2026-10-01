def ordenar_eventos(eventos, descendente=False):
    """
    Ordena la lista de eventos según el valor booleano indicado.
    - Si descendente es True: ordena de Z a A.
    - Si descendente es False (por defecto): ordena de A a Z.
    """
    return sorted(eventos, reverse=descendente)

# Ejemplos de prueba:
eventos_springfield = ["Kermés", "Concurso de Comida", "Reunión del Concejo Municipal"]

# 1. Sin parámetro booleano (orden ascendente por defecto)
print(ordenar_eventos(eventos_springfield))
# Resultado: ['Concurso de Comida', 'Kermés', 'Reunión del Concejo Municipal']

# 2. Con expresión en True (orden descendente: Z a A)
print(ordenar_eventos(eventos_springfield, True))
# Resultado: ['Reunión del Concejo Municipal', 'Kermés', 'Concurso de Comida']

# 3. Con expresión en False (orden ascendente: A a Z)
print(ordenar_eventos(eventos_springfield, False))
# Resultado: ['Concurso de Comida', 'Kermés', 'Reunión del Concejo Municipal']