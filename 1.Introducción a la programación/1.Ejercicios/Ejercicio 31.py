# Escribir un programa que permita el ingreso por teclado de una oración de cinco
# palabras, y muestras por pantalla, en minúsculas, en mayúsculas y por último solo
# el primer carácter de la oración en mayúscula.


# Solicito la oración al usuario
oracion = input("Ingrese una oración de cinco palabras: ")

# Muestra la oración en minúsculas
print("La oración en minúsculas es: " + oracion.lower())

# Muestra la oración en mayúsculas
print("La oración en mayúsculas es: " + oracion.upper())

# Muestra solo el primer carácter de la oración en mayúscula
print("El primer carácter de la oración en mayúscula es: " + oracion[0].upper())