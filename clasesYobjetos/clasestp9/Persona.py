class Persona:
    def __init__(self,nombre="", edad=int, dni=int):
        self.nombre=nombre
        self.edad=edad
        self.dni=dni
    def set_nombre(self):
        n=""
        if isinstance(n, str):
            self.n=self.nombre
        else:
            print("Error: El nombre debe ser una cadena de texto.")
    def get_nombre(self):
        return self.nombre
    
    def set_edad(self):
        ed=self.edad
        if isinstance(ed, int) and ed>= 0:
            self.ed=ed
        else:
            print("Error: La edad debe ser un número entero no negativo.")
    
    def get_edad(self):
        return self.edad
    
    def set_dni(self):
        id=self.dni
        if isinstance(id,int) and (len(str(id)) == 9 or len(str(id))==8):
            self.id=id
        else:
            print("Error: El DNI debe ser de 8 o 9 caracteres.")
    def get_dni(self):
        return self.dni
    
    def mostrar(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("DNI: ", self.dni)
    
    def esMayorDeEdad(self):
        return self.edad >= 18
