# Escribir un programa que permita que permita ingresar una nota numérica entre 1
# y 10,(utilizar 3 condicionales simples).

# Condiciones                     Mensajes por pantalla
# Si la nota está entre 1 y 3     desaprobó
# Si la nota está entre 4 y 6     aprobó
# Si la nota es 7 o más           promociono


# Solicito la nota al usuario
nota = float(input("Ingrese su calificación (1-10): "))

# Valido la nota según las condiciones
if nota < 4:
    print("Desaprobó")
elif 4 <= nota < 7:
    print("Aprobó")
else:
    print("Promociono")
