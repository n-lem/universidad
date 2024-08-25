# Escribir un programa que permita realizar 3 cálculos aritméticos, suma, resta y
# multiplicación. Las opciones deben presentarse a modo de menú de opciones , el
# usuario elegirá la operación deseada , el programa deberá verificar si el valor
# ingresado está entre las opciones del menú , si la opción ingresada no es correcta
# debe mostrar un mensaje que diga opción incorrecta y salir del programa pero si
# la opción es correcta seguirá con el programa y se le pedirá al usuario el ingreso
# de dos números enteros para ejecutar la operación seleccionada, luego debe
# mostrar la operación seleccionada, el desarrollo y el resultado.


while True:
    print("Selecciona la operación que deseas realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")

    opcion = input("Ingresa el número de la opción (1-4): ")

    if opcion == "1":
        num1 = int(input("Ingresa el primer número: "))
        num2 = int(input("Ingresa el segundo número: "))
        resultado = num1 + num2
        print(f"La suma de {num1} y {num2} es: {resultado}")
    elif opcion == "2":
        num1 = int(input("Ingresa el primer número: "))
        num2 = int(input("Ingresa el segundo número: "))
        resultado = num1 - num2
        print(f"La resta de {num1} y {num2} es: {resultado}")
    elif opcion == "3":
        num1 = int(input("Ingresa el primer número: "))
        num2 = int(input("Ingresa el segundo número: "))
        resultado = num1 * num2
        print(f"La multiplicación de {num1} y {num2} es: {resultado}")
    else:
        print("Opción incorrecta.")
        break