# 20. Escribir un programa que solicita el ingreso de una palabra, debe pasarla al
# jeringoso y mostrarla al finalizar la conversión.
# 1. Convertir la palabra a minúsculas o mayúsculas.
# 2. Utilizar un acumulador (de letras) mientras, pasa la palabra al jeringoso
# 3. Mostrarla convertida (use else).
# Definición de jeringoso: Forma festiva de hablar, que añade tras cada vocal una
# sílaba formada por una letra (p) y la misma vocal precedente. por ejemplo:
# yo no se nada
# yopo nopo sepe napadapa


# Solicito que se ingrese una palabra
palabra = str(input('Ingrese una palabra: '))
# Acumulador de letras, donde se guardarán las letras que formarán la palabra final
acumulador_letras = ''

# Recorro la palabra letra por letra
for letra in palabra:
    # Verifico si la letra ingresada es una vocal
    if letra in ['a', 'e', 'i', 'o', 'u']:
        # En caso de ser una vocal, guardo esa vocal como una letra con la vocal, la letra p y la vocal repetida
        letra = f'{letra}p{letra}'
    # Guardo las letras de la palabra
    acumulador_letras += letra

# Muestro la palabra resultante
print(acumulador_letras)