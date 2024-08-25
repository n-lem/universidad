# Alumno: Lemos, Nahuel

# Confeccionar una función que reciba tres enteros y nos muestre el mayor de 
# ellos. La carga de los valores se hace por teclado.


def mayor(a, b, c):
    # Verifico si a es mayor que b
    if a > b:
        # Si se cumple la condición, verifico si a es mayor que c
        if a > c:
            # Imprimo que a es el mayor de los tres
            print(f'El mayor de los tres es {a}')
        # Si no se cumple la condición, imprimo que c es el mayor de los tres
        else:
            print(f'El mayor de los tres es {c}')

    # Si no se cumple la primera condición, verifico si b es mayor que a
    elif b > a:
        # Si se cumple la condición, verifico si b es mayor que c
        if b > c:
            # Imprimo que b es el mayor de los tres
            print(f'El mayor de los tres es {b}')
        # Si no se cumple la condición, imprimo que c es el mayor de los tres
        else:
            print(f'El mayor de los tres es {c}')

# Solicito que se ingresen tres valores
num1 = int(input('Ingrese el primer valor entero: '))
num2 = int(input('Ingrese el segundo valor entero: '))
num3 = int(input('Ingrese el tercer valor entero: '))

mayor(num1, num2, num3)