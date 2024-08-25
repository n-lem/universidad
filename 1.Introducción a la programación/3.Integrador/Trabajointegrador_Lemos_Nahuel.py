# input 1
# Desarrollar el software de gestión del nombre de una tienda de ropa a
# elección, se implementará un sistema seguro que requiere una contraseña
# generada aleatoriamente para iniciar sesión. Además, se proporcionará la
# funcionalidad de visualizar el catálogo de productos, los cuales estarán
# divididos en las siguientes categorías:

# 1. Camisas: Incluye camisetas, camisas de vestir, camisas informales,
# camisas de manga
# corta o manga larga.
# 2. Pantalones: Incluye pantalones vaqueros, pantalones chinos, pantalones
# de vestir, pantalones cortos.
# 3. Vestidos: Incluye vestidos casuales, vestidos de cóctel, vestidos de
# noche, vestidos formales, vestidos estampados.
# 4. Vestidos: Incluye vestidos casuales, vestidos de cóctel, vestidos de
# noche, vestidos formales, vestidos estampados.
# 5. Trajes: Incluye trajes de dos piezas, trajes de tres piezas, trajes
# formales, trajes de oficina.
# 6. Ropa de abrigo: Incluye abrigos, chaquetas, chaquetones, gabardinas,
# chalecos.
# 7. Ropa deportiva: Incluye camisetas deportivas, pantalones deportivos,
# sudaderas, leggings
# deportivos, ropa de yoga.
# 8. Ropa de dormir: Incluye pijamas, camisones, batas, pantalones de pijama,
# conjuntos de dormir.
# 9. Accesorios: Incluye sombreros, gorras, bufandas, guantes, cinturones,
# joyas, bolsos.

# El software de gestión del nombre de la tienda de ropa también incluirá las
# siguientes funcionalidades:

# * Agregar productos al carrito de compra: Los usuarios podrán seleccionar
# productos del catálogo y agregarlos al carrito de compra. Podrán indicar la
# cantidad deseada de cada
# producto.

# * Ver productos en el carrito: Los usuarios podrán ver los productos que han
# agregado al carrito de compra. Se mostrará la información detallada de cada
# producto, como su nombre, categoría, precio y cantidad.

# * Eliminar productos del carrito: Los usuarios tendrán la posibilidad de
# eliminar productos del carrito de compra si desean cambiar su selección o si
# ya no desean adquirir dicho producto. Podrán seleccionar el producto que
# deseen eliminar y confirmar su eliminación.

# * Finalizar la compra: Una vez que los usuarios hayan agregado todos los
# productos deseados al carrito, podrán finalizar la compra. Se les solicitará
# confirmar su elección y se procederá al proceso de pago.

# * Medios de pago: Los usuarios podrán seleccionar el medio de pago según las
# siguientes
# condiciones:
# - Efectivo: 10% de descuento.
# - Tarjeta de crédito: Cubre el programa ahora 3 (12% de aumento) ,6 (18% de
# aumento)
# y 12 (36% de aumento). Debe respetar la siguiente tabla:

# Nro   |   Dia         |   Tarjeta de beneficio    |   Descuento total
# 1     |   Domingo     |   VISSA BNNA              |       15%
# 2     |   Lunes       |   MASTERCARD PRV          |       20%
# 3     |   Martes      |   CENNSOCUD MNP           |       15%
# 4     |   Miércoles   |   CLARESEN KFC            |       30%
# 5     |   Jueves      |   OFFIOTA LUCRA           |       20%
# 6     |   Viernes     |   TREVVI CIR              |       10%
# 7     |   Sábado      |   PUETRA COM              |       5%
# Bitcoin: Mismo precio.

# El software de gestión del nombre de la tienda de ropa contará con las
# siguientes validaciones y medidas de seguridad adicionales para evitar
# bloqueos de operaciones no válidas:

# * Validación de entrada de caracteres: En aquellos campos donde solo se
# permiten caracteres, se verificará que el usuario ingrese solo caracteres
# alfanuméricos y caracteres especiales permitidos. Si se ingresan caracteres
# no válidos, se solicitará que se ingrese nuevamente hasta un máximo de
# cinco intentos. Si se supera este límite, el usuario será bloqueado por un
# minuto antes de poder intentarlo nuevamente.

# * Validación de selección de productos: Al agregar productos al carrito, se
# verificará que el producto seleccionado esté en la lista de productos
# disponibles. Si se ingresa un producto no válido, se solicitará que se
# ingrese nuevamente hasta un máximo de cinco intentos. Si se supera este
# límite, el usuario será bloqueado por un minuto antes de poder intentarlo
# nuevamente.

# * Validación de cantidad de productos: Al agregar productos al carrito, se
# verificará que la cantidad ingresada sea un número entero positivo. Si se
# ingresa una cantidad no válida, se solicitará que se ingrese nuevamente
# hasta un máximo de cinco intentos. Si se supera este límite, el usuario
# será bloqueado por un minuto antes de poder intentarlo nuevamente.

