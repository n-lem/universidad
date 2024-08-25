# Crear un programa que abra el fichero editado anteriormente y muestre el estado del fichero,
# el modo en el que fue abierto, el nombre y la codificación de caracteres del mismo.

# La libreria permite trabajar con archivos. 'io' viene de input/output
import io

# Creo una funcion para leer un archivo
def leer_archivo(nombre_archivo, estado):
    # Abro el archivo en modo lectura
    archivo = open(nombre_archivo, estado)

    # Estado del archivo
    if archivo.closed == True:
        print('Estado: El archivo está cerrado')
    else:
        print('Estado: El archivo está abierto')
    print()

    # Modo en el cual se abrió el archivo
    print('Modo en el que se abrió el archivo:', archivo.mode)
    print()

    # Nombre del archivo
    print('Nombre del archivo:', archivo.name)
    print()

    # Codificación del archivo
    print('Codificación de caracteres del archivo:', archivo.encoding) # 'cp65001' es UTF-8
    print()

    # Leo el contenido y lo guardo en una variable
    print('Contenido del archivo:')
    print(archivo.read())

    # Cierro el archivo
    archivo.close()
    print()

    # Estado del archivo
    if archivo.closed:
        print('Estado: El archivo está cerrado')
    else:
        print('Estado: El archivo está abierto')


# Ejecuto el programa
leer_archivo('archivo_ejercicio_9_1.txt', 'r')