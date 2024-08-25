# Escriba un programa que pida dos números y que muestre cuál es el menor y cuál
# el mayor o que muestre si son iguales.


num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if num1 < num2:
    print(f"El número menor es {num1} y el número mayor es {num2}")
elif num2 < num1:
    print(f"El número menor es {num2} y el número mayor es {num1}")
else:
    print("Los números son iguales.")