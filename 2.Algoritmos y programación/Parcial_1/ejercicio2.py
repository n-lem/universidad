from ListaORDENADA_parcial import *

#  A. Agregue a una lista ordenada(PDA), la lista de datos propuesta llamada Combinados. Muestre la lista creada.
# B. Que procedimiento debería incorporar para que la lista Combinados pueda ser ordenada por ListaORDENADA_parcial

#      Explique porque se ordenaron los elementos que son palabras, de esa forma.

# C. Explique qué función cumple el método: metodo_nuevo
# D. Realice una operación donde se ponga en práctica el método metodo_nuevo
# E. Cree un método para limpiar(eliminar) la lista creada. Muestre la lista eliminada.

lista_nueva = ListaOrdenada()

combinados = ['CUATRO', 2, 3, 'CINCO', 'SEIS', 4, 'NUEVE', 'DOS', 'CERO', 'TRES', 6, 'SIETE', 9, 5, 'UNO', 'OCHO', 1, 7, 8]

for i in combinados:
    lista_nueva.agregar(str(i))

lista_nueva.ver()

# B) Se ordenan de esa forma por la ubicación que tiene cada caracter en el código ASCII

# c) Muestra el elemento que se encuentra en la posición indicada

# D
print( lista_nueva.metodo_nuevo(8) )


# E
lista_nueva.limpiar_lista()
lista_nueva.ver()

