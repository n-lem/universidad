# Alumno: Lemos, Nahuel

# Escriba un programa que cargue un vector desde el número 100 al 200, debe utilizar 2 métodos de carga, usando range y otro utilizando while, luego muestre los valores uno al lado del otro.

# Importo las librerías
import array as arr



# Usando range
def usando_range():
	# Creo un array de enteros con los valores del 100 al 200, usando la función range
	print(arr.array('i',range(100, 201)))



# Usando while
def usando_while():
	# Creo una lista vacía para guardar los valores
	vector = []

	# Asigno el valor 100 a la variable i
	i = 100

	# El bucle while se repite mientras i sea menor o igual que 200
	while i <= 200:
		# Agrego el valor de i a la lista
		vector.append(i)
		# Aumento el valor de i en uno
		i += 1

	# Imprimo la lista con los valores
	print(vector)



# Muestro las funciones
usando_range()
usando_while()
