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

#Ejercicio 3

print("Vamos a realizar la suma, resta, division y multiplicacion de dos numeros que ingreses: ")

num1=float(input("Primer numero: "))
num2=float(input("Segundo numero: "))

suma=num1+num2
resta=num1-num2
multi=num1*num2
div=num1/num2

print(f"Resta: {num1}-{num2}={resta}.")
print(f"Suma: {num1}+{num2}={suma}.")
print(f"Multiplicacion: {num1}*{num2}={multi}.")
print(f"Division: {num1}/{num2}={div}")

#Ejercicio 4

print("Convertiremos un valor en grados Fahrenheit a grados Celsius: ")

fahre=float(input("Ingrese el valor en Fahrenheit: "))
celsius=(fahre-32)*5/9

print(f"El valor en Celsius seria: {celsius}")

#Ejercicio 5

    #a
nombre=input("¿Cual es tu cancion favorita? ")
    #b
precio=int(input("Precio: "))
total=precio+(precio*0.1)
    #c
edad=int(input("Edad: "))
print("Tu edad es ", edad)
    #d
edad2=int(input("Edad: "))
edad18=bool(edad2==18)
print("Veamos si tu edad es 18: ", edad18)

#Ejercicio 6

print("Vamos a sacar el promedio de 3 numeros")
val1=float(input("Ingrese el primer numero: "))
val2=float(input("Ingrese el segundo numero: "))
val3=float(input("Ingrese el tercer numero: "))

promedio_v=(val1+val2+val3)/3
print(f"El promedio final es: {promedio_v} ")

#Ejercicio 7

minutos=int(input("Ingrese la cantidad de minutos: "))
horas=minutos//60
min_restantes= minutos%60
print(f"Los minutos convertidos en horas son: {horas}:{min_restantes}")

#Ejercicio 8

print("Calcularemos tu sueldo total")

sueldo_base=int(input("Sueldo base: "))
cant_ventas=int(input("Cantidad de ventas: "))
extra=(sueldo_base*(10*cant_ventas))/100
sueldo_total=sueldo_base+extra

print(f"Tu sueldo final es de: {sueldo_total}")

#Ejercicio 9

print("Calculemos el monto que deberas pagar: ")
compra=float(input("Ingrese el precio de la compra:"))
descuento=float(compra-(100*0.15))
print(f"Lo que debera pagar es: ${descuento}")

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

#Ejercicio 15

print("Vamos a calcular la hora de llegada de un ciclista de la ciudad A hasta la ciudad B")

hora_p=int(input("Hora/s de partida: "))
min_p=int(input("Minuto/s de partida: "))
seg_p=int(input("Segundo/s de partida:"))

seg_viaje=int(input("Tiempo de viaje en segundos: "))

seg_i=hora_p*3600+min_p*60+seg_p
seg_f=seg_p+seg_i
hora_llegada=seg_f//3600
min_llegada=(seg_f%3600)//60
seg_llegada=(seg_f%3600)%60

print(f"Hora de llegada: {hora_llegada}:{min_llegada}:{seg_llegada} ")
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
servicio=cena*(6.2/100)
propina=cena*(10/100)
pagar= propina + servicio + cena
print(f"El costo de la cena con la propina y el servicio recibido es: ${pagar}")

#Ejercicio 19

import datetime

dia=int(input("Ingrese su dia de nacimiento: "))
mes=int(input("Ingrese su mes de nacimiento: "))
anio=int(input("Ingrese su año de nacimiento: "))

print("Tu fecha de nacimiento en formato ddmmaaa es: ")
print(datetime.date(anio, mes, dia).strftime('%d/%m/%Y'))

#Ejercicio 20

completo = input("ingrese su dia de nacimiento mes y año: ")
dia=completo[:2]
mes=completo[2:4]
anio=completo[4:]

print(f"{dia}/{mes}/{anio}")

#Ejercicio 21

print("Necesitamos hacer ciertos cálculos antes de emprender un viaje en moto: ")

km_por_litro=int(input("¿Cuantos kilometros puede recorrer su moto con 1 litro de combustible?: "))
km_a_recorrer=int(input("¿Cuantos kilometros van a recorrer?: "))
capacidad_del_tanque=int(input("¿De cuantos litros es su tanque?: "))
tanques=(km_a_recorrer/km_por_litro)/capacidad_del_tanque

print(F"Necesitan {tanques} tanques de combustible. ")





