divisor = 1
acumulador = 0
listado_numeros = []

while True:
    try:
        # Agrego un bloque try-except para manejar excepciones
        numero = int(input("Ingrese un numero para calcular y mostrar sus divisores: "))
        # Convierto el valor ingresado por el usuario a un entero
        if numero >= 0:
            print(f"Los numeros divisores de {numero} son:")
            while divisor <= numero:
                if numero % divisor == 0:
                    acumulador += divisor
                    listado_numeros.append(divisor)
                divisor += 1
            break
        else:
            print("Debe ingresar un valor numérico entero positivo")
    except ValueError:
        # Manejo la excepción ValueError en caso de que el usuario ingrese un valor no numérico
        print("Debe ingresar un valor numérico entero positivo")

for i in range(len(listado_numeros)):
    print(f"{listado_numeros[i]:^30d}")
    # Se corrige el índice de listado_numeros para evitar un error de índice fuera de rango
print(f"La suma de todos los divisores es de {acumulador}")
