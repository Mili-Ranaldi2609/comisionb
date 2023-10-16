"""Integrantes: Milagros Ranaldi, Julian Gonzalez, Pia Lavilla, Venus Galiana, Valentina Lara, Ornela Condori"""
#Ejercicio1

word_1=input("Ingrese una palabra, se le mostrara 10 veces: ")

for i in range(5):
    print(word_1) 

#Ejercicio 2 
birthday_year=int(input("Ingrese su edad: "))

for i in range(birthday_year+1):
    if i !=0 : 
        print(F"{i}") 

#Ejercicio 3

positive_num=int(input("Ingrese un numero entero positivo: "))
odd_numbers=0 
for i in range(positive_num+1):
    if i%2!=0:
        odd_numbers+=1
print(f"La cantidad de numeros impares es: {odd_numbers}")

#Ejercicio 4

number4=int(input("Ingrese un numero entero positivo: "))
i=1

for i in range(number4+1):
    print(number4-i,end=",")
print(" ")

#Ejercicio 5

investment=int(input("Ingrese cuanto desea invertir: "))
annual_interest=int(input("¿Cual es el interes anual?: "))
year=int(input("Ingrese cuantos años desea invertir: "))

for i in range(year):
    annual_earnings=(investment*annual_interest)/100
    investment=investment+annual_earnings
    print(f"En el año {i+1} el usuario gano un {annual_earnings}")

#Ejercicio 6

number6=int(input("Ingrese un numero para la altura de su triangulo: "))

for i in range(number6+1):
    print(" ")
    for j in range(i):
        print("*",end=" ")
print(" ")

#Ejercicio 7

for i in range(1,11):
    for j in range(1,11):
        print(f"{i}x{j}= {i*j}") 

#Ejercicio 8

n=int(input("Introduce la altura del triangulo (entero positivo): "))

for i in range (1,n+1,2):
    for j in range(i, 0 ,-2): 
        print(j, end=" ") 
    print(" ")  

#Ejercicio 9

password="contraseña"
password_2="u" 

while (password!=password_2):  
    password2= input("ingrese la contraseña: ").lower() 

#Ejercicio 10

while True:
    number10=int(input("Ingrese un numero positivo, para indicar si es o no es primo: "))
    if number10<0:
        break
    divider=0
    for i in range(number10):
        if number10%(i+1) == 0 : 
            divider += 1 
    if divider ==2:
        print("Es un número primo") 
    else: 
        print("No es primo") 

#Ejercicio 11

word=str(input("Ingrese una palabra: "))
word2=word[::-1]
print(f"La palabra invertida seria: {word2}")

#Ejercicio 12

phrase=str(input("Ingrese una frase: "))
letter=input("Ingrese la letra que quiere buscar: ")

count=phrase.count(letter)
print(f"La letra elegida se repite {count} de veces en la frase escrita")

#Ejercicio 13 

word_13=''

while word_13!='salir':
    word_13=str(input("Escriba algo, si quiere salir escriba 'salir'. ")).lower()
    echo=word_13
    print(f"Eco: {echo}")

#Ejercicio 14

number=int(input("Ingrese un numero: "))
number_2=int(input("Ingrese otro numero: "))
print(f"Vamos a ver si los numeros que se encuentran entre {number} y {number_2} son pares o impares: ")
for i in range(number,number_2+1):
    if i %2==0:
        print(f"Numero par: {i}")
    else:
        print(f"Numero impar: {i}")    

#Ejercicio 14

number14=int(input("Ingrese un numero: ")) 
number_2=int(input("Ingrese otro numero: ")) 

print(f"Vamos a ver si los numeros que se encuentran entre {number14} y {number_2} son pares o impares: ") 

for i in range(number14,number_2+1): 
    if i %2==0: 
        print(f"Numero par: {i}") 
    else: 
        print(f"Numero impar: {i}")     

#Ejercicio 15
while True:
    num = int(input("Escriba el numero del cual quiere conocer sus divisores: ")) 
    if num <= 0: 
        break      
    for i in range(num): 
        divider = 0       
        if num%(i+1) == 0: 
            divider +=1 
            print("los divisores de ",num, "son ", i+1 ) 

#Ejercicio 16

amount= int(input("indique cuantos numeros va ingresar: ")) 
negative=0

for i in range(amount): 
    num = int(input("ingrese el numero: ")) 
    if num<0:
        negative +=1 
print(f"se han introducido: {negative} numeros negativos")
##
#Ejercicio 17

phrase17=(input("ingrese una frase: ")).lower() 
vowel="aeiou"

for i in vowel:
    if i in phrase17:  
        print(i) 

#Ejercicio 18

before1 = 0
before2 = 1
sequence = "0 1 "
for i in range(9) :
    new = before1 + before2
    before1 = before2
    before2 = new
    num3 = str(new)
    sequence += num3
    sequence += " "
print(sequence)

#Ejercicio 19

objetive=int(input("Ingrese la cantidad de dinero que desea ahorrar: ")) 
save=0
while (save<=objetive):
    money=int(input("Cuanto vas a ingresar?")) 
    if (money>=0): 
        save+=money 
        print(save) 
    else: 
        print("no se pueden ingresar numeros negativos") 
print("Objetivo alcanzado")

#Ejercicio 20

addition=0
number20=1

while (number20!=0):
    number20=int(input("ingrese un numero distinto de 0: ")) 
    addition+=number20 
print(f"La sumatoria de los numeros ingresados es: {addition}")

#Ejercicio 21

number21=1
max=0

while (number21!=0):
    number21=int(input("ingrese un numero distirnto a 0: ")) 
    if(number>max): 
        max=number 
print(f"El numero mayor es: {max}")

#Ejercicio 22

number22=0
addition=0
addition_2=0

while (number22!=-1):

    number22=int(input("Ingrese un numero, para salir ingrese '-1': ")) 
    if (number>=0): 
        for n in str(number22): 
            n=int(n) 
            addition+=n 
        print(addition) 
    else: 
        print("el numero ingresado debe ser positivo") 
    if (number22 % 2==0): 
        addition_2+=1 
print(f"La cantidad de numeros pares son: {addition_2}")

#Ejercicio 23



#Ejercicio 24

print("Ingreese los montos, para calcular el total de su compra")
total_amount = 0
while True:
    amount = float(input("Ingrese el monto(Ingrese un valor negativo para salir): "))

    if amount < 0:
        print("Monto inválido. Por favor, ingrese un nuevo monto.")
        continue
    
    total_amount += amount
    if total_amount > 1000:
        total_amount *= 0.9
    if amount == 0:
        break
print("El total a pagar es: $" + str(total_amount))

#Ejercicio 25

number25 = int(input("Ingrese un número entero positivo: "))
factorial = 1
if number25 < 0:
    print("El número ingresado debe ser positivo.")
elif number25 == 0:
    print("El factorial de 0 es 1.")
else:
    for i in range(1, number25 + 1):
        factorial *= i
    
    print("El factorial de", number25, "es", factorial)