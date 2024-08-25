# Alumno: Lemos, Nahuel

# Escriba una función para cargar un vector con n cantidad de elementos con 
# valores 0 y 1 correlativamente , luego debe retornar el vector.
# Para probar la función escriba un programa que solicite al usuario la cantidad 
# de elementos para el vector este número debe ser entero positivo, Utilice la
# función integrada de python .isnumeric() para verificar, ejemplo: 
# mi_numero.isnumeric() devuelve True o False, si es correcto debe llamar a la
# función y devolver el vector con los elementos pedidos y luego debe mostrar 
# los elementos del vector uno debajo del otro por pantalla pero si es incorrecto 
# debe volver a solicitar un nuevo número, antes controle y avise que hubo un 
# error.

# Salida: 

# Creación de vector

# Ingrese cantidad de elementos: 5
# 0
# 1
# 0
# 1
# 0


def cargar_vector(n):
    # Creo una lista vacía para almacenar los elementos
    vector = []

    # Uso un bucle for para recorrer los números desde 0 hasta n
    for i in range(n):

        # Si el número es par, agrego un 0 a la lista
        if i % 2 == 0:
            vector.append(0)
        # Si el número es impar, agrego un 1 a la lista
        else:
            vector.append(1)
        # Devuelvo la lista como resultado de la función
    return vector



def crear_vector():
    # Mensaje
    print("Creación de vector")
    
    # Uso un bucle while
    while True:
        # Pedo al usuario que ingrese la cantidad de elementos
        n = input("Ingrese cantidad de elementos: ")

        # Verifico si el valor ingresado es numérico y positivo
        if n.isnumeric() and int(n) > 0:
            # Convierto el valor a entero
            n = int(n)
            # Llamo a la función con el valor ingresado y guardo el resultado en una variable
            vector = cargar_vector(n)
            # Muestro el vector por pantalla, uno debajo del otro
            for elemento in vector:
                print(elemento)

            # Salgo del bucle while
            break

        # Si el valor ingresado no es válido, muestro un mensaje de error y vuelvo a pedir otro valor
        else:
            print("Error: debe ingresar un número entero positivo.")



crear_vector()