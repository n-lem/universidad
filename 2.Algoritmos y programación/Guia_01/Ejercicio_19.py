# 19. Escribir un programa que solicite un número entero positivo, que muestre los
# múltiplos de 5 que existen entre el número ingresado y su multiplicación por 30.
# por ejemplo: entre 3 y (3*30)


# Solicito un número entero positivo
entero = int(input('Ingrese un número entero positivo: '))

# Multiplico el número ingresado por 30
multiplo = entero * 30

# Recorro los números desde el valor ingresado, hasta el valor ingresado 
# ultiplicado por 30 más 1. Le sumo 1 por la forma en la cual funciona el for
for multiplos in range(entero,multiplo+1):
    # Verifico si el número en el cual se encuentra el ciclo es múltiplo de 5
    if multiplos % 5 == 0:
        # Si es múltiplo de 5 lo imprimo en pantalla
        print(multiplos)

