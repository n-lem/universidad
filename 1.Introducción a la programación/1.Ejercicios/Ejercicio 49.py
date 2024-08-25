# (Utilice while, if, continue y break) Escribir un programa que muestre números
# del 0 al 30 uno debajo de otro.
# ● Cuando los números sean 3, 8, 17, 26 debe mostrar el mensaje “saltando
# instrucciones con (xxxxxxxxxxxxx el nombre de la instrucción que permite
# realizar saltos en un bucle) llegue al número 3 o 8 o 17 o 26”
# ● Cuando los números sean mayor a 25 debe preguntar si continúa o sale del
# conteo (por ejemplo presione Presione: 'S' para salir , cualquier otra tecla para
# continuar)
# ○ Si presiona cualquier tecla el programa seguirá su curso
# ○ Si presiona S, terminará el programa, antes de terminar debe mostrar a
# qué número de conteo llegó.

num = 0

while num <= 30:
    if num == 3 or num == 8 or num == 17 or num == 26:
        print(f"Saltando instrucciones con continue llegue al número {num}")
        num += 1
        continue

    print(num)

    if num > 25:
        respuesta = input("Presione 'S' para salir, cualquier otra tecla para continuar: ")
        if respuesta.upper() == "S":
            print(f"El programa llegó hasta el número {num}")
            break

    num += 1