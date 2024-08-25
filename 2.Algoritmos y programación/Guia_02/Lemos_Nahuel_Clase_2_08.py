# Alumno: Lemos, Nahuel

# Confeccionar una función que reciba tres enteros y los muestre ordenados de 
# menor a mayor. En otra función solicitar la carga de 3 enteros por teclado y 
# proceder a llamar a la primera función definida.


def ordenar_de_menor_a_mayor(num1, num2, num3):
    # Se imprime el mensaje
    print('\nLos números ordenados de menor a mayor son: ', end='')

    # Verifico si num1 es el menor de los tres números
    if num1 <= num2 and num1 <= num3:
        #Verificar si num2 es menor o igual que num3
        if num2 <= num3:
            # Si se cumple la condición, imprimo num1, num2 y num3 en ese orden
            print(num1, num2, num3)
        # Si no se cumple la condición, imprimo num1, num3 y num2 en ese orden
        else:
            print(num1, num3, num2)

    # Verifico si num2 es el menor de los tres números
    elif num2 <= num1 and num2 <= num3:
        # Verifico si num1 es menor o igual que num3
        if num1 <= num3:
            # Si se cumple la condición, imprimo num2, num1 y num3 en ese orden
            print(num2, num1, num3)
        # Si no se cumple la condición, imprimo num2, num3 y num1 en ese orden
        else:
            print(num2, num3, num1)

    # Verifico si num1 es menor o igual que num2
    elif num1 <= num2:
        # Si se cumple la condición, imprimo num3, num1 y num2 en ese orden
        print(num3, num1, num2)
    # Si no se cumple la condición, imprimo num3, num2 y num1 en ese orden
    else:
        print(num3, num2, num1)


def pedir_enteros():
    # Pido que se ingresen tres números y los devuelvo en tres variables
    num1 = int(input('Ingrese el primer entero: '))
    num2 = int(input('Ingrese el segundo entero: '))
    num3 = int(input('Ingrese el tercer entero: '))
    return num1, num2, num3


a,b,c = pedir_enteros()
ordenar_de_menor_a_mayor(a, b, c)

