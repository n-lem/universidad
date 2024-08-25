# Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con 
# el nombre tabla-n.txt la tabla de multiplicar de ese número. Donde n es el número introducido. 
# Guarde en el archivo tabla-n.txt la tabla resuelta de n.

def tabla():
    # Mientras sea verdadero se ejecuta el bucle
    while True:
        try:
            # Pido al usuario que ingrese un número entero entre 1 y 10
            n = int(input('Ingrese un número entero entre 1 y 10: '))

            # Verifico si el número ingresado está dentro del rango permitido
            if n < 1 or n > 10:
                print('El número debe estar entre 1 y 10')
                print()
            else:

                # Abro el archivo con el nombre 'tabla-n.txt', donde 'n' es el número ingresado
                with open(f'tabla-{n}.txt', 'w') as archivo:

                    # Se escribe la tabla de multiplicar del número ingresado en el archivo
                    for multiplicando in range(1, 11):
                        producto = n * multiplicando
                        archivo.write(f'{n} x {multiplicando} = {producto}\n')

                    # Se muestra un mensaje indicando que la tabla de multiplicar se ha guardado en el archivo
                    print(f'La tabla de multiplicar de {n} se ha guardado en el archivo tabla-{n}.txt')
                    
                    # Finalizo el bucle
                    break
        except Exception:
            # Se muestra un mensaje de error si se ingresa un caracter no válido
            print('Ingresá un valor válido.')
            print()

# Ejecuto el programa
tabla()
