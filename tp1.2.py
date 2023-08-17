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
