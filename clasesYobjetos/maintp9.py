from Persona import Persona
#1
persona1 = Persona()
persona1.set_nombre("Juan Pérez")
persona1.set_edad(25)
persona1.set_dni("123456789")
persona1.mostrar()
print("¿Es mayor de edad?", persona1.esMayorDeEdad())