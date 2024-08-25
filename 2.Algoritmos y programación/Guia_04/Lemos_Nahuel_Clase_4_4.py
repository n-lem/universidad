# Lemos, Nahuel

# Realizar un programa en el cual se declaren dos valores enteros por teclado 
# utilizando el método __init__. Calcular después la suma, resta, multiplicación y 
# división. Utilizar un método para cada una e imprimir los resultados obtenidos. 
# Llamar a la clase Calculadora.

class Calculadora:
    # Inicailizar con el método __init__
    def __init__(self):
        self.numero1 = int(input('Ingrese el primer número: '))
        self.numero2 = int(input('Ingrese el segundo número: '))

    # Suma
    def suma(self):
        return self.numero1 + self.numero2
    
    # Resta
    def resta(self):
        return self.numero1 - self.numero2
    
    # Multiplicación
    def multiplicacion(self):
        return self.numero1 * self.numero2
    
    # División
    def division(self):
        try:
            return self.numero1 / self.numero2
        except ZeroDivisionError:
            return 'Indeterminada. No se puede dividir por cero'

    # Método para imprimir los datos
    def imprimir(self):
        print(f'La suma es: {self.suma()}')
        print(f'La resta es: {self.resta()}')
        print(f'La multiplicación es: {self.multiplicacion()}')
        print(f'La división es: {self.division()}')


# Llamo a la función
calculadora = Calculadora()
calculadora.imprimir()