# * Prevención de bloqueo infinito: Se implementará un mecanismo de control de
# intentos para evitar que el programa quede atrapado en un bucle infinito.
# Se establecerá un contador de intentos que se reiniciará después de cada
# intento válido. Si se alcanza el máximo de intentos permitidos en una
# función específica, se mostrará un mensaje de error y el programa continuará
#  con las siguientes operaciones o mostrará un menú de opciones para que el
# usuario decida cómo proceder.

# * Validación de operaciones: Antes de realizar cualquier operación, se
# verificará que la operación solicitada sea válida y esté permitida en ese
# momento. Por ejemplo, si se intenta finalizar la compra sin haber agregado
# productos al carrito, se mostrará un mensaje de error indicando que no hay
# productos en el carrito y se pedirá al usuario que agregue productos antes
# de finalizar la compra.

# Estas medidas de validación y seguridad adicional garantizarán que el
# software funcione de manera segura y evite bloqueos junto con operaciones
# no válidas. Además, se informará claramente al usuario sobre las
# validaciones y se proporcionarán instrucciones para seguir utilizando el
# programa de manera correcta y eficiente.

# Importar las bibliotecas random y os:

import random  # Para generar números aleatorios
import os  # Para limpiar la pantalla
import time  # Para utilizar un reloj

# Variables globales

# Nombre de la tienda
NOMBRE_TIENDA = 'Black Diamond'

# Creo una lista vacía donde se guardarán los productos agregados al carrito
carrito = []

# Total de la compra
total = 0


# Defino el catálogo de productos como una matriz de listas de categorias.
# Las listas de categorias contienen sublistas con productos, precios y stock.
# Es decir, defino un catálogo que es una matriz de listas de sublistas
def crear_catalogo():
    # Defino una lista vacía para almacenar los datos de cada producto
    lista_productos = []
    # Defino una matriz vacía, que contendrá la lista de productos por
    # categoría
    catalogo = []

    # Defino las categorías
    categorias = [
        'Camisas',
        'Pantalones',
        'Vestidos',
        'Trajes',
        'Ropa de abrigo',
        'Ropa deportiva',
        'Ropa de dormir',
        'Accesorios',
    ]

    # Defino los productos
    productos_agrupados_por_categoria = [
        # Camisas
        [
            'Camiseta',
            'Camisa de vestir',
            'Camisa informal',
            'Camisa de manga corta',
            'Camisa de manga larga',
        ],
        # Pantalones
        [
            'Pantalón vaquero',
            'Pantalón chino',
            'Pantalón de vestir',
            'Pantalón corto',
        ],
        # Vestidos
        [
            'Vestido casual',
            'Vestido de cóctel',
            'Vestido de noche',
            'Vestido formal',
            'Vestido estampado',
        ],
        # Trajes
        [
            'Traje de dos piezas',
            'Traje de tres piezas',
            'Traje formal',
            'Traje de oficina',
        ],
        # Ropa de abrigo
        ['Abrigo', 'Chaqueta', 'Chaquetón', 'Gabardina', 'Chaleco'],
        # Ropa deportiva
        [
            'Camiseta deportiva',
            'Sudadera',
            'Legging deportivo',
            'Ropa de yoga',
        ],
        # Ropa de dormir
        [
            'Pijama de algodón',
            'Pijama de seda',
            'Camisón de algodón',
            'Camisón de seda',
            'Bata de algodón',
            'Bata de seda',
            'Pantalón de pijama',
            'Conjunto de dormir',
        ],
        # Accesorios
        [
            'Sombrero',
            'Gorra',
            'Bufanda',
            'Guantes',
            'Cinturón',
            'Joya',
            'Bolso',
        ],
    ]

    # Creo una lista de productos donde agregaré precios y cantidades del
    # producto
    lista_productos = []

    # Recorro cada producto agrupado por categoria
    for productos_de_categoria in productos_agrupados_por_categoria:
        # Creo una lista vacía donde agregaré los productos con sus precios y
        # stock
        productos_con_precios_y_stock = []
        # Recorro cada producto de los productos agrupados por categoria
        for producto in productos_de_categoria:
            # Por cada producto designo un precio random
            precio = random.randint(300000, 1500000) / 100

            # Por cada producto designo un stock random
            cantidad = random.randint(1, 100)

            # Agrego una lista a una matriz con el nombre del producto, el
            # precio y un stock
            productos_con_precios_y_stock.append([producto, precio, cantidad])
        # Agrego una lista a una matriz con el nombre del producto, el precio
        # y un stock
        lista_productos.append(productos_con_precios_y_stock)

    # Indice de filas
    indice_fila = 0

    # Recorro la lista de productos para obtener cada producto con su precio
    # y su stock
    for producto_con_precio_y_stock in lista_productos:
        # Obtengo la categoria n-ésima de la lista de categorias
        categoria = categorias[indice_fila]

        # Agrego a cada categoría los productos con su precio y stock
        catalogo.append([categoria, producto_con_precio_y_stock])

        # Contador para avanzar a la siguiente categoria
        indice_fila += 1

    # Devuelvo la matriz con los datos
    return catalogo


