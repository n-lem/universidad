# Realice un código que implemente un TDA que defina una clase Coche con 
# métodos: guardar_en_archivo y leer_desde_archivo la información del coche 
# en un archivo.

# El método guardar_en_archivo abre el archivo en modo de 
# escritura (“w”) y escribe la  información del coche en él. 

# El método leer_desde_archivo abre el mismo archivo en modo de lectura 
# (“r”) y lee la información del coche desde él.

# Por último, cree un objeto Coche, que guarde en el archivo información 
# sobre un coche en particular y luego lea la misma información desde el 
# mismo archivo.

# Importo la librería io
import io

# Defino una clase para representar un coche
class Coche:
    # Inicializo el constructor tomando como parámetro la marca, el modelo y el color del coche
    def __init__(self, nombre_archivo, marca, modelo, color):
        self.nombre_archivo = nombre_archivo
        self.marca = marca
        self.modelo = modelo
        self.color = color

    # Defino el método para escribir la información del coche en un archivo
    def guardar_en_archivo(self):
        # Abro el archivo, definido en la variable global, en modo de escritura ('w')
        archivo = open(self.nombre_archivo, "w")

        # Escribo la marca, el modelo y el color del coche en el archivo
        archivo.write(f'Marca: {self.marca}\n')
        archivo.write(f'Modelo: {self.modelo}\n')
        archivo.write(f'Color: {self.color}\n')
        # archivo.write(f'{self.marca},{self.modelo},{self.color}') # Guardar datos en una línea

        # Cierro el archivo
        archivo.close()

    # Defino el método para leer la información del coche desde un archivo
    def leer_desde_archivo(self):
        # Abro el archivo, definido en la variable global, en modo de lectura ('r')
        archivo = open(self.nombre_archivo, "r")

        # Devuelvo el contenido del archivo
        return archivo.read()

# Creo un objeto Coche con la marca 'Ford', modelo 'Fiesta' y color 'Rojo'
mi_coche = Coche('coche.txt','Ford', 'Fiesta', 'Rojo')

# Guardo la información del coche en el archivo 'coche.txt'
mi_coche.guardar_en_archivo()

# Leo la información del coche desde el archivo 'coche.txt' e imprimo el resultado
print(mi_coche.leer_desde_archivo())

