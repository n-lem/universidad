# A partir del TDA lista enlazada no ordenada, desarrolle las siguientes consignas:
# ● Crear 3 tipos de listas distintas con
#     ○ 5 Colores
#     ○ 5 Nombres
#     ○ 5 Números aleatorios desde 1990 a 2045
# ● Muestre cada una de las listas
# ● Elimine 2 elementos de cada lista. Solicite al usuario que ingrese por teclado los elementos a eliminar.
# ● Muestre cada una de las listas
# ● Agregue al final de la lista colores un color, muestre nuevamente la lista.
# ● Muestre el tamaño de la lista de Números 

class Nodo:
    def __init__(self,datoInicial):
        self.dato = datoInicial
        # None porque está vacía la lista al comienzo
        self.siguiente = None

    def obtenerDato(self):
        return self.dato

    def obtenerSiguiente(self):
        return self.siguiente
    
    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente

class ListaNoOrdenada:
    def __init__(self):
        self.cabeza = None

    def estaVacia(self):
        return self.cabeza == None

    def ver(self):
        print('Cabeza',end='->')
        if not self.estaVacia():
            
            actual = self.cabeza
            while actual != None:
                print(actual.dato, end = '->')
                actual = actual.obtenerSiguiente()
        print('None')
        return

    def agregar(self,item):
        temp = Nodo(item)
        temp.asignarSiguiente(self.cabeza)
        self.cabeza = temp

    def tamano(self):
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.obtenerSiguiente()
        return contador

    def buscar(self,item):
        actual = self.cabeza
        encontrado = False
        while actual != None and not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                actual = actual.obtenerSiguiente()
        return encontrado

    def remover(self,item):
        actual = self.cabeza
        previo = None
        encontrado = False
        while not encontrado and actual != None:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                previo = actual
                actual = actual.obtenerSiguiente()
        if actual != None:
            if previo == None:
                self.cabeza = actual.obtenerSiguiente()
        if actual != None:
            if previo == None:
                self.cabeza = actual.obtenerSiguiente()
            else:
                previo.asignarSiguiente(actual.obtenerSiguiente())

    def anexar(self,item):
        temp = Nodo(item)
        actual = self.cabeza
        previo = None
        while actual != None:
            previo = actual
            actual = actual.obtenerSiguiente()

        if previo == None:
            self.agregar(item)
        else:
            temp = Nodo(item)
            previo.asignarSiguiente(temp)



# Instanciamos las tres listas diferentes
listaColores = ListaNoOrdenada()
listaNombres = ListaNoOrdenada()
listaNumeros = ListaNoOrdenada()

# Mostramos las lista

# listaColores
listaColores.anexar('verde')
listaColores.anexar('azul')
listaColores.anexar('rojo')
listaColores.anexar('gris')
listaColores.anexar('rosado')

# listaNombres
listaNombres.anexar('Pedro')
listaNombres.anexar('Maximiliano')
listaNombres.anexar('Noelia')
listaNombres.anexar('María')
listaNombres.anexar('Juan')

# listaNumeros
import random
for item in range(5):
    listaNumeros.anexar(random.randint(1990,2045))

print('Listados\n')
listaColores.ver()
listaNombres.ver()
listaNumeros.ver()



print('\nDatos a Eliminar\n')



# Elimino dos elementos de cada lista
# listaColores
for _ in range(2):
    eliminarColor = input('Ingrese el color a eliminar: ').lower()
    listaColores.remover(str(eliminarColor))

# listaNombres
for _ in range(2):
    eliminarNombre = input('Ingrese el nombre a eliminar: ').capitalize()
    listaNombres.remover(str(eliminarNombre))

# listaNumeros
for _ in range(2):
    eliminarNumero = int(input('Ingrese el número a eliminar: '))
    listaNumeros.remover(eliminarNumero)



print('\nListados\n')
listaColores.ver()
listaNombres.ver()
listaNumeros.ver()



# Agregue al final de la lista colores un color, muestre nuevamente la lista.



print('\nAnexando un color\n')

listaColores.anexar('amarilo')
listaColores.ver()


# Mostrar tamaño
print(f'\nEl tamaño de la lista de números es: {listaColores.tamano()}')
