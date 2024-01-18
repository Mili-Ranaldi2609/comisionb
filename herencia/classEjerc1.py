#Clase Padre 1
class Vehiculo:
    def __init__(self,color, ruedas):
        self.color= color
        self.ruedas=ruedas

#Clase HIJA 2 (coche)
class Coche(Vehiculo):
    def __init__(self,color,ruedas,velocidad,cilindrada):
        super().__init__(color,ruedas)
        self.velocidad=velocidad
        self.cilindrada=cilindrada
#Clase HIJA 2 (bicicleta)
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

#Clase subhija 3(camioneta)
class Camioneta(Coche):
    def __init__(self,color,ruedas,velocidad,cilindrada, carga):
        super().__init__(color,ruedas,velocidad,cilindrada)
        self.carga=carga


#Clase subhija 3(motocicleta)
class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilind):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilind = cilind
