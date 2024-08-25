# 21. Escribir un programa que enumere los nombres de la lista
# nombres = ['Jose' ,'Pedro' ,'Armando', 'Analía','Florencia'] . utilice la función enumerate

# Lista con nombres
nombres = ['Jose' ,'Pedro' ,'Armando', 'Analía','Florencia']

# Con un ciclo for enumero cada nombre
for numero, nombre in enumerate(nombres):
    # Imprimo el numero con el cual se enumera cada nombre y el nombre de la persona
    print(f'{numero + 1} {nombre}')

