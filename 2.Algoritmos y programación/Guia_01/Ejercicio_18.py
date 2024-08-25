# Estructura iterativa FOR
# 18. Escribir un programa que solicite una palabra y la muestre letra por letra
# separada por un guión, en una misma línea de texto ( renglón) , use “end”.
# por ejemplo:
# azul
# a-z-u-l-


# Solicito que se ingrese una palabra
palabra = str(input('Ingrese una palabra: '))

# Recorro la palabra letra por letra
for letra in palabra:
    # Imprimo cada letra separada por guión
    print(letra, end = '-')
# Imprimo un espacio vacío
print()