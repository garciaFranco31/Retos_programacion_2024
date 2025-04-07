"""
Parámetros por valor
- Cuando pasamos un parámetro por valor a una función, se crea una copia local de la variable, por lo tanto cualquier modificación que se le haga no modificará el valor final de dicha variable.

"""

num = 10
print(f"Antes de la función: {num}" )

def modificacion(por_valor):
    por_valor=100
    print(f"Dentro de la función: {por_valor}")

modificacion(num)
print(f"Luego de la función: {num}")

"""
Parámetros por referencia
- Cuando se pasa un parámetro por referencia a una función, se trabaja directamente sobre la variable pasada, por lo tanto, cualquier modificación que se le haga, modificará el valor final de dicha variable.

"""

lista = [10, 15, 20, 25]
print(f"Antes de la función: {lista}")

def modificador_lista(por_referencia):
    por_referencia.append(200)
    por_referencia = [] #por mas que se pase por referencia, esto no destruye la lista original.
    print(f"Dentro de la función: {por_referencia}")

modificador_lista(lista)
print(f"Luego de la función: {lista}")


"""Información sacada de: https://ellibrodepython.com/paso-por-valor-y-referencia"""