#Calculo factorial

def factorial(num):
    if num == 0 or num == 1:
        return(1)
    else:
        return num * factorial(num-1)

print(factorial(0)) # 1
print(factorial(1)) # 1
print(factorial(5)) # 120

def fibonacci(pos:int) -> int:
    if pos <= 0:
        print("La posicion debe ser mayor que 0")
        return -1
    elif pos == 1:
        return 0
    elif pos == 2:
        return 1
    else:
        return fibonacci(pos-1)+fibonacci(pos-2)

print(fibonacci(5))
