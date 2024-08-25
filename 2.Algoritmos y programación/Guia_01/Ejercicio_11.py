# Estructuras de decisión simple if
# 11. Escribir un programa que permita el ingreso por teclado de una oración de
# cinco palabras, y muestre por pantalla, en minúsculas, en mayúsculas y por 
# último solo el primer carácter de la oración en mayúscula.


# Solicito que se ingrese una oracion de 5 palabras
oracion = str(input('Ingrese una oracion de 5 palabras: '))

# Imprimo la oración en minúsculas
print(oracion.lower())

# Imprimo la oración en mayúsculas
print(oracion.upper())

# Imprimo en mayúsculas el último caracter de la oración
print(oracion[-1:].upper())

