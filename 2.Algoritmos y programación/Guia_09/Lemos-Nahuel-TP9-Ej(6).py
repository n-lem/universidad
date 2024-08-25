# Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la 
# tabla de multiplicar de ese número, y muestre por pantalla la línea m del fichero. Si el fichero 
# no existe debe mostrar un mensaje por pantalla informando de ello.

import io

def mostrar_linea_tabla_multiplicar():
    try:
        # Se pide al usuario que ingrese dos números enteros entre 1 y 10
        print('Selección de archivo')
        n = int(input("Ingrese un número entero entre 1 y 10: "))
        print()
        print('Selección de fila')
        m = int(input("Ingrese otro número entero entre 1 y 10: "))
        print()
        # Se verifica si los números ingresados están dentro del rango permitido
        if (n < 1 or n > 10) or (m < 1 or m > 10):
            print("Los números deben estar entre 1 y 10")
            print()
        else:
            # Se abre el archivo con el nombre "tabla-n.txt", donde "n" es el número ingresado
            with open(f"tabla-{n}.txt", "r") as archivo:
                # Se lee la línea m del archivo y se muestra por pantalla
                contenido = archivo.readlines()
                linea = contenido[m-1]
                print(linea)
                # print(archivo.readlines()[m-1]) # En una línea
    except FileNotFoundError:
        # Se muestra un mensaje de error si el archivo no existe
        print(f"No existe el archivo tabla-{n}.txt")

mostrar_linea_tabla_multiplicar()
