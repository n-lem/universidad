# Escribir un programa que pida al usuario una palabra, debe mostrarla 10 veces,
# junto al número correspondiente.
# Ejemplo:
# 1 hola
# 2 hola

palabra = input("Ingresa una palabra: ")

for i in range(1, 11):
    match i:
        case 1:
            print(f"{i} {palabra}")
        case 2:
            print(f"{i} {palabra}")
        case 3:
            print(f"{i} {palabra}")
        case 4:
            print(f"{i} {palabra}")
        case 5:
            print(f"{i} {palabra}")
        case 6:
            print(f"{i} {palabra}")
        case 7:
            print(f"{i} {palabra}")
        case 8:
            print(f"{i} {palabra}")
        case 9:
            print(f"{i} {palabra}")
        case 10:
            print(f"{i} {palabra}")