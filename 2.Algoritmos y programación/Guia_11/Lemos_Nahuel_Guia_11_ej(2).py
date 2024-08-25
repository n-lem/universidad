# Cree un programa que lea un archivo de texto, cuente la cantidad de
# palabras en el archivo y luego escriba el resultado en otro archivo.
# Suponga que tiene un archivo de texto llamado "entrada2.txt" con el
# siguiente contenido:

'''
Python es un lenguaje de programación muy poderoso y versátil.
Es ampliamente utilizado en diversas aplicaciones, incluyendo desarrollo web, análisis de
datos y aprendizaje automático.
'''
# A continuación, cree un programa para contar las palabras en este
# archivo y escribir el resultado en un nuevo archivo llamado 
# "resultado2.txt"

# Importo la libería io para trabajar con archivos
import io

# Defino una función llamada contar_palabras
def contar_palabras():
	# Abro el archivo llamado entrada2.txt en modo lectura
	archivo_entrada = open('entrada2.txt', 'r')

	# Leo todo el contenido del archivo y lo guardo en una variable llamada contenido
	contenido = archivo_entrada.read()

	# Divido el contenido por espacios y guardo cada palabra en una lista llamada palabras
	palabras = contenido.split()

	# Obtengo la longitud de la lista palabras y la guardo en una variable llamada cantidad_palabras
	cantidad_palabras = len(palabras)

	# Cierro el archivo de entrada
	archivo_entrada.close()

	# Abro el archivo llamado resultado2.txt en modo escritura
	archivo_escritura = open('resultado2.txt', 'w')

	# Escribo la variable cantidad_palabras en el archivo de escritura, convirtiéndola a cadena de caracteres
	archivo_escritura.write(str(cantidad_palabras))

	# Cierro el archivo de escritura
	archivo_escritura.close()

	# Elimino los archivos de entrada y escritura
	del(archivo_entrada)
	del(archivo_escritura)

# Llamo a la función contar_palabras
contar_palabras()
