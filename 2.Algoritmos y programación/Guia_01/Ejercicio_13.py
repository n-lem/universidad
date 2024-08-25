
# 13. Escribir un programa que permita calcular la suma de tres números enteros
# ingresados por teclado. Si el resultado es mayor a 50 dividir por 2 ,En caso 
# contrario elevar el resultado al cubo, si al calcular el cubo el resultado es
# superior a 5000 deberá mostrar por pantalla “Este es un gran número”

# Llamo a la función auxiliar
ejercicio(13)

# Solicito que se ingresen tres números
num1 = int(input('Ingrese un número: '))
num2 = int(input('Ingrese otro número: '))
num3 = int(input('Ingrese un último número: '))

# Sumo los tres números ingresados por teclado e imprimo su suma
num = num1 + num2 + num3
print(f'La suma de los números es {num}.')

# Evalúo si la suma de los números es mayor a 50
if num > 50:
    # Si es mayor a 50, lo divido a la mitad e imprimo su resultado
    print(f'Como {num} es mayor a 50 lo divido por dos.')
    num = num / 2
    print(f'Obtengo {num}')
else:
    # Si es menor a 50, lo elevo al cubo e imprimo un mensaje con el número
    num = num ** 3
    print(f'Como es menor a 50, lo elevo al cubo y obtengo {num}.')
    if num > 5000:
        # Muestro el mensaje de que es un gran número
        print('Este es un gran número.')
