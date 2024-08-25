# Alumno: Lemos, Nahuel

# Funciones recursivas

# Implementar una función para calcular el producto de dos números enteros dados.

def producto_recursivo(x, y):
    # Si x o y son cero, devuelvo cero
    if x == 0 or y == 0:
        return 0
    # Sumo el primer número a sí mismo y resto 1 al segundo número
    return x + producto_recursivo(x, y - 1)

