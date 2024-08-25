# Alumno: Lemos, Nahuel

# Funciones recursivas

# Implementar una función para calcular la potencia dado dos números enteros, el 
# primero representa la base y el segundo el exponente.

def calcular_potencia(base, exponente):
    # Si el exponente es 0, el resultado es 1
    if exponente == 0:
        return 1
    
    # Calculo la potencia reduciendo el exponente en 1 en cada llamada recursiva
    return base * calcular_potencia(base, exponente - 1)
