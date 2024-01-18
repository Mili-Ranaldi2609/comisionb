from herencia.classEjerc2 import Pajaro,Perro,Gato

perro1 = Perro("Max", 3, "Macho", "Labrador")
gato1 = Gato("Whiskers", 2, "Hembra", "Atigrado")
pajaro1 = Pajaro("Tweetie", 1, "Macho", "Canario")

# Llamar a hacer_sonido() e informacion() para cada instancia
perro1.hacer_sonido()
perro1.informacion()
print("\n")

gato1.hacer_sonido()
gato1.informacion()
print("\n")

pajaro1.hacer_sonido()
pajaro1.informacion()