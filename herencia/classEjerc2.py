#clase padre 1:
class Animal:
    def __init__(self,nombre,edad,genero):
        self.nombre= nombre
        self.edad=edad
        self.genero=genero
    def hacer_sonido(self):
        print("El animal hace un sonido generico")

    def informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Genero: {self.genero} ")
#CLASES DERIVADAS 
class Perro(Animal):
    def __init__(self, nombre, edad, genero, raza):
        super().__init__(nombre, edad, genero)
        self.raza=raza
    def hacer_sonido(self):
        print("El perro ladra.")   

    def informacion(self):
        super().informacion()
        print(f"Raza: {self.raza}")

class Gato(Animal):
    def __init__(self, nombre, edad, genero,color):
        super().__init__(nombre, edad, genero)
        self.color=color
    def hacer_sonido(self):
        print("El gato maulla")
    def informacion(self):
        super().informacion()
        print(f"Color del gato: {self.color}")

class Pajaro(Animal):
    def __init__(self, nombre, edad, género, especie):
        super().__init__(nombre, edad, género)
        self.especie = especie

    def hacer_sonido(self):
        print("El pajaro canta.")

    def informacion(self):
        super().informacion()
        print(f"Especie: {self.especie}")