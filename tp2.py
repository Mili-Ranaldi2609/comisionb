"""Integrantes: Milagros Ranaldi, Pia Lavilla, Valentina Lara, Ornela Condori, Julian Gonzalez, Venus Galiana"""

#Ejercicio 1

anio_comp=int(input("Ingrese los años de su computador: "))

if anio_comp<=2:
    print("El computador es nuevo ")
else:
    print("El computador es viejo ")

#Ejercicio 2

anio_comp=int(input("Ingrese los años de su computador: "))

if anio_comp<0:

    print("No se puede ingresar un numero negativo ")

elif anio_comp<=2:
    print("El computador es nuevo ")
else:
    print("El computador es viejo ")

#Ejercicio 3

print("Te pediremos que ingreses dos nombres y los vamos a comparar: ")

nombre01=input("Nombre de la primer persona: ").capitalize()
nombre02=input("Nombre de la segunda persona: ").capitalize()

if nombre01[0]==nombre02[0]:
    print("Coincidencia ")
else:
    print("No hay coincidencia ")

#Ejercicio 4

"""upper() convierte en mayusculas"""
candidato_a="rojo"
candidato_b="verdad"
candidato_c="azul"

candidato_elegido=input("Ingrese el candidato que desea votar: A, B , C ").upper()

if candidato_elegido=="A":

    print(f"Usted ha votado por el partido: {(candidato_a).upper()}")
elif candidato_elegido=="B":

    print(f"Usted ha votado por el partido: {(candidato_b).upper()}")
elif candidato_elegido=="C":

    print(f"Usted ha votado por el partido: {(candidato_c).upper()}")

#Ejercicio 5

"""lower()convierte en minusculas"""

letra=input("Ingrese una letra: ").lower()

"""len indica la cantidad de caracteres"""
if len(letra)==1:
    if letra=="a" or letra=="e"or letra=="i" or letra=="o" or letra=="u":
        print(f"{letra}, es una vocal")
    else:
        print(F"{letra}, es una consonante")
else:
    print("ERROR, solo puede ingresar una letra.")

#Ejercicio 6

print("Veremos si el año que ingreses es bisiesto o no")

año=int(input("Año: "))

if (año%4==0 and año%100!=0) or año%400==0 :
    print(F"{año}, es un año bisiesto ")
else:
    print(f"{año}, no es un año bisiesto")

#Ejercicio 7

print("Le pediremos que ingrese 3 numeros: ")

num01=int(input("Numero (1): "))
num02=int(input("Numero (2): "))
num03=int(input("Numero (3): "))

if num01<num02 and num01<num03:
    print(f"{num01}, es el menor de los tres.")
elif num02<num01 and num02<num03:
    print(f"{num02}, es el menor de los tres.")
else:
    print(f"{num03}, es el menor de los tres.")

#Ejercicio 8
"""str es un string, guarda texto"""

usuario=str(input("Ingrese su usuario: "))
contrasenia=str(input("Ingrese su contraseña: "))

if usuario=="Gwenevere" and contrasenia=="excalibur":
    print("Usuario y contraseña correctos. Puede ingresar a Camelot.")
else:
    print("Acceso denegado.")

#Ejercicio 9

nombre=str(input("Ingrese su nombre: ")).upper()
sexo=str(input("Ingrese su sexo: F/M "))
sexo=sexo.upper()

if (sexo=="F" and nombre[0]<"M")  or(sexo=="M" and nombre[0]>"N"):
    print("Le corresponde el grupo 'A' ")
else:
    print("Le corresponde el grupo 'B' ")

#Ejercicio 10

print("Bienvenidos a la sala de juegos: ")

edad=int(input("Ingrese su edad: "))

if edad<4:
    print("Tiene la entrada gratuita")
elif edad>=4 and edad<=18:
    print("Tiene que pagar la entrada de $500")
else:
    print("Tiene que pagar la entrada de $1000")

#Ejercicio 11

print("Bienvenido a la pizzeria 'Bella Napoli' ")

pizza=str(input("Ingrese si quiere una pizza: (a)Vegetariana o (b)No vegetariana: "))
pizza=pizza.lower()

if pizza=="a":
    print("Los ingredientes que ya vienen con la pizza son: mozzarella y tomate ")
    ingr=str(input("Puede elegir uno de estos ingredientes: Pimiento/Tofu "))
    ingr=ingr.lower()
    print(f"Su pizza es vegetariana: los ingredientes que lleva son: Mozzarella, tomate y {ingr} ")
else:
    print("Los ingredientes que ya vienen con la pizza son: mozzarella y tomate ")
    ingr=str(input("Puede elegir uno de estos ingredientes: Pepperonni/Jamon/Salmon "))
    ingr=ingr.lower()
    print(f"Su pizza es no vegetariana: los ingredientes que lleva son: Mozzarella, tomate y {ingr} ")

