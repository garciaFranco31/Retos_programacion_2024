
def imprimir_numeros(num):
    if num <= 5:
        print(num)
        num+=1
        imprimir_numeros(num)

imprimir_numeros(0)