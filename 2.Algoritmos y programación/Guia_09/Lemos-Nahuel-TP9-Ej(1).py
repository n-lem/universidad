# Crear un programa que abra un fichero en modo lectura y escritura, si no existe lo creará, y
# añadir la frase ‘Este es el ejercicio 1’.

# La libreria permite trabajar con archivos. 'io' viene de input/output
import io

# Creo una funcion para escribir un archivo
def escribir_archivo(nombre_archivo, estado):
    # Abro el archivo en modo escritura
    archivo = open(nombre_archivo, estado)

    # Mensaje a guardar
    archivo.write('Este es el ejercicio 1')
    
    # Cierro el programa
    archivo.close()

# Ejecuto el programa
escribir_archivo('archivo_ejercicio_9_1.txt', 'w')