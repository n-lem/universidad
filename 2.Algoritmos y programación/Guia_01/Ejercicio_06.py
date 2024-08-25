
# Entradas input()
# 6. Escribir un programa que pregunte al usuario por el número de horas 
# trabajadas y el costo por hora. Después debe mostrar por pantalla la paga que
# le corresponde.


# Solicito que se indiquen las horas trabajadas
horas_trabajadas = int(input('Ingrese la cantidad de horas trabajadas: '))

# Solicito que se ingrese el costo por hora trabajada
costo_por_hora = float(input('Ingrese el costo por hora trabajada: '))

# Calculo el pago a recibir en función a la cantidad de horas y su costo
pago = horas_trabajadas * costo_por_hora
print('La paga correspondiente es de: $', pago)

