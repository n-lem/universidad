

# 10. Escribir un programa que solicite la fecha de nacimiento en formato 
# “dd/mm/aaaa” , y muestre por pantalla la fecha por separado el día, el mes y 
# el año.


# Pido que se ingrese una fecha en el formato dd/mm/aaaa
fecha_de_nacimiento = str(input('Ingrese la fecha de nacimiento en formato dd/mm/aaaa: '))

# Para el día, tomo desde el primer dígito hasta llegar al segundo índice, es decir,
# tomo las dos primeras posiciones
dia = fecha_de_nacimiento[:2]

# Para el mes, tomo la tercera y cuarta posición
mes = fecha_de_nacimiento[3:5]

# Para el mes, tomo desde la sexta hasta el final
anio = fecha_de_nacimiento[6:]

# Imprimo cada valor tomado
print(f'Día de nacimiento: {dia}')
print(f'Mes de nacimiento: {mes}')
print(f'Año de nacimiento: {anio}')

