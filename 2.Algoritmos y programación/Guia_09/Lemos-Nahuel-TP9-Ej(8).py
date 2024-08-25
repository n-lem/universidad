# Título: Reemplazar texto
# Escriba un programa que abra un archivo de texto, el nombre debe ser 
# solicitado el usuario este debe tener la característica de ser un archivo 
# de texto plano ej cancion.txt
# ● Investigue qué función de python reemplaza textos.
# ● Muestre todo el texto en pantalla
# ● Solicite al usuario un texto a buscar y el texto que reemplaza al texto buscado.
# ● Analice el archivo, busque y encuentre dentro del archivo el texto buscado
# ● y reemplácelo por el texto de reemplazo.
# ● Atención, el texto buscado es 'sensible' a mayusculas o minusculas.
# ● Trate de solucionar cómo guardar los cambios, revise el material visto en clases.
# ● Si no hubiera coincidencia deberá avisar.
# Atención cuando abra el archivo utilice la codificación utf8
# with open(nombre_archivo,'r',encoding='utf8') as xxxx :

import io

# Definimos una función que recibe el nombre del archivo como parámetro
def reemplazar_texto():
    try:
        # Solicito al usuario el nombre del archivo a abrir
        nombre_archivo = input('Ingrese el nombre del archivo a abrir: ')

        # Abro el archivo con la codificación utf8
        with open(nombre_archivo, "r", encoding="utf8") as archivo:
            # Leo el contenido del archivo y lo muestro por pantalla
            contenido = archivo.read()
            print('Contenido del archivo:')
            print(contenido)
            print()

            # Solicito un texto a buscar y un texto de reemplazo
            texto_buscar = input('Ingrese el texto a buscar: ')
            texto_reemplazar = input('Ingrese el texto de reemplazo: ')
            print()

            # Uso la función replace para reemplazar el texto buscado por el de reemplazo
            nuevo_contenido = contenido.replace(texto_buscar, texto_reemplazar)

            # Verifico si hubo algún cambio en el contenido
            if nuevo_contenido != contenido:
                # Si hubo cambio, muestro el nuevo contenido en pantalla
                print("El nuevo contenido del archivo es:")
                print(nuevo_contenido)

                # Abro el archivo en modo escritura con codificación utf8
                with open(nombre_archivo, "w", encoding="utf8") as archivo:
                    # Escribo el nuevo contenido en el archivo, sobreescribiendo el anterior
                    archivo.write(nuevo_contenido)
                    
                    # Muetro un mensaje si se realizó bien
                    print("Se ha guardado los cambios en el archivo.")
            else:
                # Si no hubo cambio, muestro un mensaje de aviso
                print("No se encontró ninguna coincidencia con el texto buscado.")

    except FileNotFoundError:
        # Si el archivo no existe, muestro un mensaje de error
        print("El archivo no existe o no se encuentra en el directorio actual.")

# Ejecuto el programa
reemplazar_texto()

