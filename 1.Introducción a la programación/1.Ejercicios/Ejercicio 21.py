# Escribir un programa que pregunte al usuario por el número de horas trabajadas y
# el costo por hora. Después debe mostrar por pantalla la paga que le corresponde.

# Pregunto al usuario por el número de horas trabajadas
horas_trabajadas = int(input("Ingrese el número de horas trabajadas: "))

# Pregunto al usuario por el costo por hora
costo_por_hora = float(input("Ingrese el costo por hora: "))

# Calculo el pago
paga = horas_trabajadas * costo_por_hora

# Muestro el pago por pantalla
print(f"La paga correspondiente a {horas_trabajadas} horas trabajadas con un costo por hora de {costo_por_hora} es: ${paga}")