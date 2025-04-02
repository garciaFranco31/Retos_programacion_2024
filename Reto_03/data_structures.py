"""Listas
Estructura en la que se pueden almacenar datos de cualquier tipo. Son mutables (pueden modificarse una vez que fueron creadas) y dinámicas.
Son ordenadas (mantienen el orden en el que fueron definidas), se puede acceder a una posición particular por medio de la utilización de un índice, se pueden anidar (meter una lista dentro de otra), sus elementos pueden modificarse (mutables) y se les puede añadir o eliminar elementos (dinámicas).
"""
lista = [1,2,"hola",["coso",4,5]]
numeros = list("12345")

print(lista)
print(numeros)
print(lista[2]) #hola
print(lista[0:2]) #[1,2]
print(lista[1:3]) #[2, 'hola']
print(lista[-1]) #['coso', 4, 5]

#Iterando listas

for i in lista:
    print(i)

for i in range(0, len(lista)):
    print(lista[i])

#Modificando listas
del lista[1] #elimina el elemento en la pos 1 de la lista
print(lista) #[1, 'hola', ['coso', 4, 5]]

lista.append("Andy") #agrega el elemento al final de la lista
print(lista) # [1, 'hola', ['coso', 4, 5], 'Andy']

lista.extend([10,11]) #añade una nueva lista a la lista original
print(lista) #[1, 'hola', ['coso', 4, 5], 'Andy', 10, 11]

lista.insert(0,"Franco") #agrega un nuevo elemento en la pos indicada
print(lista) #['Franco', 1, 'hola', ['coso', 4, 5], 'Andy', 10, 11]

lista.remove(1) #elimina el elemento pasado por parámetro, si no existe da error
print(lista) #['Franco', 'hola', ['coso', 4, 5], 'Andy', 10, 11]

lista.pop() #elimina por default el último elemento de la lista
print(lista) #['Franco', 'hola', ['coso', 4, 5], 'Andy', 10]

lista.reverse() #invierte el orden la lista
print(lista) #[10, 'Andy', ['coso', 4, 5], 'hola', 'Franco']

print(lista.index("Franco")) #devuelve el ìndice de la primer aparición del objeto

#existe también el método sort para ordenar las listas de menor a mayor, este método puede tener el valor reverse=True (sort(reserse=True)), el cual ordena la lista de mayor a menor.

"""SET
Permiten almacenar elementos inmutables. Cada elemento es único (no puede haber repetidos) y son desordenados (no mantienen el orden de cuando son declarados). No pueden ser modificados (inmutables), es por esto que no pueden contener diccionarios ni listas.
"""

conjunto = set([4,5,6,8,8,1])
print(conjunto) #{1, 4, 5, 6, 8}

conjunto = {5,4,6,8,8,1} #{1, 4, 5, 6, 8}

#Iteración
conj = set({5,4,3})
for item in conj:
    print(item) #{5,4,3}

len(conj) #devuelve la longitud del conjunto

print(5 in conj) #True

# se pueden unir 2 o mas conjuntos con la operación union |
s1 = set([1, 2, 3])
s2 = set([3, 4, 5])
print(s1 | s2) #{1, 2, 3, 4, 5}

conj.add(6) #{5,4,3,6}
conj.remove(4) #{5,3,6}
conj.discard(5) #{3,6} si no encuentra el elemento no hace nada
conj.pop() #elimina un elemento aleatorio
conj.clear() #elimina todos los elementos

"""
Mas elementos de los conjuntos:
s1.union(s2[, s3 ...])
s1.intersection(s2[, s3 ...])
s1.difference(s2[, s3 ...])
s1.symmetric_difference(s2)
s1.isdisjoint(s2)
s1.issubset(s2)
s1.issuperset(s2)
s1.update(s2[, s3 ...])
s1.intersection_update(s2[, s3 ...])
s1.difference_update(s2[, s3 ...])
s1.symmetric_difference_update(s2)
"""

"""TUPLAS
Estructuras de datos inmutables (no se pueden modificar), se deben inicializar con parentesis.
"""

tupla = (1,2,3) # tambien se puede declarar tupla = 1,2,3
print(tupla) #(1,2,3)

tupla2 = (1,2,('a','b'),3,4)
print(tupla2) #(1,2,('a','b'),3,4)
print(tupla2[2][1]) # 'b'