# Genero una contraseña aleatoria
def generar_contrasena():
    # Defino los posibles caracteres de la contraseña
    caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ\
0123456789!@#$%^&*()_+-='

    # Defino la longitud de la contraseña de forma aleatoria entre 8 y 12
    # caracteres
    longitud = random.randint(8, 12)

    # Creo una cadena vacía para almacenar la contraseña
    contrasena = ''

    # Armo la contraseña
    for _ in range(longitud):
        # Elijo un caracter aleatorio de la lista de caracteres y lo agrego a
        # la cadena
        contrasena += random.choice(caracteres)

    # Devuelvo la contraseña
    return contrasena


# Limpiar pantalla
def limpiar_pantalla():
    # Comprueba el sistema operativo
    sistema = os.name

    # Para Windows
    if sistema == 'nt':
        os.system('cls')

    # Para Linux o iOS
    elif sistema == 'posix':
        os.system('clear')

    # Si no se puede limpiar la pantalla muestra un mensaje
    else:
        print('No se puede limpiar la pantalla en este sitema operativo.')
        # Agrego 100 saltos de líneas para limpiar la pantalla
        print('\n' * 100)


# Valido que lo ingresado sea un caracter alfanumérico o un caracter permitido
def validar_entrada(entrada):
    # Se devuelve True si la entrada es válida o False si no lo es

    # Defino los caracteres válidos
    caracteres_validos = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxy\
z0123456789!@#$%^&*()'

    # Recorro cada caracter de la entrada
    for caracter in entrada:
        # Si el caracter no está en los caracteres válidos
        if caracter not in caracteres_validos:
            # Devuelve False
            return False

    # Si todos los caracteres son válidos, devuelve True
    return True


# Defino la función para una cuenta regresiva de x segundos, donde x es el
# tiempo.
def cuenta_regresiva(tiempo):  # simplificar la función cuenta_regresiva
    while tiempo > 0:  # usar un bucle while
        # usar el argumento end='\r' para sobreescribir la línea anterior
        print(f'Esperá {tiempo} segundos.', end='\r')
        time.sleep(1)  # esperar un segundo
        tiempo -= 1  # restar uno al tiempo
    print(' '*20, end='\r')  # borrar la línea


# Función para iniciar sesión
def iniciar_sesion():
    # Genero una contraseña aleatoria
    contrasena = generar_contrasena()
    # Inicializo el contador de intentos en cero
    intentos = 0

    # Muestro un mensaje de bienvenida con el nombre de la tienda
    print(f'¡Hola! Bienvenido al software de gestión de {NOMBRE_TIENDA}.\n')

    # Indico que se debe ingresar la contraseña
    print('Para iniciar sesión, ingrese la contraseña que se muestra abajo.\n')

    # Se indica que se tiene un límite de intentos
    print(
        f'''{'·'*78}
{'ATENCIÓN':^78}
{' '}
{'Tenés cinco intentos para ingresar la contraseña correctamente.':^78}
{'·'*78}\n'''
    )

    # Se muestra la contraseña
    print(f'La contraseña es: {contrasena:^20}\n')

    # Un bucle infinito
    while True:
        # Se pide al usuario que ingrese la contraseña
        ingreso = input('Ingresá la contraseña: ')

        # Si el ingreso coincide con la contraseña
        if ingreso == contrasena:
            # Limpio la pantalla
            limpiar_pantalla()

            # Designo un tiempo para la cuenta regresiva
            tiempo = 2

            # Mensaje de ingreso exitoso
            print(
                f'''{'·'*78}
{'Contraseña correcta':^78}
{'·'*78}\n'''
            )

            # Mensaje de cuenta regresiva y contador
            print(
                f'Se inició sesión correctamente.\n\nSe mostrará el menú en \
{tiempo} segundos.'
            )
            cuenta_regresiva(tiempo)

            # Se rompe el bucle infinito
            break

        # Si el ingreso no coincide con la contraseña
        else:
            # Se incrementa el contador de intentos en uno
            intentos += 1

            # Si se alcanza el máximo de intentos permitidos
            if intentos == 5:
                # Designo un minuto para la cuenta regresiva
                tiempo = 60

                # Se muestra un mensaje de error
                print(
                    'Superaste el límite de intentos. Esperá un minuto antes \
de volver a escribirla.\n'
                )

                # Se hace una pausa de un minuto
                cuenta_regresiva(tiempo)

                # Limpio la pantalla
                limpiar_pantalla()

                # Se genera una nueva contraseña
                contrasena = generar_contrasena()

                # Se muestra la nueva contraseña
                print(f'La nueva contraseña es:\n{contrasena}\n')

                # Reinicio el contador de intentos
                intentos = 0

            # Si se ingresa mal la contraseña se resta un intento
            else:
                # Se muestra un mensaje de error y los intentos restantes
                print(
                    'Contraseña incorrecta. Te quedan',
                    5 - intentos,
                    'intentos.\n',
                )


