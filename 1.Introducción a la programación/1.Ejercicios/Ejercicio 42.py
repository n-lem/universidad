# Escriba un programa que pida dos números y que muestre cuál es el menor y cuál
# el mayor o que muestre si son iguales.
# usar un if y match case

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

match (num1, num2):
    case (num1, num2) if num1 < num2:
        print(f"El número {num1} es el menor y el número {num2} es el mayor.")
    case (num1, num2) if num1 > num2:
        print(f"El número {num2} es el menor y el número {num1} es el mayor.")
    case (num1, num2) if num1 == num2:
        print(f"Los números {num1} y {num2} son iguales.")