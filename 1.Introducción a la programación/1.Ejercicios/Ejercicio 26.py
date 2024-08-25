# Escribir un programa que solicite al usuario el ingreso por teclado de su altura
# en metros con decimales, y muestre por pantalla la altura expresada en metros
# incluir la palabra metros y la altura expresada en centímetros incluir la palabra
# centímetros.
# Ejemplo: ingresa: 1.80
# Resultado ud mide 1.80 metros o 180 centímetros

# Solicito al usuario el ingreso de la altura en metros con decimales
altura_metros = float(input("Ingrese su altura en metros con decimales: "))
altura_centimetros = altura_metros * 100

# Muestro la altura expresada en metros y centímetros
print(f"Ud mide {altura_metros} metros o {altura_centimetros} centímetros")