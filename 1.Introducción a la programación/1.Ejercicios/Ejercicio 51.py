# Escribir un programa que muestre un menú con las siguientes opciones:
# a. Suma.
# b. Multiplicación
# c. Largo de Palabras
# d. Salir.
# Funcionamiento:
# - El usuario debe ver el menú de opciones todo el tiempo.
# - Si elige la opción a:
# * debe solicitar 2 números, sumarlos y mostrarlos.
# - Si elige la opción b
# * Debe solicitar 2 números, multiplicarlos y mostrarlos.
# - Si elige la opción c,
# * Debe solicitar dos palabras y mostrar la palabra más larga, avisar cuando
# sean iguales.en ambos casos debe mostrar el largo de cada una
# - Si elige la opción d
# * Debe salir y despedir al usuario.

while True:
    print("Selecciona una opción:")
    print("a. Suma")
    print("b. Multiplicación")
    print("c. Largo de Palabras")
    print("d. Salir")

    opcion = input("Ingresa tu selección (a/b/c/d): ")

    match opcion:
        case "a":
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            print(f"La suma de {num1} y {num2} es: {num1 + num2}")
        case "b":
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            print(f"La multiplicación de {num1} y {num2} es: {num1 * num2}")
        case "c":
            palabra1 = input("Ingresa la primera palabra: ")
            palabra2 = input("Ingresa la segunda palabra: ")
            largo1 = len(palabra1)
            largo2 = len(palabra2)
            if largo1 > largo2:
                print(f"La palabra más larga es '{palabra1}' con {largo1} letras.")
            elif largo2 > largo1:
                print(f"La palabra más larga es '{palabra2}' con {largo2} letras.")
            else:
                print(f"Las palabras '{palabra1}' y '{palabra2}' tienen el mismo largo ({largo1} letras).")
        case "d":
            print("¡Hasta luego!")
            break
        case _:
            print("Opción inválida. Intenta de nuevo.")