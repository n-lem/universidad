# Lemos, Nahuel

# Ejercicio 2
# Realizar un programa que tenga una clase Persona con las siguientes
# características. La clase tendrá como atributos el nombre y la edad de una
# persona. Implementar los métodos necesarios para inicializar los atributos
# utilizando el constructor (__init__), mostrar los datos e indicar si la 
# persona es mayor de edad o no.
# ¡Utilice el constructor!

class Persona():
    # Inicializo con el método __init__, es el constructor, me facilita el ingreso de datos
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    # Imprimo los datos
    def imprimir(self):
        print('Nombre:',self.nombre)
        print('Edad:',self.edad)

    # Compruebo si es mayor de edad o no
    def mayor_edad(self):
        if self.edad >= 18:
            print(f'{self.nombre} es mayor de edad')
        else:
            print(f'{self.nombre} no es mayor de edad')

# Bloque principal
persona1 = Persona('Ivan',23)
persona2 = Persona('Carlos',17)

# Imprimo los datos y compruebo si es mayor de edad
persona1.imprimir()
persona1.mayor_edad()

persona2.imprimir()
persona2.mayor_edad()


