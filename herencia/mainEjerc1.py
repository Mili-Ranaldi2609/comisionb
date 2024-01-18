from herencia.classEjerc1 import Camioneta,Motocicleta

camioneta1=Camioneta("Roja",4,100,1200,"Carga pesada")
print("Detalles de la camioneta:")
print(f"Color: {camioneta1.color}")
print(f"Ruedas: {camioneta1.ruedas}")
print(f"Velocidad del coche: {camioneta1.velocidad}km/h")
print(f"Cilindrada del coche: {camioneta1.cilindrada}cc")
print(f"Carga: {camioneta1.carga}")

moto1=Motocicleta("Rosa",2,"Deportiva",300,200)
print("Detalles de la motocicleta:")
print(f"Color: {moto1.color}")
print(f"Ruedas: {moto1.ruedas}")
print(f"Tipo de vehiculo:{moto1.tipo}")
print(f"Velocidad del coche: {moto1.velocidad}km/h")
print(f"Cilindrada del coche: {moto1.cilind}cc")
