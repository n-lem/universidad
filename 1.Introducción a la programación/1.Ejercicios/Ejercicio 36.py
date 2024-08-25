# Escribir un programa que diferencie entre verdadero y falso, el usuario podrá
# ingresar un número entre 0 y 1, y el programa debe imprimir por pantalla si el
# número es falso o verdadero según lo visto en clases. Pista (True,False).

auxiliar = True
# Solicito el número al usuario
numero = int(input("Ingrese un número entre 0 y 1: "))

# Verifico si el número es verdadero o falso
if auxiliar == numero:
    print("El número ingresado es verdadero")
else:
    print("El número ingresado es falso")

