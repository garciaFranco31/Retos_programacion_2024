num1=2
num2=5

def sumar():
    res = num1 + num2
    print(res)

sumar()


def restar(resta1, resta2):
    res = resta1-resta2
    return res

print(restar(3,4))


"""Se pueden crear funciones dentro de otras. Pero como puede verse en este caso, la función interna (función2) solamente 
puede ser declarada dentro del cuerpo de funcion1, ya que esta es la única que la conoce. Si quiero llamar a funcion2 por fuera
de funcion1 voy a tener un error."""
def funcion1():
    numerito = 5
    def funcion2():
        print("hola desde funcion 2")
    print("funcion 1")
    funcion2()
    print(numerito)

funcion1()

"""Como tengo num1 y num2 declarados por fuera de las funciones, estas variables las puedo utilizar en cualquier otra
función o parte del programa, son variables globales"""

print(num1)
#print(numerito) numerito al estar declarada dentro de una funcion da error.