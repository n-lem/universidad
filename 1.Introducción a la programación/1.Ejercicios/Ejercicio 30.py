# Escribir
# un programa que solicite la fecha de nacimiento en formato
# “dd/mm/aaaa”, y muestre por pantalla la fecha por separado el día,el mes y el año.
# Ejemplo: El usuario ingresa “23/08/2022” el programa debe mostrar:
# “ Día:23 - Mes:08 - Año:2022 ”.


# Solicito la fecha de nacimiento al usuario
fecha_nacimiento = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ")

# Separo los elementos de la fecha de nacimiento
dia = fecha_nacimiento[:2]
mes = fecha_nacimiento[3:5]
anio = fecha_nacimiento[6:]

# Muestro la fecha por separado el día, el mes y el año
print("Día:", dia, "- Mes:", mes, "- Año:", anio)