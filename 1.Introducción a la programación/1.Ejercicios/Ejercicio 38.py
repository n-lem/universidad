# Escribir un programa que ayude a escoger un destino para irse de vacaciones,
# entonces, el usuario ingresa por teclado el mes que se tomara las vacaciones (en
# formato numérico), si ingresa el mes diciembre, enero, febrero o marzo,
# mostraremos por pantalla por siguientes puntos turísticos “Mar del plata”, “Santa
# Teresita”, “Córdoba”, “San Luis”, pero si elige los meses junio, julio o agosto
# mostraremos por pantalla "Cataratas", "Bariloche", "Perito Moreno", si elige
# cualquier otro mes mostraremos por pantalla "No tenemos sugerencias cargadas.",
# los sitios turísticos se deben mostrar uno debajo de otro. mes:
# Por ejemplo:
# 12 - Mar del plata Santa Teresita


mes = int(input("Ingrese un número del mes (1-12): "))

if mes == 12 or mes == 1 or mes == 2 or mes == 3:
    print("Sugerencias turísticas para Mar del Plata, Santa Teresita, Córdoba, San Luis:")
    print(f'{mes}. Mar del Plata - Santa Teresita - Córdoba - San Luis')
elif mes == 6 or mes == 7 or mes == 8:
    print("Sugerencias turísticas para Cataratas, Bariloche, Perito Moreno:")
    print(f'{mes}. Cataratas - Bariloche - Perito Moreno')
else:
    print("No tenemos sugerencias cargadas.")
