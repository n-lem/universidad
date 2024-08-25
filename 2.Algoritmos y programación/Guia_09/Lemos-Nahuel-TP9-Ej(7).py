# Título: Búsqueda textual
# Dado el archivo de texto cancion.txt, brindado por el profesor, realice la 
# descarga y guárdelo en el mismo path donde creará su programa.
# ● Muestre todo el texto en pantalla
# ● Solicite al usuario un texto a buscar.
# ● Analice el archivo, busque y encuentre dentro del archivo el texto 
# buscado
# imprima por pantalla todas las líneas completas donde aparezca el texto.
# ● Atención, el texto buscado no debe ser sensible a mayúsculas o 
# minúsculas.
# ● Devuelva cuantas veces se encontró el texto introducido en el total del 
# archivo
# ● Si no hubiera coincidencia deberá avisar.
# Atención cuando abra el archivo utilice la codificación utf8
# with open(nombre_archivo,'r',encoding='utf8') as xxxx :

import io

def buscar_texto():
    try:
        # Abro el archivo cancion.txt con la codificación utf8
        with open('cancion.txt', 'r', encoding='utf8') as archivo:
            # Leo el contenido del archivo y lo muestro por pantalla
            print('Contenido del archivo:')
            contenido = archivo.read()
            print()
            print(contenido)
            print()

            # Solicito un texto a buscar y lo convierto en minúsculas para hacer la búsqueda no sensible a mayúsculas o minúsculas
            texto_buscar = input('Ingrese el texto a buscar: ').lower()

            # Inicializo el contador de coincidencias en 0
            coincidencias = 0

            # Busco el texto en el archivo y muestro las líneas completas donde aparece
            lineas_encontradas = []
            coincidencias = 0
            print()
            print('Líneas encontradas: ')
            print()
            for linea in contenido.splitlines():
                if texto_buscar in linea.lower():
                    print(linea)
                    lineas_encontradas.append(linea)
                    coincidencias += 1
            print()

            # Muestro el número de coincidencias del texto en el archivo
            if coincidencias == 0:
                print('No se encontraron coincidencias')
            else:
                print(f'El texto se encontró {coincidencias} veces en el archivo')

    except FileNotFoundError:
        # Muestro un mensaje de error si el archivo no existe
        print('No se encontró el archivo cancion.txt')

# Ejecuto el programa
buscar_texto()
