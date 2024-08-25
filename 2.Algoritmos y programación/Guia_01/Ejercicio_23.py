# 23. . Escribir un programa muestre las tablas del 1 al 10 en formato pitagórico
# 1 2 3 4 5 6 7 8 9 10
# 2 4 6 8 10 12 14 16 18 20
# 3 6 9 12 15 18 21 24 27 30 

# Represento la fila de la tabla pitágorica
for i in range(1,11):

    # Represento la columna de la tabla pitágorica
    for j in range(1,11):

        # Muestro el elemento n-ésimo de la tabla pitágorica, que resulta de multiplicar
        # el elemento de la i-ésima fila y de la j-ésima columna.
        # El :>3 indica que cada n-ésimo elemento debe tener 3 caracteres comenzando desde
        # la derecha
        print(f'{i * j:>3}', end =' ')

    # Imprimo un salto después de completar cada i-ésima fila
    print()
