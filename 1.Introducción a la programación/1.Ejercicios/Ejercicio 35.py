# Escribir un programa que permita que permita ingresar su año de nacimiento sin
# decimales, y calcular SI ya pasaron 18 años, si ya pasaron 18 años, mostrar
# cuantos años pasaron desde que cumplio los 18 años junto al mensaje que diga:
# “Ud es mayor de edad hace: ......años, porque este año usted tendrá .... años".
# Indique la finalización del programa



# Solicito el año de nacimiento al usuario
año_nacimiento = int(input("Ingrese su año de nacimiento: "))

# Calculo la edad actual
edad_actual = 2023 - año_nacimiento

# Calculo cuantos años pasaron desde que cumplio los 18 años
años_pasados = (2023 - año_nacimiento) - 18

# Verifico si ya pasaron 18 años
if edad_actual >= 18:
    print(f"Ud es mayor de edad hace: {años_pasados} años, porque este año usted tendrá {edad_actual} años.")

# Fin del programa
print("El programa ha finalizado.")