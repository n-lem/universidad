#Crear un programa que abra un fichero en modo lectura y escritura, si no existe 
# lo creará, y añadir la frase ‘Este es el ejercicio 1’. Luego, abrir el fichero 
# editado y muestrar el estado del fichero, el modo en el que fue abierto, el nombre 
# y la codificación de caracteres del mismo. Realizarlo utilizando la estructura with. 

# Librería io
import io

# Función para ver el estado del archivo
def estado_archivo(nombre_archivo):
    # Estado del archivo
    if nombre_archivo.closed:
        print('Estado: El archivo está cerrado')
    
    else:
        print('Estado: El archivo está abierto')


# Función que contiene lo hecho en el ejercicio 1 y 2
def abrir_archivo(nombre_archivo, modo):
    # Crea un contexto para una ejecución segura. Es para evitar daños en el archivo.
    with open(nombre_archivo, modo) as archivo:
        # Escribo contenido en el archivo
        archivo.write("Este es el ejercicio 1")

        # Estado del archivo
        estado_archivo(archivo) # Abierto porque está dentro del with
        print()

        # Modo de apertura del archivo
        print("Modo en el que se abrió el archivo:",archivo.mode)
        print()

    # Estado del archivo
    estado_archivo(archivo) # Cerrado porque está fuera del with
    print()

    # Crea un contexto para una ejecución segura. Es para evitar daños en el archivo.
    with open(nombre_archivo, "r") as archivo:
        # Modo de apertura del archivo
        print("Modo en el que se abrió el archivo:",archivo.mode)
        print()

        # Nombre del archivo
        print("Nombre del archivo:",archivo.name)
        print()

        # Codificación del archivo
        print("Codificación de caracteres del archivo:",archivo.encoding)
        print()

        # Contenido del archivo
        print("Contenido del archivo:")
        print(archivo.read())
        print()

    # Estado del archivo
    estado_archivo(archivo)


# Ejecuto el programa
abrir_archivo('Ejercicio_3.txt', 'w')