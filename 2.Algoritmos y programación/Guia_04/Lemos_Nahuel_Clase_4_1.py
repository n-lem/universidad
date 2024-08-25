# Lemos, Nahuel

# Ejercicio 1
# Realizar un programa que conste de una clase llamada Alumno que tenga como 
# atributos el nombre y la nota del alumno. Definir los métodos para 
# inicializar sus atributos, imprimirlos y mostrar un mensaje con el 
# resultado de la nota y si ha aprobado o no.
# ¡No utilice el constructor!

class Alumno():
    # Inicializo los atributos
    def inicializar(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    # Función para imprimir los datos
    def imprimir(self):
        print('Nombre:',self.nombre)
        print('Nota:',self.nota)

    # Función para obtener el resultado
    def resultado(self):
        if self.nota < 5:
            print(f'{self.nombre} desaprobó')
        else:
            print(f'{self.nombre} aprobó')

# Bloque principal
# Creo los nuevos objetos
alumno1 = Alumno()
alumno2 = Alumno()

# Inicializamos los atributos
alumno1.inicializar('Ivan',8)
alumno2.inicializar('Juan',4)

# Imprimimos los datos y resultados de cada alumno

alumno1.imprimir()
alumno1.resultado()

alumno2.imprimir()
alumno2.resultado()