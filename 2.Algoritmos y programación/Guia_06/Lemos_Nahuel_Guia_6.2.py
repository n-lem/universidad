# A partir del TDA lista enlazada ordenada debe generar una lista de 1000 números, los
# números deben ser ingresados aleatoriamente desde el número 5 al 300.
# Utilice ciclos para el ingreso de los números.
# muestre la lista una vez finalizada la carga

# La clase nodo es igual para lista ordenada y no ordenada
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


# Clase para listas ordenadas
class ListaOrdenada:
    
    # Se mantiene igual
    def __init__(self):
        self.cabeza = None

    # Se mantiene igual
    def estaVacia(self):
        return self.cabeza == None

    # Se mantiene igual
    def tamano(self):
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.obtenerSiguiente()
        return contador

    # Se mantiene igual
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

    # Se mantiene igual
    def ver(self):
        print('Cabeza',end='->')
        if not self.estaVacia():
            actual = self.cabeza
            while actual != None:
                print(actual.dato, end = '->')
                actual = actual.obtenerSiguiente()
        print('None')
        return


    # Cambian las funciones de abajo


    def buscar(self,item):
        actual = self.cabeza
        encontrado = False
        detenerse = False # Linea nueva
        while actual != None and not encontrado and not detenerse: # and not deterse se agrega
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                # Se modifica el else
                if actual.obtenerDato() > item:
                    detenerse = True
                else:
                    actual = actual.obtenerSiguiente()
        return encontrado

    def agregar(self,item):
        # Se agregan estas líneas
        actual = self.cabeza
        previo = None
        detenerse = False
        while actual != None and not detenerse:
            if actual.obtenerDato() > item:
                detenerse = True
            else:
                previo = actual
                actual = actual.obtenerSiguiente()
        
        temp = Nodo(item) # Se mantiene
        if previo == None:
            temp.asignarSiguiente(self.cabeza)
            self.cabeza = temp
        else:
            temp.asignarSiguiente(actual)
            previo.asignarSiguiente(temp)




# A partir del TDA lista enlazada ordenada debe generar una lista de 1000 números, los
# números deben ser ingresados aleatoriamente desde el número 5 al 300.
# Utilice ciclos para el ingreso de los números.
# muestre la lista una vez finalizada la carga


# Instanciamos milista
milista = ListaOrdenada()

print('Muestro la lista vacía:\n')

milista.ver()

# Importo la librería random
import random

print('\nCargando los datos\n')

# Agregamos nodos y datos
for _ in range(1000):
    milista.agregar(random.randint(5,300))

# Mostramos la lista
milista.ver()
