"""
DIFICULTAD EXTRA (opcional):
 Desarrolla un programa de gestión de ventas que almacena sus datos en un 
 archivo .txt.
 - Cada producto se guarda en una línea del archivo de la siguiente manera:
   [nombre_producto], [cantidad_vendida], [precio].
 - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar, actualizar, eliminar productos y salir.
 - También debe poseer opciones para calcular la venta total y por producto.
 - La opción salir borra el .txt.
"""

path = 'Reto_11\\nano_store.txt'
import os

#open(path,'a')

while True:
    print("1.Añadir")
    print("2.Consultar")
    print("3.Actualizar")
    print("4.Eliminar")
    print("5.Salir")

    opt = input("Seleccione una opcion: ")

    if opt == "1":
        name=input("Nombre: ")
        cant=input("Cantidad: ")
        precio=input("Precio: ")
        
        with open(path,'a') as file:
            file.write(f"{name}, {cant}, {precio}\n")
        
    elif opt == "2":
        name = input("Nombre: ")
        with open(path, 'r') as file:
            for line in file.readlines():
                if line.split(", ")[0] == name:
                    print(line)
                    break
    elif opt == "3":
        name=input("Nombre: ")
        cant=input("Cantidad: ")
        precio=input("Precio: ")

        with open(path, 'r') as file:
            lineas = file.readlines()

        with open(path, 'w') as file:
            for line in lineas:
                if line.split(", ")[0] == name:
                    file.write(f"{name}, {cant}, {precio}\n")
                else:
                    file.write(line)
            
    elif opt == "4":
        name=input("Nombre: ")
        with open(path, 'r') as file:
            lineas = file.readlines()
        with open(path,'r') as file:
            for line in lineas:
                if line.split(", ")[0] != name:
                    file.write(line)
    elif opt == "5":
        os.remove(path)
        break
