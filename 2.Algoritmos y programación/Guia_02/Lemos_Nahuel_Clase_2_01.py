# Alumno: Lemos, Nahuel

# Escriba un programa que contenga un vector de 10 posiciones con valores 
# enteros mayores a 1000 y menores a 2000, luego muestre los valores y sus 
# posiciones.

# Importo las librerías
import array as arr
import random


# Defino la función para mostrar el vector
def mostrar_vector():
    # Creo un arreglo de 11 posiciones con valores enteros aleatorios entre 1000 y 2001
    vector = arr.array("i", range(10))
    print(f"Posición\tValor")

    # Muestro los valores y sus posiciones
    for elemento in vector:
        vector[elemento] = random.randint(1000, 2001)
        print(f"{elemento+1:^8}\t{vector[elemento]}")


mostrar_vector()
