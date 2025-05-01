"""
DIFICULTAD EXTRA (opcional):
 Crea una función que sea capaz de procesar parámetros, pero que también
 pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 corresponderse con un tipo de excepción creada por nosotros de manera
 personalizada, y debe ser lanzada de manera manual) en caso de error.         
 - Captura todas las excepciones desde el lugar donde llamas a la función.
 - Imprime el tipo de error.
 - Imprime si no se ha producido ningún error.
 - Imprime que la ejecución ha finalizado.
"""

class StrTypeError(Exception):
    pass

def procesar_parametros(parametros: list):

    if len(parametros) < 3:
        raise IndexError()
    elif (parametros[1] == 0):
        raise ZeroDivisionError()
    elif (type(parametros[2]) == str):
        raise StrTypeError("El elemento no puede ser de tipo texto")
    
    print(parametros[2])
    print(parametros[0]/parametros[1])
    print(parametros[2]+5)

try:
    procesar_parametros([1,7,9])
except IndexError as e:
    print("La cantidad de elementos debe ser mayor a 2")
except ZeroDivisionError as e:
    print("El 2do elemento de la lista no puede ser 0")
except StrTypeError as e:
    print(f"{e}")
except Exception as e:
    print(f"Se produjo una excepcion: {e}")
else:
    print("No se produjo excepcion")
finally:
    print("Finaliza el programa")