
# Estructuras de decisión doble if else
# 12. Escribir un programa que permita el ingreso de 2 dígitos, si es menor a 
# 50 debe mostrar la mitad de ese número.


# Solicito que se ingresen dos dígitos, que los leo como cadena
num1 = str(input('Ingrese un dígito: '))
num2 = str(input('Ingrese otro dígito: '))

# Uno ambos dígitos y los convierto en un numero entero
num = int(num1+num2)

# Verifico si el digito obtenido es menor a 50
if num < 50:
    # Si el número es menor a 50, lo divido a la mitad
    print(f'Al ser menor a 50 divido el {num} a la mitad.')
    num = num / 2
# Muestro el dígito obtenido
print(f'El numero final es {num}')


