def total_donas_fiesta(a, b):
    total = 0
    # Sumamos 'a' donas para cada una de las 'b' personas iterativamente
    for _ in range(b):
        total += a
    return total

# Ejemplo de uso/prueba:
# 3 donas por persona, 5 personas -> Total: 15 donas
print(total_donas_fiesta(3, 5))