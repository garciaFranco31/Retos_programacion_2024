#Utilizando rise podemos levantar excepciones manualmente
#raise ZeroDivisionError("Excepcion")
#raise NameError("Información de la excepcion")

#Manejo de excepciones para que no se pare el programa, usamos try except
a = 10
b = 0

try:
    #Tenemos el código que puede causar una excepcion/error que pare la ejecucion del programa
    print(a/b)
except ZeroDivisionError:
    #Captura la excepcion y se realizan opciones alternativas sin que se pare el programa
    print("No se puede realizar divisiones por 0")

print("segunda parte")

try:
    c = 5 + "hola"
    d = 2/0
except TypeError:
    print("No se pude sumar numeros con strings")
    c = 5 + 20
    print(f"{c}")
except ZeroDivisionError:
    print("No se pueden realizar diviosiones por 0")

print("TERCERA PARTE")

# try:
#     e = 5 + "chau"
#     f = 10/0
# except(ZeroDivisionError, NameError):
#     print("Surgió un error en la ejecución")

try:
    e = 5 + "chau"
    f = 10/0
except Exception as ex:
    print(type(ex))

try:
    e = 5 + "chau"
    f = 10/0
except Exception:
    print("Hubo una excepcion")

print("CUARTA PARTE - Uso de else")
try: 
    div = 2/0
except Exception as exc:
    print(f"Hubo una excepcion del tipo: {type(exc)}")
else:
    print(f"No hubo excepcion, el resultado es: {div}")

print("QUINTA PARTE - Uso del Finally")
#Finally se ejecuta siempre, haya o no habido una excepcion
try: 
    div = 5/0
except Exception as exc:
    print(f"Hubo una excepcion del tipo:{type(exc)}")
else:
    print(f"No hubo excepcion, resultado: {div}")
finally:
    print("Siempre se ejecuta el finally")