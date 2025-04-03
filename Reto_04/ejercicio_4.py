"""STRINGS
Es un tipo de dato inmutable, el cual permite almacenar secuencias de caracteres.
Para crear un string, el texto debe ponerse entre comillas dobles o simples.
"""

string = "esto es un string" # declaracion
string_vacio = " "
print("\110") #H, usando la barra invertida podemos imprimir ASCII

#OTRAS FORMAS DE IMPRIMIR CADENAS
name = "franco"
cadena = "Nombre: " + str(name)
print(cadena)

cadena2 = "Numeros: {} y {}".format(4,5)
print(cadena2)

cadena3 = "Numeros %d y %d"%(10,11)
print(cadena3)

cadena4 = "Numeros {a} y {b}".format(a=3, b=29)
print(cadena4)

a=59
b=72
cadena5 = f"Numeros son {a} y {b}" #esto se llama fstring
print(cadena5)

#utilizando fstrings, dentro de las llaves podemos realizar operaciones y llamar funciones
a=59
b=72
cadena6 = f"Numeros son {a} y {b}" #esto se llama fstring
print(cadena6)

def funcion():
    print("hola desde la funcion")
cadena7 = f"Numeros son {funcion()}" #esto se llama fstring
print(cadena7)

#OPERACIONES
#Los strings se pueden sumar
s1 = "hola"
s2 = "persona"
print(s1 + " " +s2) #hola persona

#Se pueden multiplicar por un entero
s3 = "franco"
print(s3*4) #franco franco franco franco

#Ver si una cadena esta dentro de otra
s4 = "hola mundo"
print("hola" in s4) #True

#Saber la longitud de una cadena
print(len("hola como estas"))

#Indexar como si fuesen listas
s5 = "abcde"
print(s5[0]) #a
print(s5[-1]) #e
print(s5[0:2]) #ab
print(s5[3:]) #de
print(s5[0:5:2]) #ace -> se toman los elementos del 0 al 5, salteando de 2 en 2
print(s5[0::2]) #ace -> igual que el anterior, pero sin determinar el tamaño de la cadena, util cuando no lo conocemos.
print(s5[0:len(s5):2]) #ace

#MÉTODOS
capi = "mi cadena"
print(capi.capitalize()) #"Mi cadena"

low = "MI CADENA"
print(low.lower()) #"mi cadena"

up = "mi cadena"
print(up.upper()) #"MI CADENA"

swp = "Mi Cadena"
print(swp.swapcase()) #mI cADENA

s6 = "bello cuello"
print(s6.count("llo")) #2 -> cuenta la cant de veces que aparece el string en la cadena

#isalnum() devuelve True si la cadena solamente esta formada por car alganumericos
s = "correo@dominio.com"
print(s.isalnum()) #False

#devuelve True si todos los caracteres son alfabeticos
s = "abcdefg"
print(s.isalpha()) #True

#strip(par) elimina el caracter enviado a la izq y a la der
s = "  abc  "
print(s.strip()) #abc
s = "  abc  "
print(s.strip("%")) #"  abc  "

#zfill(par) llena la cadena con 0 a la izq, la cant depende del par
s = "123"
print(s.zfill(5)) #00123

#join() recibe una lista y devuelve una cadena unida con cada elemento de la lista
cad = "Numeros ".join(["1","2","3"])
print(cad) #1Numeros 2Numeros 3

#split(sep,maxsplit) divide una cadena en subcadenas y las devuelve almacenadas en una lista. La división se realiza según el 1er parámetro
divido = "Python, Java, Go, C"
print(divido.split(",")) #'Python', ' Java', ' Go', ' C']
#el parametro maxsplit indica la cantidad de separaciones que va a hacer
print(divido.split(",",0)) #['Python, Java, Go, C'] no hace splits
print(divido.split(",",2)) #['Python', ' Java', ' Go, C'], hace 2 splits