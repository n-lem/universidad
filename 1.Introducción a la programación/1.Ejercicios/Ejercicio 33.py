# Escribir un programa que permita el ingreso de 2 digitos, si es menor a 20 debe
# mostrar la mitad de ese número.


# Solicito los digitos al usuario
digito1 = int(input("Ingrese el primer digito (1-9): "))
digito2 = int(input("Ingrese el segundo digito (0-9): "))

# Valido si es menor a 20
if digito1 * 10 + digito2 < 20:
    # Calcula la mitad del numero
    mitad = (digito1 * 10 + digito2) / 2

    # Muestra la mitad
    print("La mitad del numero es: " + str(mitad))