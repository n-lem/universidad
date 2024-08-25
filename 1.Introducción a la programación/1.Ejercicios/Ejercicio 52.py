# Escribir un programa que solicite una frase al usuario y luego una letra, usando
# while y lo aprendido sobre string en las clases anteriores, acceso a cada carácter
# de una cadena por medio del elemento palabra[0], (no use IN).
# Buscar si la letra que ingresó se encuentra en la frase solicitada.
# Cuente cuántas veces está esa letra dentro de la frase
# - Sí, esta mostrará un mensaje que diga “letra ... encontrada aparece ...
# veces.
# - Si no está mostrara “Letra ... no encontrada en la frase”
# Luego de resolver debe preguntar al usuario si quiere salir debe ingresar una letra
# “S” o si presiona cualquier otra letra continuará.

while True:
    # Solicitar la frase al usuario
    frase = input("Ingresa una frase: ")

    # Solicitar la letra al usuario
    letra = input("Ingresa una letra: ")

    # Inicializar el contador de la letra
    contador = 0

    # Recorrer la frase carácter por carácter
    i = 0
    while i < len(frase):
        if frase[i] == letra:
            contador += 1
        i += 1

    # Mostrar el resultado
    if contador > 0:
        print(f"La letra '{letra}' se encuentra {contador} veces en la frase.")
    else:
        print(f"La letra '{letra}' no se encuentra en la frase.")

    # Preguntar si el usuario quiere salir
    salir = input("Presiona 'S' para salir, cualquier otra tecla para continuar: ")
    if salir.upper() == "S":
        print("¡Hasta luego!")
        break