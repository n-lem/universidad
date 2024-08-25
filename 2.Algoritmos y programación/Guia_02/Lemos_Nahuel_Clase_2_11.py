# Alumno: Lemos, Nahuel

# Funciones Recursivas

# Implementar una función que calcule la suma de todos los números enteros 
# comprendidos entre cero y un número entero positivo dado.

def suma_enteros(n):
    # Si n es cero, se devuelve cero
    if n == 0:
        return 0
    # Se devuelve n con la suma de los enteros anteriores
    else:
        return n + suma_enteros(n-1)