# Función para mostrar el menú principal
def mostrar_menu():
    # Se muestra el título del menú
    print(f'{"·"*78}\n{"MENÚ PRINCIPAL":^78}\n{"·"*78}\n')
    opciones = [
        'Ver catálogo de productos',  # Opción 1
        'Agregar productos al carrito',  # Opción 2
        'Ver productos en el carrito',  # Opción 3
        'Eliminar productos del carrito',  # Opción 4
        'Finalizar la compra',  # Opción 5
        'Salir',  # Opción 6
    ]
    for elemento in range(len(opciones)):
        print(f' [{elemento+1}] {opciones[elemento]}')
    print()
    return len(opciones)


# Función para validar si un numero ingresado es un entero
def es_numero_entero(valor):
    # Compara el valor con una cadena vacía
    match valor:
        # Si el valor es una cadena vacía, devuelve False
        case '':
            return False

        # Si el valor no es una cadena vacía
        case _:
            # Recorre cada caracter del valor
            for caracter in valor:
                # Si el caracter no está en la cadena de dígitos,
                # devuelve False
                if caracter not in '0123456789':
                    return False

            # Si todos los caracteres son dígitos, devuelve True
            return True


# Función para determinar si un valor ingresado es válido o no.
# Requiere un parámetro numérico a validar, por ejemplo, el largo de una
# cadena o el largo de una lista
def validar_opcion(maximo, opcion):
    intentos = 0  # variable para contar los intentos
    while True:  # usar un bucle while en lugar de un for
        # usar el método isdigit()
        if opcion.isdigit():
            # convertir la cadena a entero
            opcion = int(opcion)
            # verificar que la opción esté dentro del rango
            if opcion > 0 and opcion <= maximo:
                return opcion  # retornar la opción válida
            else:
                print('Opción inválida. Debe ingresar un número entre 1 y',
                      maximo)
        else:
            print('Opción inválida. Debe ingresar un número entero positivo.')
        intentos += 1  # incrementar los intentos si es inválido
        if intentos == 5:  # si se supera el límite de intentos
            tiempo = 60
            print(f'\nSe superaron los intentos. Esperá {tiempo} \
segundos para volver a intentarlo.\n')
            cuenta_regresiva(tiempo)  # hacer esperar al usuario
            intentos = 0  # reiniciar los intentos
        else:
            print(f'\nTe quedan {5 - intentos} intentos.')
        # pedir una nueva opción al usuario
        opcion = input('Ingresá una opción: ')


# Función para mostrar el catálogo de productos
def mostrar_catalogo(catalogo):
    limpiar_pantalla()  # Limpio la pantalla
    # Se muestra el título del catálogo
    print(f'{"·"*78}\n{"CATÁLOGO DE PRODUCTOS":^78}\n{"·"*78}\n')

    # Recorro el catálogo
    for i in range(len(catalogo)):
        # Imprimo un número identificador y la categoría del catálogo
        # La categoría se encuentrá en la fila i-ésima y es en la posición 0
        print(f' [{i+1}] {catalogo[i][0]}')
    # Indico que si se presiona Enter se vuelve al menú anterior
    print('\n [ENTER] Volver al menú anterior.\n')

    # Solicito que se ingrese una opción
    numero_categoria = input(
        'Ingresá el número de la categoría que querés ver: ')
    # Al presionar Enter se vuelve al menú anterior
    if numero_categoria == '':
        return
    # Llamo a la función validar_opción, que me dice si lo ingresado es válido
    #  o no
    # En caso de ser válido, lo convierto a un dato del tipo entero y le
    # resto 1, para obtener el índice
    categoria = int(validar_opcion(len(catalogo), numero_categoria)) - 1

    # Limpio la pantalla
    limpiar_pantalla()

    # Imprimo la etiqueta de categoría
    print('·' * 78)
    print(f'{catalogo[categoria][0].upper():^78}')
    print('·' * 78, '\n')

    # Matriz de etquetas de la tabla a mostrar
    etiquetas = ['Producto', 'Precio', 'Stock']

    # Diseño del encabezado de la tabla
    imprimir_encabezado = f'·  ID ·{etiquetas[0]:^29}·{etiquetas[1]:^15}·\
{etiquetas[2]:^9}·'.format(
        *etiquetas
    )
    imprimir_linea_separatoria = '·' * 63
    print(imprimir_linea_separatoria)
    print(imprimir_encabezado)
    print(imprimir_linea_separatoria)

    # Asigno un índice de fila
    indice_fila = 1

    # Recorro los elementos de cada categoría
    for producto in range(len(catalogo[categoria][1])):
        # Imprimo la tabla diseñada e indico un indíce, producto, precio y
        # stock de cada producto de la categoria
        print(
            f'· {indice_fila:^4}· {catalogo[categoria][1][producto][0]:<28}· \
$ {catalogo[categoria][1][producto][1]:>11} · \
{catalogo[categoria][1][producto][2]:>7} ·'
        )
        # Incremento el índice de la fila
        indice_fila += 1
    # Final del diseño de la tabla
    print(imprimir_linea_separatoria)

    # Devuelvo la matriz de la categoría solicitada para un posterior uso
    return categoria

