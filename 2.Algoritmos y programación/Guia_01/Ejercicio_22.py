# Estructuras iterativas for anidadas
# 22. Escribir un programa que solicite muestre las tablas del 1 al 9 utilice for
# anidados.

# Recorro los números que serán multiplicados
for multiplicando in range(1,10):
    # Imprimo como título, el número multiplicado
    print(f'- Tabla del {multiplicando} -\n')

    # Recorro los números que van a multiplicar
    for multiplicador in range(1,11):

        # Imprimo el número que multiplicador por el multiplicando, para 
        # mostrar el producto de la multiplicación
        print(f'{multiplicador:>2} x {multiplicando} = {multiplicador * multiplicando:>2}')

    # Salto de línea
    print()
