# Lemos, Nahuel

# Desarrollar un programa que cargue los datos de un triángulo. Implementar
# una clase con los métodos para inicializar los atributos, imprimir el valor
# del lado con un tamaño mayor y el tipo de triángulo que es (equilátero,
# isósceles o escaleno).


class Triangulo:
    # Inicializar con el método __init__
    def __init__(self,lado1,lado2,lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    # Imprimo los datos
    def imprimir(self):
        print('Lado 1:', self.lado1)
        print('Lado 2:', self.lado2)
        print('Lado 3:', self.lado3)

    # Imprimo el mayor
    def mayor(self):
        if self.lado1 >= self.lado2 and self.lado1 >= self.lado3:
            print(f'El lado mayor es el lado 1 con una medida de: {self.lado1}')
        elif self.lado2 >= self.lado1 and self.lado2 >= self.lado1:
            print(f'El lado mayor es el lado 2 con una medida de: {self.lado2}')
        else:
            print(f'El mayor es el lado 3 con {self.lado3}')

    # Método para calcular el tipo de triángulo
    def tipo_de_triangulo(self):
        if self.lado1 == self.lado2 and self.lado2 == self.lado3:
            print('Es un triángulo equilátero')
        elif self.lado1 == self.lado2 or self.lado2 == self.lado3 or self.lado1 == self.lado3:
            print('Es un triángulo isósceles')
        else:
            print('Es un triángulo escaleno')

# Bloque principal

triangulo = Triangulo(45,50,90)
triangulo.imprimir()
triangulo.mayor()
triangulo.tipo_de_triangulo()