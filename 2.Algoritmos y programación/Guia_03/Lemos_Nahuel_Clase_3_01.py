# Lemos, Nahuel

# Dado el siguiente programa trate de resolver cualquier error que pueda 
# producirse al ejecutarlo, resuelva con excepcione

try:
    # Se inicialia las variables resultado y menor
    resultado = 0
    menor = 0
    
    # Pido al usuario que ingrese dos números
    numero_1 = int(input("Escriba un número: "))
    numero_2 = int(input("Escriba otro número: "))
    
    # Comparo los dos números para ver si son iguales o cuál es menor
    if numero_1 == numero_2:
        print("Los dos números son iguales.")
    elif numero_1 < numero_2:
        print(f"El número {numero_1} es menor que {numero_2}")
        menor = numero_1
    else:
        print(f"El número {numero_2} es menor que {numero_1}")
        menor = numero_2
    
    # Caldulo el resultado de multiplicar los dos números
    resultado = numero_2 * numero_1
    print(f"El resultado entre {numero_1} * {numero_2} = {resultado}")
    
    # Imprimo todos los números entre el menor y el resultado
    for i in range(menor, resultado + 1):
        print(i)



