class inicializador:
    #atributos de la clase inicializador
    nombre: str
    apellido: str

    #constructor de la clase, se llama siempre que vamos a intanciar un objeto
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    #método de la clase, se pueden definir varios en una misma clase
    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")


objeto = inicializador("Franco", "Garcia") #se instancia el objeto de la clase inicializador
objeto.imprimir() #se imprimen los atributos del objeto