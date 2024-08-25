# Cree un programa que lee datos desde un archivo, los procesa y luego
# escribe el resultado en otro archivo. Suponga que tiene un archivo 
# llamado "entrada.txt" con números enteros separados por comas, y 
# desea calcular la suma de estos números y escribir el resultado en
# un archivo llamado "salida.txt".

# Importo la librería io
import io

def procesar_archivo():
	# Abro el archivo en forma de lectura
	archivo_lectura = open('entrada.txt', 'r')

	# Almaceno el contenido del archivo en una variable
	contenido = archivo_lectura.read()

	# Creo una lista vacía para más tarde guardar los valores numéricos
	numeros = []

	# Divido el texto del archivo por comas y se almacenan en una lista
	numeros_separados = contenido.split(',')

	# Recorro los valores separados que están en la lista numeros_separados
	for numero in numeros_separados:
		# A la lista vacía numeros le agrego cada numero individual
		numeros.append(int(numero))

	# Sumo los valores almacenados en la lista numeros
	suma = sum(numeros)

	# Cierro el archivo
	archivo_lectura.close()

	# Creo un archivo llamado entrada2.txt y lo abro en modo escritura
	archivo_escritura = open('entrada2.txt','w')

	# Escribo el contenido de la suma en el archivo entrada2.txt
	archivo_escritura.write(str(suma))	

	# Cierro el archivo entrada2.txt
	archivo_escritura.close()

	# Borro los archivos de la memoria, porque ya están en el disco rígido
	del(archivo_lectura)
	del(archivo_escritura)

# Ejecuto el programa
procesar_archivo()
