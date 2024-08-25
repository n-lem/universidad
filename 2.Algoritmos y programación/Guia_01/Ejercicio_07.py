# 7. Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
# Suele hacer venta por correo y la empresa de logística les cobra por peso de 
# cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán
# en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir 
# un programa que lea el número de payasos y muñecas vendidos en el último pedido 
# y calcule el peso total del paquete que será enviado


# Indico el peso del payaso y de la muñeca. Al ser constantes, van en mayúsculas
PESO_PAYASO = 112
PESO_MUNIECA = 75

# Solicito que se ingrese la cantidad vendida de cada producto
payasos_vendidos = int(input('Ingrese la cantidad de payasos vendidos: '))
muniecas_vendidas = int(input('Ingrese la cantidad de muñecas vendidas: '))

# Realizo el cálculo del peso de cada producto vendido
peso_payasos_vendidos = PESO_PAYASO * payasos_vendidos
peso_muniecas_vendidas = PESO_MUNIECA * muniecas_vendidas

# Sumo el peso de cada producto vendido
peso_total_paquete = peso_payasos_vendidos + peso_muniecas_vendidas

# Muestro el resultado del peso total del paquete que contiene los productos
# vendidos, expresado en gramos.
print('El peso total del paquete es de:', peso_total_paquete,' g.')

