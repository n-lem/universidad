from tda_parcial import *

import random
print()
print("Turnos")
print()
clientes = Cola()


for i in range ( 0,10):
    clientes.encolar(i)
    print(f"Turno {i} otorgado: ")
print()
print("Sistema de Atención al cliente ")
print()
cajas = ['A','B','C']
for i in range (10):
    print(f"Número {clientes.desencolar()} caja {random.choice(cajas)}: ")
    