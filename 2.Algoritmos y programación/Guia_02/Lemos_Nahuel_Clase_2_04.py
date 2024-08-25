# Alumno: Lemos, Nahuel

# Escriba un programa que simule ser un sorteo al azar con 58 participantes. 
# Tenemos sus números de DNI, los participantes tienen números de dni entre 
# 43158258 y 44200952, no puede haber participantes repetidos, una vez cargados 
# los dni, debe seleccionar 3 ganadores al azar, no se pueden repetir los 
# ganadores, muestre el listado de participantes, muestre el número de dni de 
# los ganadores


# Importo librerías
import array as arr
import random



# Creo una función para generar una lista de participantes con números aleatorios
def generar_participantes():
    # Creo un array vacío para almacenar los participantes
    participantes = arr.array('i')

    # Genero 58 números aleatorios y los agrego al array de participantes
    for _ in range(58):
        participantes.append(random.randint(43158258, 44200952))
    # Devuelvo el array de participantes

    return participantes



# Función para elegir 3 ganadores de una lista de participantes
def elegir_ganadores(participantes):
    # Creo un array vacío para almacenar los ganadores
    ganadores = arr.array('i')

    # Elijo los 3 participantes de la lista
    for _ in range(3):
        # Mezclo aleatoriamente la lista de participantes
        random.shuffle(participantes)
        # Obtengo el último participante de la lista
        ganador = participantes.pop()
        # Agrego el participante a la lista de ganadores
        ganadores.append(ganador)

    # Devuelvo el array de ganadores
    return ganadores



# Función principal para realizar el sorteo
def sorteo():
    # Genero la lista de participantes llamando a la función generar_participantes
    participantes = generar_participantes()

    # Imprimo la lista de participantes
    print("Listado de participantes:")
    for participante in participantes:
        print(participante)

    # Llamo a la función elegir_ganadores para obtener la lista de ganadores
    ganadores = elegir_ganadores(participantes)

    # Imprimo la lista de ganadores
    print("\nGanadores:")
    for ganador in ganadores:
        print(ganador)



# Llamo al programa
sorteo()