# Función para agregar productos al carrito
def agregar_productos(catalogo, carrito):
    # Asigno un 3 a la variable tiempo, que será usado en un temporizador
    tiempo = 3
    # Muestro el título de la función
    print(f'{"·"*78}\n{"AGREGAR PRODUCTOS":^78}\n{"·"*78}\n')
    # Bucle infinito
    while True:
        # Llamo a la función para mostrar el catálogo de productos
        categoria = mostrar_catalogo(catalogo)

        # Si el usuario presionó ENTER
        # Se muestra un mensaje de que se volverá al menú anterior,
        # se muestra una cuenta regresiva, se limpia la pantalla y
        # se rompe el ciclo infinito
        if categoria is None:
            limpiar_pantalla()  # Limpio la pantalla
            break

        # Se calcula la cantidad de productos contenidos en la categoría
        # seleccionada
        cantidad_de_productos_en_categoria = len(catalogo[categoria][1])

        print('\n [ENTER] Volver al menú principal')
        # Solicito que se ingrese el ID del producto
        id_producto = input('\nIngresá el ID del producto: ')

        # Si el ID ingresado es nulo, entonces se vuelve al menú anterior
        if id_producto == '':
            limpiar_pantalla()  
            break

        # Si el usuario ingresa un nombre de producto
        else:
            # Valido que el ingreso sea correcto
            producto = (
                validar_opcion(
                    cantidad_de_productos_en_categoria, id_producto) - 1
            )
            # Se inicializa una variable booleana como Falsa
            encontrado = False

            # Se recorre la matriz con los productos
            for i in range(
                len(catalogo[categoria][1])
            ):  
                # Si el producto ingresado coincide con el nombre de algún
                # producto de la matriz
                if catalogo[categoria][1][producto][0] == \
                        catalogo[categoria][1][i][0]:
                    # Se cambia la variable booleana a Verdadera
                    encontrado = True
                    # Se guarda el índice del producto encontrado
                    indice = i  
                    # Se imprime el producto elegido
                    print(
                        f'\n* Producto elegido: \t\
{catalogo[categoria][1][producto][0]}\n'
                    )
                    # Se rompe el bucle for
                    break  
            # Si se encontró el producto en la matriz
            if encontrado:  
                # Se comprueba si se pueden agregar producto al carrito
                if catalogo[categoria][1][producto][2] <= 0:
                    print(
                        f'No se pueden agregar productos al carrito dado que \
el stock es de {catalogo[categoria][1][producto][2]}'
                    )
                    # Temporizador
                    cuenta_regresiva(tiempo)
                    # Se vuelve al menú anterior
                    break

                # Se pide al usuario que ingrese la cantidad que desea agregar
                auxiliar = input(
                    f'Ingresá la cantidad que desea agregar \
(Max. {catalogo[categoria][1][producto][2]}): '
                )
                # Si se presiona ENTER se vuelve al menú anterior
                if auxiliar == '':
                    limpiar_pantalla()
                    break
                # Valido la cantidad ingresada
                cantidad = validar_opcion(catalogo[categoria][1][producto][2],
                                          auxiliar)
                # Si la cantidad es mayor que cero
                if cantidad > 0:
                    # Si la cantidad es menor o igual que el stock disponible
                    # del producto
                    if cantidad <= int(catalogo[categoria][1][producto][2]):
                        # Se agrega el producto al carrito con su categoría,
                        # nombre, precio y cantidad
                        carrito.append(
                            [
                                catalogo[categoria][0],
                                catalogo[categoria][1][producto][0],
                                catalogo[categoria][1][producto][1],
                                cantidad,
                            ]
                        )
                        # Resto la cantidad en el catálogo
                        catalogo[categoria][1][producto][2] -= cantidad
                        # Se muestra un mensaje de confirmación
                        print(
                            f'\n* Se han agregado {cantidad} unidad(es) de \
{catalogo[categoria][1][producto][0].lower()} al carrito.'
                        )
                        # Regreso al menú anterior para seguir comprando
                        input('\nPresioná [ENTER] para continuar comprando.')
                     # Si la cantidad es mayor que el stock disponible del producto
                    else: 
                        # Se muestra un mensaje de error y el stock disponible
                        print(
                            'No hay suficiente stock para ese producto. El \
stock disponible es:',
                            catalogo[categoria][1][producto][2],
                        )
                # Si la cantidad es menor o igual que cero se muestra un mensaje de error
                else:  
                    print('La cantidad debe ser mayor que cero.')
            # Si no se encontró el producto en la matriz
            else:  
                # Se muestra un mensaje de error
                print('El producto ingresado no existe en el catálogo.')
                cuenta_regresiva(tiempo)
    return carrito


