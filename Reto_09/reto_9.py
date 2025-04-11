class Animal:
    especie: str
    edad: int

    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    def hablar(self):
        pass

    def moverse(self):
        pass

    def descripcion(self):
        print(f"Soy un animal del tipo {type(self).__name__}")

class Perro(Animal):
    raza: str

    def __init__(self,especie, edad, raza):
        super().__init__(especie,edad)
        self.raza = raza
    
    def hablar(self):
        print("Guau")

    def moverse(self):
        print("Camina en 4 patas")

class Gato(Animal):
    
    def hablar(self):
       print("Miau")

    def moverse(self):
        print("Camina en 4 patas")

mi_perro = Perro("Mamífero", 3, "Labrador")
mi_perro.hablar()
mi_perro.moverse()
mi_perro.descripcion()

mi_gato = Gato("Mamifero", 1)
mi_gato.hablar()
mi_gato.moverse()
mi_gato.descripcion()