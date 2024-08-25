import io
import csv

# Carga de datos de personas
def carga_personas():
    codigo = 0

    # Apertura del archivo
    with open('personas.csv', 'a+', encoding = 'utf-8', newline = '\n') as archivo:

        # Vuelvo el puntero al principio porque a+ abre y se posiciona al final
        archivo.seek(0)
        print('\n Listado de personas \n')

        # Generamos el objeto del tipo csv archivo de lectura
        lectura = csv.reader(archivo, delimiter = ';')
        for cod, nombre, apellido, dni in lectura:
            print(f'{cod:<15} {nombre:<25} {apellido:<25} {dni:<10}')
            if cod != '':
                codigo = cod

        # Generamos el objeto del tipo csv archivo de escritura
        escritura = csv.writer(archivo, delimiter = ';')
        if codigo == 0:
            escritura.writerow(['CODIGO', 'NOMBRE', 'APELLIDO', 'DNI'])
        print('\n Carga de personas')
        while True:
            nom = input('\nIngrese nombre: ')
            ape = input('\nIngrese apellido: ')
            dni = input('\nIngrese dni: ')
            if nom != '' and ape != '' and dni != '':
                codigo = int(codigo) +1
                # Encierro los datos en una lista
                escritura.writerow([codigo, nom, ape, dni])
                print('Usuario agendado correctamente\n')

                op = input('Desea continuar con la carga de personas? (S)i o (N)o: ').upper()
                if op == 'N':
                    break
            else:
                input('\nDatos invalidos. Intente nuevamente.\nPresione Enter para continuar')

# Enlista a las personas de la base de datos
def lista_personas():
    try:
        with open('personas.csv', 'r', encoding = 'utf-8', newline = '\n') as archivo:
            # Generamos el objeto del tipo csv archivo de lectura
            lectura = csv.reader(archivo, delimiter = ';')
            for cod, nombre, apellido, dni in lectura: # Recorro lectura
                print(f'{cod:<15} {nombre:<25} {apellido:<25} {dni:<10}') # Quiero que lo formatee de esta forma
                if cod != '':
                    codigo = cod
            input('\nPresione Enter para continuar') 
    
    except FileNotFoundError:
        input('\nNo hay datos cargados\nPresione Enter para continuar') # En caso de haber error pido que presione enter

# Inicio
while True:
    # Menú principal
    op = input('''
            Menú principal
               
            1. Cargar persona
            2. Listar persona
            3. Salir del programa
               
            Opción: ''')
    
    if op == '1':
        carga_personas()
    elif op == '2':
        lista_personas()
    elif op == '3':
        break
