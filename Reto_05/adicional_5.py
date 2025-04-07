"""POR VALOR"""

valor_a = 20
valor_b = 50

def cambio_de_valores(parametro_a: int, parametro_b:int) -> tuple:
    temp = parametro_a
    parametro_a = parametro_b
    parametro_b = temp
    return (parametro_a, parametro_b)

valor_c, valor_d = cambio_de_valores(valor_a, valor_b)
print(valor_c)
print(valor_d)



"""POR REFERENCIA"""

def cambio_por_referencia(lista_a:list, lista_b:list) -> tuple:
    temp = lista_a
    lista_a = lista_b
    lista_b = temp
    return lista_a, lista_b

list_1 = [50,100]
list_2 = [200,300]
list_3, list_4 = cambio_por_referencia(list_1, list_2)
print(f"{list_1} {list_2}")
print(f"{list_3} {list_4}")
