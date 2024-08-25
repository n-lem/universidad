# Escribir un programa que muestre la sucesión de Fibonacci.
# En matemáticas, la sucesión de fibonacci es una sucesión infinita de números
# naturales, donde el siguiente número es calculado sumando los dos números
# anteriores.
# Empiece a partir del 1 y termine cuando sea mayor a 200

a, b = 0, 1

while b <= 200:
    print(b)
    a, b = b, a + b