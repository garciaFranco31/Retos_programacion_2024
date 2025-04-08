# Pilas - stacks LIFO

list = []

def agregar(elem:int):
  list.append(elem)

def sacar(q:list) -> int:
  return list.pop(-1)

agregar(4)
agregar(5)
agregar(6)
print(list)

print(sacar(list))
print(sacar(list))
print(sacar(list))

# Colas - queue FIFO

queue = []

def agregar(elem: int, q: list) -> list:
  return q.append(elem)

def sacar(q:list) -> int:
  return q.pop(0)

print(queue)

agregar(1, queue)
agregar(2, queue)
agregar(3, queue)

print(queue)

print(sacar(queue))
print(sacar(queue))
print(sacar(queue))
