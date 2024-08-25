'''
Este código crea una base de datos simple de productos que se almacenan en un archivo\n
de texto llamado "lista_productos.txt". Usted puede agregar y mostrar productos\n
utilizando las opciones del menú. Los productos se cargan desde el archivo al iniciar el programa\n
y se guardan en el archivo cuando se realizan cambios.

'''

import os

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class ProductoDatos:
    def __init__(self, archivo):
        self.archivo = archivo
        self.lista_productos = []

    def cargar_datos(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, 'r') as arch:
                lista_lineas = arch.readlines()
                for linea in lista_lineas:
                    nombre, precio = linea.strip().split(',')
                    self.lista_productos.append(Producto(nombre, float(precio)))

    def guardar_datos(self):
        with open(self.archivo, 'w') as arch:
            for producto in self.lista_productos:
                arch.write(f"{producto.nombre},{producto.precio}\n")

    def agregar_producto(self, nombre, precio):
        producto_nuevo = Producto(nombre, precio)
        self.lista_productos.append(producto_nuevo)
        self.guardar_datos()


    def listar_productos(self):
        print()
        for producto in self.lista_productos:
            print(f"{producto.nombre}: ${producto.precio:.2f}")

    def eliminar_producto(self, nombre):
        for producto in self.lista_productos:
            if producto.nombre == nombre:
                self.lista_productos.remove(producto)
        self.guardar_datos()
    
    def modificar_producto(self, nombre_antiguo, nuevo_nombre, nuevo_precio):
        for producto in self.lista_productos:
            if producto.nombre == nombre_antiguo:
                producto.nombre = nuevo_nombre
                producto.precio = float(nuevo_precio)

        self.guardar_datos()

# Creamos un objeto de tipo ProductoDatos con el nombre stock
# y en el mismo enviamos el nombre del archivo de texto llamado lista_productos.txt
# con el que vamos a trabajar

stock = ProductoDatos("lista_productos.txt")

# Cargamos los datos
stock.cargar_datos()

def pausa():
    input("\nIngrese ENTER para continuar")
    
while True:
    print("\nMenú de opciones:")
    print("1. Agregar producto")
    print('2. Eliminar producto')
    print('3. Modificar producto')
    print("4. Mostrar productos")
    print("5. Salir")
    choice = input("Seleccione una opción: ")

    if choice == '1':
        nombre = input("\nNombre del producto: ")
        precio = float(input("Precio del producto: "))
        stock.agregar_producto(nombre, precio)

    elif choice == '4': #mostrar
        stock.listar_productos()
    
    elif choice == '2': #eliminar
        nombre = input("\nNombre del producto: ")
        stock.eliminar_producto(nombre)

    elif choice == '3': #modificar
        nombre_antiguo = input("\nNombre del producto: ")
        nuevo_nombre = input('\nIngresá el nuevo nombre: ')
        nuevo_precio = float(input('\nIngresá el nuevo precio: '))
        stock.modificar_producto(nombre_antiguo, nuevo_nombre, nuevo_precio)

    elif choice == '5':
        break
    else:
        print("Opción no válida. Intente de nuevo.")
    
    pausa()
