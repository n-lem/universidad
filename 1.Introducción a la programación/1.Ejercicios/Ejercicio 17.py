# Escribir un programa que muestre por pantalla, el resultado de 27 dividido 5 y el
# resto de esa división (recuerde cómo se calcula el resto, busque el operador de
# Python en la guía de estudio), almacene cada valor en una variable distinta.

dividendo = 27
divisor = 5

# Calculando el cociente
cociente = dividendo // divisor

# Calculando el resto
resto = dividendo - (cociente * divisor)

print(f"Resto: {resto}")