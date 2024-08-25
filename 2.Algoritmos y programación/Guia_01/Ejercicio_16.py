# 16. Escribir un programa que pida al usuario un número entero positivo y muestre
# por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
# (Investigue cómo mostrar datos con print en la misma línea de texto), Si se anima
# trate de no imprimir la última coma después del 0.
# Ejemplo: 5
# 5,4,3,2,1,0,
# 5,4,3,2,1,0


# Solicito que se ingrese un número positivo
inicio = int(input('Ingrese un número entero positivo desde el cual empezar la cuenta regresiva: '))

# Recorro el buclo desde el número ingresado hasta el 1
while inicio >= 1:
    # Imprimo el número obtendio y agrego un coma al final
    print(inicio, end = ', ')
    # Por cada vuelta resto una unidad
    inicio = inicio - 1

# Imprimo el cero como último dígito de la cuenta regresiva
print('0')