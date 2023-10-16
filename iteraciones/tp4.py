#Ejercicio 1 ingles
X=int(0)

print("Resultado:")
while X<30:
    X+=1
    if X==15:
        print(f"Se rompio la ejecucio del bucle cuando x valia: {X}")
        break
    elif (X==4) or (X==6) or (X==10):
        print(f"Se salto el valor: {X} ")
        continue
    print(f'El valor del bucle es: {X} ')

print(f"La ejecución del bucle se interrumpió cuando x era {X}" )

#Ejercicio 1
"""append(se utiliza para agregar un elemento a una lista existente)"""
"""upper=convierte a mayusculas"""
lines=[]
while True:
    line=input("Ingrese una linea de texto: ")
    if line:
        lines.append(line.upper())
    else:
        break
print(f"Las lineas convertidas a mayusculas son: {lines}")

#Ejercicio 2

total = 0

while True:
    action = input("Ingrese 'd' para depositar o 'r' para retirar seguido de la cantidad (ejemplo: d 100): ")
    if not action:
        break
    parts = action.split()
    if len(parts) != 2:
        print("Formato incorrecto. Intente de nuevo.")
        continue
    operation, amount_str = parts
    amount = int(amount_str)
    if operation == 'd':
        total += amount
    elif operation == 'r':
        total -= amount
    else:
        print("Operación no válida. Intente de nuevo.")
        continue

print("El total en su cuenta es de:", total)

#Ejercicio 3

number3=1
primeQuantity=0
while number3>0:
    number3 = int(input("Ingresa un número mayor que 1 (ingresa 0 para finalizar): "))
    for i in range(2, number3):
        if number3 % i == 0:
            primeQuantity += 1
        if number3 < 2:
            break

print("La cantidad total de números primos ingresados es:", primeQuantity)

#Ejercicio 4

currentYear=int(input("Ingrese su año actual: "))
lastYear=int(input("Ingrese un año pasado: "))


for i in range(lastYear,currentYear,1):
    if (i%4==0 and i%100!=0) or i%400==0 :
        
        print(F"El año: {i} es bisiesto.")
    else:
        continue

#Ejercicio 5
number5=20
number5_2=1
for i in range(number5_2,number5,1):
    if i%2==0:
        print(f"{i} es par")
    else:
        continue

#Ejercicio 6

numbers6=[10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
number=0
choose=int(input("Ingrese un numero del 10 al 25: "))

for i in numbers6:
    
    if choose==20:
        number=numbers6.index(choose)
        print("Encontraste el numero! ")
        break
    else:
        print("No es el numero que se esta buscando")
        choose=int(input("Ingrese otro numero: "))

#Ejercicio 7

option=1

while option:
    option=int(input("Ingrese una opcion: (1), (2), (3): "))
    if option==1:
        print("Usted ha elegido la opcion 1 ºuº")
    elif option==2:
        print("Usted ha elegido la opcion 2 +-+")
    elif option==3:
        print("Usted ha elegido la opcion 3 O.O")
    elif option==0:
        print("Usted marco 0 el programa se termina")
    else:
        print("Ha ingresado una opcion equivocada")
