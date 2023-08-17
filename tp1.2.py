"""Trabajo Practico 1.2"""

#Ejercicio 1

base=float(input("Ingrese el valor de la base del rectangulo: "))
altura=float(input("Ingrese el valor de la altura del rectangulo: "))

area_rectangulo=base*altura
perim_rectangulo=(base*2)+(altura*2)

print(f'El area del rectangulo es: {area_rectangulo}.\n El perimetro del rectangulo es: {perim_rectangulo}')

#Ejercicio 2

cateto1=float(input("Ingrese el valor del primer cateto: "))
cateto2=float(input("Ingrese el valor del segundo cateto: "))

hipotenusa=((cateto1)**2+(cateto2)**2)

print(f'La hipotenusa del triangulo es: {hipotenusa}')