# Función para ver los productos en el carrito
def ver_productos(carrito):
    total = 0  # Se inicializa la variable del total como cero
    id_producto = 0 # Se inicializa la variable del identificador del producto como cero
    # Se muestra el título de la función
    print(f'{"·"*78}\n{"CARRITO DE PRODUCTOS":^78}\n{"·"*78}\n')
    if len(carrito) == 0 or len(carrito) == None:  # Si el carrito está vacío
        # Se muestra un mensaje de aviso
        print('░' * 34 + '  VACÍO   ' + '░' * 34 + '\n')
        print(f'{"No hay productos en el carrito.":^78}\n')
    # Si el carrito no está vacío
    else:  
        # Se muestra un mensaje informativo
        etiquetas = ['ID.', 'Categoria', 'Producto', ' Precio', 'Stock']

        # Diseño de la tabla
        imprimir_encabezado = f':{etiquetas[0]:^6}:{etiquetas[1]:^17}:\
{etiquetas[2]:^25}:{etiquetas[3]:^15}:{etiquetas[4]:^9}:'.format(
            *etiquetas
        )
        imprimir_linea_separatoria = '·' * 78

        print(imprimir_linea_separatoria)
        print(imprimir_encabezado)
        print(imprimir_linea_separatoria)

        # Se recorre la lista del carrito
        for producto in carrito:  
            # Se muestra la información de cada producto
            # Se diseña la tabla con id del producto, la categoría, el producto, precio y stock
            print(
                f':{id_producto+1:^6}: {producto[0]:<16}: {producto[1]:<24}\
: $ {producto[2]:>11} :{producto[3]:>8} :'
            )  
            # Se muestra el total de la compra
            total += float(producto[2]) * int(producto[3])
            # Aumento el id del producto para mostrar el siguiente
            id_producto += 1
        # Diseño de la tabla
        print(imprimir_linea_separatoria)
        # Se imprime el total
        print(f'\nEl total de la compra es: $ {total:.2f}')
    # Devuelvo el total
    return total


# Función para eliminar productos del carrito
def eliminar_productos(carrito):
    total = 0  # Se inicializa la variable del total como cero
    # Se muestra el título de la función
    print(f'{"·"*78}\n{"ELIMINAR PRODUCTOS":^78}\n{"·"*78}\n')
    # Un bucle infinito
    while True:  
        # Se llama a la función para ver los productos en el carrito
        ver_productos(
            carrito
        )  
        # Si está vario se pide que ingrese ENTER para continuar
        if len(carrito) == 0:
            input('Presioná [ENTER] para continuar.')
            limpiar_pantalla()
            return carrito
        # Separador
        print('⎼' * 78)

        # En caso de no estar vacío se sigue el programa
        # Se pide que se indique el producto a eliminar
        print('\n¿Qué producto querés eliminar?\n')

        # Se muestran los productos con un id
        for id_producto in range(len(carrito)):
            print(f' [{id_producto+1}] {carrito[id_producto][1]}')
        print('\n [ENTER] Volver al menú principal\n')
        # Se pide al usuario que ingrese el nombre del producto o presione
        # ENTER para salir
        producto = input('Ingresá el ID del producto que desea eliminar: ')
        # Si el usuario presiona ENTER
        if producto == '':  
            return carrito
            limpiar_pantalla()
            # Se rompe el bucle infinito
            break  
        # Se busca el producto a eliminar
        else:
            # Valido el producto ingresado
            producto = validar_opcion(len(carrito), producto) - 1
            print('\n * Producto a eliminar: ', carrito[producto][1], '\n')

            # Inicio los intentos
            intentos = 0  

            # bucle para validar la entrada
            while True:  
                # Pido una confrimación de eliminación
                confirmacion = input(
                    '¿Está seguro de que desea eliminar el producto? (S/N): '
                )

                # Uso match case para saber que paso seguir
                match confirmacion.lower():
                    case 's':
                        carrito.pop(producto) # Elimino el producto de la i-ésima posición
                        input('Se ha eliminado el producto del carrito. \
Presioná [ENTER] para continuar.')
                        return carrito # Devuelvo el carrito
                        break  # salir del bucle si es válido
                    case 'n':
                        input('No se ha eliminado el producto del carrito. \
Presioná [ENTER] para continuar.')
                        limpiar_pantalla()
                        break  # salir del bucle si es válido
                    case _:
                        # incrementar los intentos si es inválido
                        intentos += 1
                        # si se supera el límite de intentos
                        if intentos == 5:
                            tiempo = 60 # Tiempo de espera
                            print(
                                f'\nSe superaron los intentos. Esperá \
{tiempo} segundos para volver a intentarlo.\n'
                            ) # Mensaje
                            # hacer esperar al usuario
                            cuenta_regresiva(tiempo)
                            intentos = 0  # reiniciar los intentos
                        # Indico que la opción no es válida
                        else:
                            print(f'\nOpción inválida. Te quedan \
{5 - intentos} intentos. Debe ingresar S o N.')
                        continue

