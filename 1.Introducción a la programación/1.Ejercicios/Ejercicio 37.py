# Escribir un programa permita el ingreso de una letra, el programa debe mostrar
# un aviso si la letra es vocal o consonante.


# Solicito la letra al usuario
letra = input("Ingrese una letra: ").lower()

# Verifico si la letra es vocal o consonante
if letra in ['a', 'e', 'i', 'o', 'u']:
    print("La letra ingresada es una vocal.")
else:
    print("La letra ingresada es una consonante.")