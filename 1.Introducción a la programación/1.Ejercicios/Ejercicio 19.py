# Primero investigue cómo obtener el último dígito de un valor, luego escriba un
# programa que calcule el último dígito de la siguiente operación aritmética 58742
# al cubo (58742 ** 3), muestre por pantalla el resultado de las dos operaciones.


# Obteniendo el último dígito de un número
ultimo_digito = 58742 % 10

# Calculando el último dígito del cubo de 58742
ultimo_digito_cubo = (ultimo_digito ** 3) % 10

print(f"El último dígito de 58742 al cubo es: {ultimo_digito_cubo}")