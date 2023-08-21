"""Trabajo Practico 1.2"""

"""Integrantes del grupo: Milagros Ranaldi, Pia Lavilla, Julian Gonzalez, Valentina Lara, Ornela Condori, Venus Galiana"""

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

#Ejercicio 10

parcial1=float(input("Ingrese la nota del primer parcial: "))
parcial2=float(input("Ingrese la nota del segundo parcial: "))
parcial3=float(input("Ingrese la nota del tercer parcial: "))
examen_final=float(input("Ingrese la nota del examen final: "))
trabajo_final=float(input("Ingrese la nota  del trabajo final: "))

prom_p=(parcial1+parcial2+parcial3)/3

ppp=prom_p*0.55
pe=examen_final*0.30
pt=trabajo_final*0.15

nota_final=ppp+pe+pt

print(f'Su calificacion final de la materia seria: {int(nota_final)}')


#Ejercicio 11

print("Vamos a tomar la distancia entre dos numeros: ")
numd_1=float(input("Ingrese el primer numero "))
numd_2=float(input("Ingrese el segundo numero: "))

distancia=abs(numd_1-numd_2)

print(f'La distancia entre los dos numeros es de: {distancia}')

#Ejercicio 12

print("Vamos a calcular la raiz cuadrada y cubica del numero que elijas ")

numero_r=float(input("Ingresa el numero: "))

raiz_cubica_num=numero_r**(1/3)
raiz_cuadrada_num=numero_r**(1/2)

print(f"La raiz cuadrada de {numero_r} es de {raiz_cuadrada_num} y su raiz cubica es de {raiz_cubica_num}")

#Ejercicio 13

num_i=input("Ingrese un numero de dos cifras, (Por ejemplo: 20): ")
inverso=num_i[::-1]
print(f"El numero inverso es: {inverso}")

#Ejercicio 14

print("Ingresaremos dos numeros y los cambiaremos de lugar: ")
a=int(input("Numero 'A': "))
b=int(input("Numero 'B': "))

aux=a
a=b
b=aux

print(f"Ahora 'a' vale: {a} y 'b' vale: {b}")

#Ejercicio 16

print("Ahora te pediremos que ingreses tu nombre y tus dos apellidos:")

nombre=input( "Nombre: ")
primer_apellido =input( "Primer apellido: ")
segundo_apellido =input( "Segundo apellido: ")

inicales= (nombre[0]+", "+primer_apellido[0]+", "+segundo_apellido[0]+".").upper()

print (f"Sus iniciales son: {inicales} ")

#Ejercicio 17

usuario=input( "Ingrese su nombre: ")
print(f"Ahora estas en la matrix , [{usuario}]")

#Ejercicio 18

cena = float(input("Precio de la comida del Restaurante: "))
servicio=cena%6.2
propina=cena%10
cena+= propina + servicio 
print(f"El costo de la cena con la propina y el servicio recibido es: ${cena}")

#Ejercicio 19

import datetime

dia=int(input("Ingrese su dia de nacimiento: "))
mes=int(input("Ingrese su mes de nacimiento: "))
anio=int(input("Ingrese su año de nacimiento: "))

print("Tu fecha de nacimiento en formato ddmmaaa es: ")
print(datetime.date(anio, mes, dia).strftime('%d/%m/%Y'))

#Ejercicio 20

import datetime

dia=int(input("Ingrese su dia de nacimiento: "))
mes=int(input("Ingrese su mes de nacimiento: "))
anio=int(input("Ingrese su año de nacimiento: "))
fecha=datetime.date(anio, mes, dia).strftime('%d/%m/%Y')

print(f"La fecha con formato ddmmaaa es: {fecha}")

#Ejercicio 21

print("Necesitamos hacer ciertos cálculos antes de emprender un viaje en moto: ")

km_por_litro=int(input("¿Cuantos kilometros puede recorrer su moto con 1 litro de combustible?: "))
km_a_recorrer=int(input("¿Cuantos kilometros van a recorrer?: "))
capacidad_del_tanque=int(input("¿De cuantos litros es su tanque?: "))
tanques=(km_a_recorrer/km_por_litro)/capacidad_del_tanque

print(F"Necesitan {tanques} tanques de combustible. ")