#Ejercicio 12

anio_actual=int(input("Ingrese su año actual: "))
anio_cualquiera=int(input("Ingrese cualquier año: "))

suma_anio=anio_actual-anio_cualquiera
resta_anio=abs(anio_actual-anio_cualquiera)

if anio_actual>anio_cualquiera:
    print(f"Desde el año {anio_actual} hasta el año {anio_cualquiera} han pasado {suma_anio} años")
else:
    print(f"Desde el año {anio_actual} hasta el año {anio_cualquiera} faltan {resta_anio} años ")

#Ejercicio 13

print("Le pediremos que ingrese dos numeros enteros. ")
num_1=int(input("Numero 1: "))
num_2=int(input("Numero 2: "))

if num_1<=0 or num_2<=0:
    print("Ingreso de numeros negativos o nulos")
elif num_2>num_1:
    if num_2%num_1==0:
        print(f"{num_2} es multiplo de {num_1}")
    else:
        print("No son multiplos")
elif num_1>num_2:
    if num_1%num_2==0:
        print(f"{num_1} es multiplo de {num_2}")
else:
        print("No son multiplos")

#Ejercicio 14

print("Le pediremos que ingrese los coeficientes de una ecuacion de primer grado (ax+b=0)")

a=int(input("Valor de 'a': "))
b=int(input("Valor de 'b': "))

print(f"{a}x+{b}=0")
x= -b / a

print(f"x=-{b}/{a}")
print(f"El resultado de su ecuacion es {x}")

#Ejercicio 15

import math
forma=input("Desea sacar el area de un triangulo o un circulo? ingrese 't' para triangulo y 'c' para circulo: ").lower()

if(forma=="t"):
    base=int(input("ingrese la base del triangulo: "))
    altura=int(input("ingrese la altura del triangulo: "))
    area= (base*altura)/2
    print("El area del triangulo es: ", area)
elif(forma=="c"):
    radio=int(input("ingrese el radio del circulo: "))
    area=(math.pi*(radio**2))
    print("el area del circulo es: ", area)
else:
    print("error, el tipo de operacion ingresada no corresponde a lo pedido")



#Ejercicio 16
print("Con esta calculadora basica operaremos segun lo que ingreses")

num001=float(input("Ingrese un numero: "))
num002=float(input("Ingrese otro numero: "))

operacion=int(input("¿Que operacion desea realizar?: (1)Suma, (2)Multiplicacion, (3)Resta, (4)Division: "))

if operacion==1:
    suma=num001+num002
    print(f"El resultado de la suma es de {num001}+{num002}={suma}")
elif operacion==2:
    multi=num001*num002
    print(f"El resultado de la multiplicacion es de {num001}*{num002}={multi}")
elif operacion==3:
    resta=num001-num002
    print(f"El resultado de la resta es de {num001}-{num002}={resta}")
elif operacion==4:
    div=num001/num002
    print(f"El resultado de la division es de {num001}/{num002}={div}")
else:
    print("La operacion ingresada no cerresponde a ninguna operacion de las pedidas")

#Ejercicio 17

dia=input("ingrese un dia de la semana: ")
dia.lower
if (dia=="lunes"):
    print("inicio de semana")
elif (dia=="viernes"):
    print("ya casi es fin semana")
elif (dia=="sabado" or dia=="domingo"):
    print("fin de semana")
else:
    print("hoy es: ", dia)




#Ejercicio 18

sal_hora=float(input("Le pediremos por favor que ingrese su salario por hora: "))
mes_hora=float(input("Y sus horas trabajadas durante el mes: "))

hora_min=48

hora_extra=mes_hora-hora_min

print(f"Horas extras trabajadas: {hora_extra}")

sal_total=(hora_min*sal_hora)+(hora_extra*sal_hora*1.1)

print(f"Salario total: ${sal_total}")


#Ejercicio 19

cantidad_lapiz=int(input("Ingrese la cantidad de lapices a comprar: "))
costo_lapiz=60


if cantidad_lapiz>=1000:

    sin_descuento=costo_lapiz*cantidad_lapiz
    descuento=(sin_descuento*7)/100
    costo_total=sin_descuento-descuento
    print(f"El monto total a pagar es de: ${costo_total}")
else:
    sin_descuento=costo_lapiz*cantidad_lapiz
    print(f"El monto total a pagar es de: ${sin_descuento}")



#Ejercicio 20

print("Te pediremos que ingreses tus notas: ")

nota_1=int(input("Primer nota: "))
nota_2=int(input("Segunda nota: "))
nota_3=int(input("Tercer nota: "))
nota_4=int(input("Cuarta nota: "))
    
promedio=(nota_1+nota_2+nota_3+nota_4)/4

if promedio>=6:
    print(f"Aprobaste con: {promedio}")
else:
    print(F"Desaprobaste con: {promedio}")