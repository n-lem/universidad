# Alumno: Lemos, Nahuel

# Desarrollar un programa que permita ingresar el lado de un cuadrado. Luego 
# preguntar si quiere calcular y mostrar su perímetro o su superficie.


def calcular_perimetro_o_superficie(lado, calcular):

    # Verificar si el valor a calcular es 's' o 'S'
    if calcular.lower() == 's':
        # Calculo la superficie de un cuadrado
        superficie = lado ** 2
        # Imprimo el resultado de la superficie
        print(f'La superficie es: {superficie}')

    # Si no se cumple la primera condición, verificar si el valor de calcular es 'p' o 'P'
    elif calcular.lower() == 'p':
        # Si se cumple la condición, calculo el perímetro de un cuadrado
        perimetro = lado * 4
        # Imprimo el resultado del perímetro
        print(f'El perímetro es: {perimetro} ')

    # Si no se cumple ninguna de las condiciones anteriores, imprimo un mensaje de error
    else:
        print('Opción incorrecta.')


# Solicito que se ingresen los datos
lado = float(input('Ingrese el lado de un cuadrado: '))
calcular = str(input('¿Querés calcular la (s)uperficie o el (p)erímetro?: '))



calcular_perimetro_o_superficie(lado, calcular)