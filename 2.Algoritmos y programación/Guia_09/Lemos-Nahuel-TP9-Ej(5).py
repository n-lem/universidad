# Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt con la
# tabla de multiplicar de ese número, donde n es el número introducido, y la muestre por pantalla.
# Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.


import io

def mostrar_tabla_multiplicar():
    try:
        # Pido al usuario que ingrese un número entero entre 1 y 10
        n = int(input('Ingrese un número entero entre 1 y 10: '))

        # Verifico si el número ingresado está dentro del rango permitido
        if n < 1 or n > 10:
            print('El número debe estar entre 1 y 10')
        else:

            # Abro el archivo con el nombre 'tabla-n.txt', donde 'n' es el número ingresado
            with open(f'tabla-{n}.txt', 'r') as archivo:
                # Leo el contenido del archivo y se muestra por pantalla
                print(archivo.read())

    except FileNotFoundError:
        # Muestro un mensaje de error si el archivo no existe
        print(f'No existe el archivo tabla-{n}.txt')

mostrar_tabla_multiplicar()
