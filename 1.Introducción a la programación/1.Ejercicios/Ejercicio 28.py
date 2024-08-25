# Escribir un programa que muestre su primer nombre al derecho y al revés,
# accediendo caracter por caracter. También debe mostrar el número del último
# índice.


# Leo el nombre del usuario
nombre = input("Ingrese su nombre: ")

# Muestro su nombre al derecho
print("Nombre al derecho:")
for i in range(len(nombre)):
    print(nombre[i], end="")
print()

# Muestro el número del último índice
ultimo_indice = len(nombre) - 1
print("Número del último índice:", ultimo_indice)

# Muestro su nombre al revés
print("Nombre al revés:")
for i in range(len(nombre) - 1, -1, -1):
    print(nombre[i], end="")
print()

# Muestro la cantidad de caracteres
# print("Cantidad de caracteres:", len(nombre))