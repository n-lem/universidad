
# Estructuras de decisión anidadas if elif else .
# 14. Escribir un programa que permita realizar 3 cálculos aritméticos, suma, 
# resta y multiplicación.
# Las opciones deben presentarse a modo de menú de opciones , el usuario elegirá
# la operación deseada , el programa deberá verificar si el valor ingresado esta
# entre las opciones del menú , si la opción ingresada no es correcta debe mostrar
# un mensaje que diga opción incorrecta y salir del programa pero si la opción es
# correcta seguirá con el programa y se le pedirá al usuario el ingreso de dos 
# números enteros para ejecutar la operación seleccionada, luego debe mostrar la
# operación seleccionada, el desarrollo y el resultado. ejemplo :
# Menú:
# Suma (1) Resta (2) Multiplicación (3)
# opción: 1
# dato : 1
# dato : 2
# El resultado de la suma 1 + 2 = 3. 


# Creo una cadena con el mensaje del menú en una variable e imprimo el menú
menu = 'Menú:\n\t(1) Suma\n\t(2) Resta\n\t(3) Multiplicacion'
print(menu)

# Solicito que se ingrese una opción
opcion = int(input('Ingrese una opción: '))

# Verifico si la opción es válida
if opcion in [1,2,3]:
    # Solicito los valores a operar
    valor1 = int(input('Ingrese el primer valor: '))
    valor2 = int(input('Ingrese el segundo valor: '))

    # El el número ingresado es 1, entonces...
    if opcion == 1:
        # Indico la operación
        operacion = 'suma'
        # Realizo la operación
        resultado = valor1 + valor2
        # Imprimo el resultado de la operación
        print(f'El resultado de la {operacion} es: {resultado}')
    
    # El el número ingresado es 2, entonces...
    elif opcion == 2:
        # Indico la operación
        operacion = 'resta'
        # Realizo la operación
        resultado = valor1 - valor2
        # Imprimo el resultado de la operación
        print(f'El resultado de la {operacion} es: {resultado}')
    
    # El el número ingresado es 3, entonces...
    elif opcion == 3:
        # Indico la operación
        operacion = 'multiplicacion'
        # Realizo la operación
        resultado = valor1 * valor2
        # Imprimo el resultado de la operación
        print(f'El resultado de la {operacion} es: {resultado}')

# Si la opción no es válida, entonces...
else:
    # Imprimo un mensaje de error
    print('Numero ingresado incorrecto.\nFin del programa')