# Datos de la tabla con los días, tarjetas de beneficio y descuentos
def matriz_tarjetas():
    return [
        ['Domingo', 'VISSA BNNA', 15],
        ['Lunes', 'MASTERCARD PRV', 20],
        ['Martes', 'CENNSOCUD MNP', 15],
        ['Miércoles', 'CLARESEN KFC', 30],
        ['Jueves', 'OFFIOTA LUCRA', 20],
        ['Viernes', 'TREVVICIR', 10],
        ['Sábado', 'PUETRA COM', 5],
    ]


# Función para finalizar la compra
def finalizar_compra(carrito):
    total = 0 # Inicio el total en 0
    descuento = 0 # Inicio los descuentos en 0
    aumento = 1 # El aumento del precio es 1, es decir, nulo
    dias = ['Domingo', 'Lunes', 'Martes',
            'Miércoles', 'Jueves', 'Viernes', 'Sábado'] # Dias de la semana
    print(f'{"·"*78}\n{"FINALIZAR COMPRA":^78}\n{"·"*78}\n') # Titulo de la función
    # En caso de estar vacío el carrito
    if len(carrito) == 0:
        print(
            'No se puede finalizar la compra sin haber agregado productos al \
carrito.\n'
        )
        # Tiempo de espera
        tiempo = 3 
        print(f'Volviendo al Menú principal en {tiempo} segundos.\n')
        cuenta_regresiva(tiempo)
        limpiar_pantalla()
        return carrito # Devuelvo el carrito tal cual estaba
    # En caso de no estar vacío
    else:
        # Mustro el carrito y obtengo su total
        total = ver_productos(
            carrito
        )
        intentos = 0  # variable para contar los intentos
        while True:  # bucle para validar la entrada
            # Pido confirmación al usuario
            confirmacion = input(
                '¿Está seguro de que desea finalizar la compra? (S/N): '
            )
            # Uso match case para validar lo ingresado
            match confirmacion.upper():
                case 'S':
                    # Mensajes útiles para el usuario
                    print()
                    print(f'Total a pagar: \t$ {total:.2f}\n')
                    print('Seleccione el medio de pago: \n')
                    # Lista con métodos de pago
                    metodo_de_pago = ['Efectivo', 'Tarjeta de crédito',
                                      'Bitcoin']
                    # Muestro los métodos de pagos
                    for i in range(len(metodo_de_pago)):
                        print(f' [{i+1}] {metodo_de_pago[i]}')
                    # Solicito el método de pago
                    medio_de_pago = input('Indicá el número del medio de \
pago: ')
                    # VAlido el método de pago
                    medio_de_pago = validar_opcion(len(metodo_de_pago),
                                                   medio_de_pago) - 1
                    print(' * Método de pago: ',metodo_de_pago[medio_de_pago])
                    # Aplico los descuentos
                    match medio_de_pago:
                        case 0:
                            descuento = 0.10
                        case 1:
                            for i in range(len(dias)):
                                print(' ', [i+1], dias[i])
                            dia = input(
                                'Ingresá el ID del día de la semana en que realizará \
la compra: '
                            )
                            dia = validar_opcion(7,dia)-1
                            print()
                            # REcorro la matriz tarjetas
                            for i in range(len(matriz_tarjetas())):
                                print(f' - {matriz_tarjetas()[i][1]}')
                            tarjeta = input(
                                'Ingresá el nombre de la tarjeta con la que \
realiza el pago: '
                            )
                            print()
                            # BUsco coincidencias entre el día y la tarjeta, entonces aplicio descuento
                            match tarjeta.upper():
                                case 'VISSA BNNA':
                                    if dia == 0:
                                        descuento = 15
                                case 'MASTERCARD PRV':
                                    if dia == 1:
                                        descuento = 20
                                case 'CENNSOCUD MNP':
                                    if dia == 2:
                                        descuento = 15
                                case 'CLARESEN KFC':
                                    if dia == 3:
                                        descuento = 30
                                case 'OFFIOTA LUCRA':
                                    if dia == 4:
                                        descuento = 20
                                case 'TREVVICIR':
                                    if dia == 5:
                                        descuento = 10
                                case 'PUETRA COM':
                                    if dia == 6:
                                        descuento = 5
                                case _:
                                    descuento = 0
                            # Indico el descuento encontrado
                            print(f'Hay un descuento del {descuento}%')
                            print()
                            print('Seleccioná el plan de pago:\n')
                            print(' [ 3] Ahora 3')
                            print(' [ 6] Ahora 6')
                            print(' [12] Ahora 12')
                            cuotas = int(input(
                                'Ingresá la cantidad de cuotas: '))
                            match cuotas:
                                case 3:
                                    aumento = 1.12
                                case 6:
                                    aumento = 1.18
                                case 12:
                                    aumento = 1.36
                                case _:
                                    # Solicito que ingrese 3, 6 o 12, con un máximo de 5 intentos
                                    while True:
                                        if cuotas not in ['3','6','12']:
                                            intentos += 1
                                            coutas = input(f'Opción incorrecta. Te quedan {5-intentos} intentos. Ingrese 3, 6 o 12: ')
                                        else:
                                            intentos = 0
                                            break
                                        if intentos == 5:
                                            print('Superaste los 5 intentos. Esperá 1 minuto para continuar.')
                                            cuenta_regresiva(60)
                            # Busco coincidencias entre la fila  y la tarjeta
                            for i in range(len(matriz_tarjetas())):
                                if dia == matriz_tarjetas()[i][0] and tarjeta == matriz_tarjetas()[i][1]:
                                    descuento = matriz_tarjetas()[i][2]
                                    break
                        case 2:
                            descuento = 0
                            aumento = 1
                            precio_btc = round(random.uniform(12589372,
                                                              16914458), 2)
                            print(precio_btc)
                            total = total
                    if descuento > 0:
                        print(
                            f'\nTenés un descuento del {descuento} \
% por comprar con {(metodo_de_pago[medio_de_pago]).lower()}.')
                        print(f'\nEl total de la compra sin ningún descuento es:\
\n $ {total:.2f}.')
                        print(f'\nEl monto descontado es de: \n \
$ {total*aumento*((descuento/100)):.2f}')
                        total = total * aumento * (1-(descuento/100))
                        print(f'\nEl total de la compra con el descuento es: \n \
$ {total:.2f}')
                    else:
                        print(f'Lo sentimos, no hay ningún descuento \
disponible por comprar con {(metodo_de_pago[medio_de_pago]).lower()}.'
                              )
                        print(f'El total de la compra sin ningún descuento es:\
 $ {total:.2f}')
                    input('Gracias por su compra. Presiona [ENTER] para \
continuar.')
                    limpiar_pantalla()
                    carrito = []
                    return carrito
                    break  # salir del bucle si es válido
                case 'N':
                    print(
                        'No ha finalizado la compra. Puede seguir agregando o \
eliminando productos del carrito.'
                    )
                    break  # salir del bucle si es válido
                case _:
                    intentos += 1  # incrementar los intentos si es inválido
                    if intentos == 5:  # si se supera el límite de intentos
                        tiempo = 60
                        print(
                            f'\nSe superaron los intentos. Esperá {tiempo} \
segundos para volver a intentarlo.\n'
                        )
                        cuenta_regresiva(tiempo)  # hacer esperar al usuario
                        intentos = 0  # reiniciar los intentos
                    else:
                        print(f'\nOpción inválida. Te quedan {5 - intentos} \
intentos. Debe ingresar S o N.')
    print()
    input('Presioná [ENTER] para continuar.')
    return carrito
    limpiar_pantalla()


