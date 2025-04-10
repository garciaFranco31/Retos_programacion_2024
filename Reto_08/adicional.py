class Stack:
    stack: list

    def __init__(self):
        self.stack = []

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        return self.stack.pop(-1)

    def imprimir(self):
        print(self.stack)

pila = Stack()
pila.imprimir()
pila.push(5)
pila.push(6)
pila.push(7)
pila.imprimir()
pila.pop()
pila.imprimir()

class Queue:
    queue: list

    def __init__(self):
        self.queue = []
    
    def push(self, elem):
        self.queue.append(elem)
    
    def pop(self):
        self.queue.pop(0)

    def imprimir(self):
        print(self.queue)

cola = Queue()
cola.imprimir()
cola.push(1)
cola.push(2)
cola.push(3)
cola.imprimir()
cola.pop()
cola.imprimir()