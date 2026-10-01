def total_donas_fiesta(a, b):
    total = 0
    # Sumamos 'a' donas para cada una de las 'b' personas iterativamente
    for _ in range(b):
        total += a
    return total

# Ejemplo de uso/prueba:
# 4 donas por persona, 6 personas -> Total: 24 donas
print(total_donas_fiesta(4, 6))