# Escribir un programa que nos muestre si es hora de desayunar, almorzar,
# merendar o cenar dependiendo de la hora ingresada, según el siguiente listado.
# 10 Desayuno
# 13 Almuerzo
# 17 Merienda
# 21 cena

hora = int(input("Ingrese la hora: "))

if hora == 10:
    print("Desayunar")
elif hora == 13:
    print("Almorzar")
elif hora == 17:
    print("Merienda")
elif hora == 21:
    print("Cena")