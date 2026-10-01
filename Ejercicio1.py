import math

# Generar un diccionario por comprensión para n donas (por ejemplo, del 1 al 10)
# donde cada clave es el número de dona y el valor es (sqrt(2)) ** n
n_donas = 10

donas = {i: math.pow(math.sqrt(2), i - 1) for i in range(1, n_donas + 1)}

# Mostrar el resultado
print(donas)