class Cuenta:
    def __init__(self, titular="", cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    def get_titular(self):
        return self.titular

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.cantidad = cantidad
        else:
            print("Error: La cantidad no puede ser negativa.")

    def mostrar(self):
        print(f"Titular: {self.titular}")
        print(f"Cantidad: {self.cantidad}")

    def ingresar(self, cant):
        if cant >= 0:
            self.cantidad += cant
            print("Se ha ingresado el monto de ", cant)
            print("Ahora tiene en la cuenta: ",self.cantidad)
        else:
            print("Error: No se puede ingresar una cantidad negativa.")

    def retirar(self, cant):
        self.cantidad -= cant
        print("Se ha retirado el monto de ",cant)
        print("Ahora tiene en la cuenta: ",self.cantidad)
