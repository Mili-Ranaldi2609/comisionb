from Motocicleta import Motocicleta
motorcycle1=Motocicleta('Rosa','whjs123','Honda','CB500X',2023,185,199)
motorcycle2 = Motocicleta("Azul", "456XYZ", "Yamaha", "YZF-R1", 2023, 180, 190)
print("Motocicleta 1:")
motorcycle1.get_information()
motorcycle1.stopped_or_running()
motorcycle1.start_up()
motorcycle1.arrest()
print()
print("Motocicleta 2:")
motorcycle2.get_information()
motorcycle2.stopped_or_running()
motorcycle2.start_up()
motorcycle2.arrest()
print()

#se asigna un precio
motorcycle1.get_price(8000)
motorcycle2.get_price(200)
# Consulta de precio desde fuera de la clase
def check_te_price(moto):
    return moto.precio

precio_moto1 = check_te_price(motorcycle1)
#precio_moto2 = ckeck_te_price(motorcycle2)  # Esto generaría un error en moto2

print(f"El precio de la motocicleta '{motorcycle1.brand} {motorcycle1.model}' es de {precio_moto1} $.")
#print(f"El precio de la motocicleta '{motorcycle2.brand} {motorcycle2.model}' es de {precio_moto2} $.")