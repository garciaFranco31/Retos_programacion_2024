path='Reto_11\\nanoidk.txt'

"""
Con w lo que se hace es aunque el archivo exista, borrarlo y volverlo a crear. Cuando utilizamos a, se abre el archivo y lo que se quiera agregar, se agrega al final
"""

fichero = open(path,'w')
name="Franco"
age="24"
lang="Python"
fichero.write(name)
fichero.write(age)
fichero.write(lang)
fichero.close()

fichero = open(path,'r')
lineas = fichero.readlines()
for linea in lineas:
    print(linea)
fichero.close()


path = 'Reto_11\\deportes.txt'
fichero=open(path,'a')
lista = ["Natacion","Futbol","Basket"]

for sport in lista:
    fichero.write(sport + "\n")

fichero.close()

path = 'Reto_11\\nuevo_archivo.txt'
fichero = open(path, 'a')

mascotas = ["Gato\n", "Perro\n", "Pez\n"]
fichero.writelines(mascotas)
fichero.close()