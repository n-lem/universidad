# 17. Escribir un programa que muestre números del 0 al 30 uno debajo de otro.
# ● Cuando los números sean 3, 8, 17, 26 debe mostrar el mensaje “saltando instrucciones 
# con(xxxxxxxxxxxxx el nombre de la instrucción que permite realizar saltos en un bucle) 
# llegue al número 3 o 8 o 17 o 26 ”
# ● Cuando los números sean mayor a 25 debe preguntar si continúa o sale del conteo (por 
# ejemplo presione Presione: 'S' para salir , cualquier otra tecla para continuar)
# ○ Si presiona cualquier tecla el programa seguirá su curso
# ○ Si presiona S, terminará el programa, antes de terminar debe mostrar a qué número de 
# conteo llegó .


# Valor de inicio y final
valor = 0
final = 30

# Mientras el número de inicio sea menor al número del final, se repite el ciclo
while valor <= final:


    # Verifico si el número es 3, 8, 17 o 26
    if valor in [3, 8, 17, 26]:
        # Muestro un mensaje
        print('Saltando instrucciones con \'continue\' llegué al numero 3, 8, 17 o 26.')
        # Incremento el valor en 1 dígito
        valor += 1
        # Utilizo continue para saltar las instrucciones
        continue

    # Verifico si el valor es mayor a 25
    if valor > 25:
        # Si el valor es mayor a 25, entonces le digo a usuario que si presiona 's' puede salir
        opcion = str(input('Ingrese \'S\' para salir o cualquier tecla para continuar.'))
        # Verifico si la opción ingresada es 'S' o 's'
        if opcion.lower() == 's':
            # En caso de ser 'S' o 's' muestro un mensaje
            print(f'Se llegó al número {valor}')
            # En caso de ser 'S' la opción ingresada, termino el programa
            break
    
    # Imprimo el valor
    print(valor)
    
    # Sumo una unidad al valor
    valor += 1

