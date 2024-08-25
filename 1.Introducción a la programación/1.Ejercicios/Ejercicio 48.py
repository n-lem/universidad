# Escribir un programa que pida al usuario un número entero positivo y muestre por
# pantalla la cuenta atrás desde ese número hasta cero separados por comas.
# (Investigue cómo mostrar datos con print en la misma línea de texto), Si se anima
# trate de no imprimir la última coma después del 0.
# Ejemplo: 5
# Esta bien
# 5,4,3,2,1,0,
# Está mejor...
# 5,4,3,2,1,0

num = int(input("Ingresa un número entero positivo: "))

for i in range(num, -1, -1):
    match i:
        case 0:
            print(i, end="")
        case _:
            print(i, end=",")