# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés
# anual y el número de años, y muestre por pantalla el capital obtenido en la
# inversión.

# Pregunto al usuario la cantidad a invertir
cantidad = float(input("Ingrese la cantidad a invertir: "))

# Pregunto al usuario el interés anual
interes_anual = float(input("Ingrese el interés anual: "))

# Pregunto al usuario el número de años
numero_anios = int(input("Ingrese el número de años: "))

# Calculamos el factor del interés anual
factor_interes = (interes_anual / 100) + 1

# Calculamos el capital obtenido en la inversión
capital_obtenido = cantidad * factor_interes ** numero_anios

# Muestro el capital obtenido en la inversión
print(f"El capital obtenido en la inversión es: ${capital_obtenido:.2f}")
