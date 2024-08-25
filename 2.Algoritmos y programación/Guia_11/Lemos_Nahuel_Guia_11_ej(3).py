# Realice un código, donde MiArchivo sea un TDA que tiene dos métodos:
# escribir y leer. El método escribir abre el archivo en modo de 
# escritura (“w”) y escribe el texto proporcionado.

# El método leer abre el archivo en modo de lectura (“r”) y devuelve el 
# contenido del archivo.

# Tenga en cuenta que este código sobrescribirá cualquier contenido 
# existente en el archivo cuando se use el método escribir.

# ¿Cómo agregaría el texto al final del archivo sin eliminar el 
# contenido existente?

import io

class MiArchivo:
    # Incializo el constructor
    def __init__(self,nombre_archivo):
        self.nombre_archivo = nombre_archivo

    # Defino el método escribir que recibe un texto como parámetro
    def escribir(self, texto):
        # Abro el archivo en modo escritura
        archivo = open(self.nombre_archivo, 'w')

        # Escribo el mensaje
        archivo.write(texto)

        # Cierro el archivo
        archivo.close()

    # Defino el método leer que no recibe parámetros
    def leer(self):
        # Abro el archivo en modo lectura
        archivo = open(self.nombre_archivo, 'r')

        # Leo el contenido y lo almaceno en una variable
        contenido = archivo.read()

        # Cierro el archivo
        archivo.close()

        # Devuelvo el contenido del archivo
        return contenido

    # Defino el método para agregar un texto que se ingresa como parámetro
    def agregar(self, texto):
        # Para agregar el texto al final del archivo, se puede usar el 
        # modo de apertura "a".

        archivo = open(self.nombre_archivo, 'a')

        # Escribo el texto en el archivo
        archivo.write(texto)

        # Cierro el archivo
        archivo.close()

# Creo una instancia
# mi_archivo = MiArchivo("prueba.txt")

# Uso el método escribir para escribir "Hola mundo" en el archivo
# mi_archivo.escribir("Hola mundo")

# Uso el método leer para leer el contenido del archivo
# contenido = mi_archivo.leer()

# Muestro el contenido por pantalla
# print(contenido)



# # Uso el método agregar para agregar "\nNueva línea"
# mi_archivo.agregar("\nNueva línea")

# contenido = mi_archivo.leer()
# print(contenido)

