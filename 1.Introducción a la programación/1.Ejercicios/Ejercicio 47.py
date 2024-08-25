# Escribir un programa que pregunte al usuario cuantos años cumplió o cumplirá
# este año
# a. Debe calcular el año de nacimiento, teniendo en cuenta el año actual.
# b. Debe mostrar por pantalla el año de nacimiento y los años que ha cumplido
# cada año hasta la edad actual.
# Ejemplo:
# 2017 - 0 años
# 2018 - 1 años
# 2019 - 2 años
# 2020 - 3 años
# 2021 - 4 años
# 2022 - 5 años
# 2023 - 6 años

# Librería para obtener el año actual
import datetime

# Obtengo el año actual
anio_actual = datetime.datetime.now().year

# Preguntar al usuario su edad
edad = int(input("¿Cuántos años cumpliste o cumplirás este año? "))

# Calcular el año de nacimiento
anio_nacimiento = anio_actual - edad

# Mostrar el año de nacimiento y los años cumplidos cada año
for i in range(edad):
    match i:
        case 0:
            print(f"{anio_nacimiento + i} - {i} años")
        case _:
            print(f"{anio_nacimiento + i} - {i} años")

print(f"Naciste en el año {anio_nacimiento}")