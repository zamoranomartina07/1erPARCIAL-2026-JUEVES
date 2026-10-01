def total_interrupciones(a, b):

    if b == 0:
        return 0
    
    # Caso recursivo: suma las interrupciones de 1 hora ('a') 
    # más el resultado para las horas restantes ('b - 1')
    return a + total_interrupciones(a, b - 1)

# Ejemplo de prueba:
# 4 interrupciones por hora durante 3 horas -> Total: 12
print(total_interrupciones(4, 3))