tupla.count(2) #cuenta el numero de veces q el parametro esta en la tupla
tupla.index(3) #busca el obj pasado como parametro y devuleve el indice, si no lo encuentra devuelve error.
tupla.index(1,3) # busca el objeto 1 a partir de la 3er posicion.

"""DICCIONARIOS
Permite almacenar contenido en forma clave:valor. Son dinamicos (permite añadir o eliminar elementos), indexados (se puede acceder a los elementos por medio de un índice) y son anidados (un diccionario puede contener a otro en su interior).
"""

dic = {
    "Nombre":"Franco",
    "Edad": 23,
    "Deporte":"Natacion"
}
print(dic) #{'Nombre': 'Franco', 'Edad': 23, 'Deporte': 'Natacion'}

d2 = dict([
      ('Nombre', 'Sara'),
      ('Edad', 27),
      ('Documento', 1003882),
])

d3 = dict(Nombre='Sara',
          Edad=27,
          Documento=1003882
)

# Acceder y modificar

print(dic['Nombre']) #Franco
print(dic.get("Nombre")) #Franco

dic["Nombre"] = "Ander" #{'Nombre': Ander', 'Edad': 23, 'Deporte': 'Natacion'}

dic['Direccion'] = "Calle 57" # En caso de que la key no exista, se agrega automaticamente.

#{'Nombre': Ander', 'Edad': 23, 'Deporte': 'Natacion', 'Direccion':'Calle 57'}

#Iteracion

for elem in dic:
    print(elem)
#Imprime los key del diccionario
#Nombre
#Edad
#Deporte

for elem in dic:
    print(dic[elem])
#Imprime los values:
#Franco
#23
#Natacion

for key,value in dic.items():
    print(key, value)

#Imprime el key y su value:
#Nombre Franco
#Edad 23
#Deporte Natacion

#Un diccionario puede contener uno o mas diccionarios en su interior.
anidado1 = {"a": 1, "b": 2}
anidado2 = {"a": 1, "b": 2}
d = {
  "anidado1" : anidado1,
  "anidado2" : anidado2
}
print(d)
#{'anidado1': {'a': 1, 'b': 2}, 'anidado2': {'a': 1, 'b': 2}}

d.clear() #elimina todos los elementos del diccionario

#Con el metodo get podemos consultar el value para un determinado key, podemos agregar un 2do parametro (no obligatorio) el cual sera devuelto en caso de que el valor no exista.
d = {'a': 1, 'b': 2}
print(d.get('a')) #1
print(d.get('z', 'No encontrado')) #No encontrado

#El metodo items devuelve una lista con los key y los values del diccionario. Si se convierte en un list, puede ser indexada como una lista normal.
d = {'a': 1, 'b': 2}
it = d.items()
print(it)             #dict_items([('a', 1), ('b', 2)])
print(list(it))       #[('a', 1), ('b', 2)]
print(list(it)[0][0]) #a

#El metodo keys devuelve una lista con los key del diccionario
d = {'a': 1, 'b': 2}
k = d.keys()
print(k)       #dict_keys(['a', 'b'])
print(list(k)) #['a', 'b']

#El metodo values devuelve una lista con los value del diccionario
d = {'a': 1, 'b': 2}
print(list(d.values())) #[1, 2]

#El metodo pop busca y elimina el key pasado como parametro y devuelve su valor asociado.

dict = {'Nombre':'Franco', 'Edad':23}
dict.pop('Edad')
print(dict)

# el 2do parametro sera devuelto en caso de que no exista el key buscado.
dict.pop('Calle', 'No existe')
print(dict)

#popitem() elimina de forma aleatoria un elemento del diccionario
dict1 = {'Nombre':'Ander', 'Edad':23}
dict.popitem()

#el metodo update() es llamado sobre un diccionario y contiene como entrada otro diccionario. Sirve para actualizar los value. Si alguna key del diccionario no está, es añadida

dict2 = {'Nombre':'Bardo', 'Edad':2}
print(dict2) #{'Nombre': 'Bardo', 'Edad': 2}
dict3 = {'Nombre':'Zelda', 'Color':'Gris', 'Especie':'Gato'}
dict2.update(dict3)
print(dict2) #{'Nombre': 'Zelda', 'Edad': 2, 'Color': 'Gris', 'Especie': 'Gato'}