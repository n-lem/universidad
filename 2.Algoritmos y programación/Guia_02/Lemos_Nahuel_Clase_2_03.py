# Alumno: Lemos, Nahuel

# Escriba un programa que permita cargar por teclado un vector de 10 posiciones,
# con números enteros, luego debe mostrar los números pero si el número termina
# en 3 8 4 9 debe agregar un * antes de mostrar el número (investigue cómo obtener
# un ultimo digito de un número).

# Importo librerías
import array as arr
import random


def vector():
    # Asigno el valor 10 a la variable elementos
    elementos = 10

    # Creo un array de enteros con los valores del 0 al 9, usando la función range
    vector = arr.array("i", range(10))

    # Uso un bucle for para recorrer cada elemento del array
    for elemento in vector:
        # Asigno un valor aleatorio entre 50 y 150 al elemento, usando la función randint
        elemento = random.randint(50, 150)

        # Verifico si el elemento termina en 3, 4, 8 o 9, usando el operador módulo (%). Es decir, el resto que se obtiene al realizar la división por 10
        if elemento % 10 in [3, 4, 8, 9]:
            # Si se cumple la condición, imprimo el elemento con un asterisco (*) al principio
            print(f"*{elemento}")
        # Si no se cumple la condición, imprimo el elemento sin modificar
        else:
            print(elemento)


vector()
