# Alumno: Lemos, Nahuel

# Escriba un programa que utilice tres funciones, que dada una secuencia 
# numérica (lista, tupla, vector) debe:
# a. Encontrar el mayor de los valores
# b. Calcular el promedio
# c. Encontrar el valor más bajo
# El programa debe mostrar los tres resultados por pantalla.


def estadisticas(vector):
    # Imprimo el valor máximo del vector
    print(f'El mayor de la secuencia es: {max(vector)}')

    # Imprimo el promedio de los valores del vector
    print(f'El promedio de la secuencia es: {sum(vector)/len(vector)}')

    # Imprimo el valor mínimo del vector
    print(f'El menor de la secuencia es: {min(vector)}')



# Vector
arreglo = [3,2,5,6,7]

# Llamo a la función
estadisticas(arreglo)
