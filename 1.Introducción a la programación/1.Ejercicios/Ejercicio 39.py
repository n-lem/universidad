# Escribir un programa que permita calcular la suma de tres números enteros
# ingresados por teclado. Si el resultado es mayor a 50 dividir por 2 , En caso
# contrario elevar el resultado al cubo, si al calcular el cubo el resultado es superior
# a 5000 deberá mostrar por pantalla “Este es un gran número”


num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

suma = num1 + num2 + num3

if suma > 50:
    resultado = suma / 2
    print(f"El resultado es {resultado}")
elif suma ** 3 > 5000:
    print("Este es un gran número.")