# Función principal del programa

def main():
    carrito_compras = []

    # Matriz con datos del catálogo
    matriz = crear_catalogo()

    # Limpio la pantalla
    limpiar_pantalla()

    # Se llama a la función para iniciar sesión con la contraseña
    # iniciar_sesion()

    # Limpio la pantalla
    limpiar_pantalla()

    # Un bucle infinito
    while True:
        # Se llama a la función para validar una opción del menú principal y
        # se guarda el resultado en una variable
        opcion = validar_opcion(mostrar_menu(), input('Ingresá una opción: '))

        # Limpio la pantalla
        limpiar_pantalla()

        # Uso match case para hacer coincidir la opción con el menú
        match opcion:
            # Si la opción es 1
            case 1:
                # Llamo a la función para mostrar el catálogo de producto

                if mostrar_catalogo(matriz) == None:
                    limpiar_pantalla()
                    continue
                # Indico que se debe presionar Enter para continuar
                else:
                    input('\nPresioná [ENTER] para continuar. ')
                    # Limpio la pantalla
                    limpiar_pantalla()

            # Si la opción es 2
            case 2:
                # Se llama a la función para agregar productos al carrito
                carrito_compras = agregar_productos(matriz, carrito_compras)
                continue
            # Si la opción es 3
            case 3:
                # Se llama a la función para ver los productos en el carrito
                ver_productos(carrito_compras)
                input('Presioná [ENTER] para continuar.')
                limpiar_pantalla()

                # Limpio la pantalla

            # Si la opción es 4
            case 4:
                # Se llama a la función para eliminar productos del carrito
                carrito_compras = eliminar_productos(carrito_compras)
                continue
            # Si la opción es 5
            case 5:
                # Se llama a la función para finalizar la compra
                carrito_compras = finalizar_compra(carrito_compras)
                continue
            # Si la opción es 6
            case 6:
                print('╔' + '═' * 78 + '╗')
                # Se muestra un mensaje de despedida
                print(
                    f'║   Gracias por usar el software de gestión de \
{NOMBRE_TIENDA}. Hasta pronto.    ║'
                )
                print('╚' + '═' * 78 + '╝')
                # Se rompe el bucle infinito
                break
            #


# Llamada a la función principal del programa
main()
