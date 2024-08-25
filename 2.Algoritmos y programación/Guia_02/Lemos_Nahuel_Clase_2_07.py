# Alumno: Lemos, Nahuel

# Desarrollar una función que reciba un string como parámetro y nos muestre la 
# cantidad de vocales. Llamarla desde el bloque principal del programa 3 veces 
# con string distintos ingresados por teclado.


def cantidad_de_vocales(cadena):
    # Inicializo el contador en 0
    contador_de_vocales = 0
    # Uso un bucle for para recorrer cada letra de la cadena en minúsculas
    for letra in cadena.lower():
        # Uso una condición para verificar si la letra es una vocal
        if letra in 'aeiouáéíóúüAEIOUÁÉÍÓÚÜ':
            # Si se cumple la condición, incremento el valor de contador_de_vocales
            contador_de_vocales += 1
    # Imprimo el resultado del contador de vocales
    print(f'La cantidad de vocales del string \'{cadena}\' es: {contador_de_vocales}.')


# Solicito que se ingresen textos y llamo a la función
texto = str(input('Ingrese una palabra o texto: '))
cantidad_de_vocales(texto)


texto2 = str(input('Ingrese una palabra o texto: '))
cantidad_de_vocales(texto2)


texto3 = str(input('Ingrese una palabra o texto: '))
cantidad_de_vocales(texto3)