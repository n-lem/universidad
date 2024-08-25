# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
# Suele hacer venta por correo y la empresa de logística les cobra por peso de cada
# paquete así que deben calcular el peso de los payasos y muñecas que saldrán en
# cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir
# un programa que lea el número de payasos y muñecas vendidos en el último
# pedido y calcule el peso total del paquete que será enviado.

# Peso de los juguetes
PESO_PAYASO = 112
PESO_MUNECA = 75

# Pregunto al usuario el número de payasos y muñecas vendidos
payasos_vendidos = int(input("Ingrese el número de payasos vendidos: "))
munecas_vendidas = int(input("Ingrese el número de muñecas vendidas: "))

# Calculo el peso total del paquete y lo muestro por pantalla
peso_total = (PESO_PAYASO * payasos_vendidos) + (PESO_MUNECA * munecas_vendidas)
print(f"El peso total del paquete es: {peso_total} gramos")

