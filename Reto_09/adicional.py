""" 
 DIFICULTAD EXTRA (opcional):
 Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 Cada empleado tiene un identificador y un nombre.
 Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 actividad, y almacenan los empleados a su cargo.
"""

class Empleado:
    identificador: int
    nombre: str
    empleados: list

    def __init__(self, identificador, nombre):
        self.identificador = identificador
        self.nombre = nombre
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def mostrar_empleados(self):
        for emp in self.empleados:
            print(emp.nombre)

class Manager(Empleado):

    def coordinar(self):
        print(f"{self.nombre} está coordinando todos los proyectos")

class Project_Manager(Empleado):
    proyecto: str
    def __init__(self, identificador, nombre, proyecto):
        super().__init__(identificador, nombre)
        self.proyecto = proyecto


    def coordinar_proyecto(self):
        print(f"{self.nombre} está coordinando el proyecto {self.proyecto}")

class Programador(Empleado):
    lenguaje:str

    def __init__(self, identificador, nombre, lenguaje):
        super().__init__(identificador, nombre)
        self.lenguaje = lenguaje
    
    def mostrar_lenguaje(self):
        print(f"{self.nombre} programa utilizando {self.lenguaje}")

    def agregar_empleado(self, empleado):
        print(f"Un programador no puede tener empleados, no se agregara a {empleado.nombre}")

    def mostrar_empleados(self):
        for emp in self.empleados:
            print(emp.nombre)

manager = Manager(12, "Franco")
project_manager = Project_Manager(43, "Ander", "Liga TTNB")
programador1 = Programador(98, "Bardo", "Python")
programador2 = Programador(93, "Zelda", "Java")

manager.agregar_empleado(project_manager)
project_manager.agregar_empleado(programador1)
project_manager.agregar_empleado(programador2)


manager.mostrar_empleados()

project_manager.coordinar_proyecto()
project_manager.mostrar_empleados()

programador1.mostrar_lenguaje()
programador2.mostrar_lenguaje()

programador3 = Programador(87, "Gervarsio", "Go")
programador1.agregar_empleado(programador3)
programador1.mostrar_empleados()