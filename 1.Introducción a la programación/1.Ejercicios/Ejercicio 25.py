# Una panadería vende una baguette a $50 cada una. La baguette que no es el día
# tiene un descuento del 60%. Escribir un programa que comience leyendo el
# número de baguette vendidas que no son del día. Después el programa debe
# mostrar el precio habitual de una baguette, el descuento que se le hace por no ser
# fresca y el costo final total con descuento.


# Precio de una baguette
PRECIO_BAGUETTE = 50

# Leo el número de baguette vendidas que no son del día
numero_no_dia = int(input("Ingrese el número de baguette vendidas que no son del día: "))

# Calculo el descuento
descuento = PRECIO_BAGUETTE * 0.6

# Calculo el costo final total con descuento
costo_final = PRECIO_BAGUETTE - descuento
costo_total_con_descuento = numero_no_dia * costo_final
costo_total_con_descuento = round(costo_total_con_descuento, 2)

# Muestro el precio habitual, el descuento y el costo final total con descuento
print(f"Precio habitual de una baguette: ${PRECIO_BAGUETTE}")
print(f"Descuento: -${descuento:.2f}")
print(f"Costo final total con descuento: ${costo_total_con_descuento}")
print(f"Costo final total sin descuento: ${numero_no_dia * PRECIO_BAGUETTE:.2f}")
