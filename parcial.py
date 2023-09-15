#Se pide al usuario su nombre y se asigna a una vaiable
name_u=input("Ingrese su nombre por favor: ").upper()
#listas de los numeros
numbers_p=[]
numbers_i=[]
#variable donde se gaurdara el valor del numero max de los pares
number_max=0
#variables para calcular el promedio de numeros impares
s=0
q=0
#lista donde se almacenan las vocales
vowels=[0,0,0,0,0]

#posicion for de las vocales
p=0
#
number1=1
#menu de opciones:
option=1
while option!=0:
    option=int(input(F"{name_u}. Elija una opcion: (0)Salir---(1)Juego de numeros---(2)Juego de palabras-: "))
    if option==0:
        print(f"{name_u}. Ha salido del menu de opciones.")
        break
    elif option==1:
        while number1!=0:
            number1=int(input(f"{name_u}; ingrese numeros enteros,; ingrese 0 para terminar: "))
            if number1%2==0:
                #se agrega el numero par a la lista ya creada
                numbers_p.append(number1)
                #se va iterando y calculando con esta funcion cual numero es el maximo 
                number_max=max(numbers_p)
            elif number1%2!=0:
                numbers_i.append(number1)
                #se suman los numeros de la lista
                s=sum(numbers_i)
                #se cuentan cuantos numeros hay en la lista
                q=len(numbers_i)
                #se saca el promedio
                average=s/q
            elif number1==0:
                print(f"{name_u}; Ha finalizado el juego. Reinicie para volver a jugar")
                break
            else:
                print("---numero invalido---reinicie el programa---")
        print(f"El mayor numero par que ingreso es: {number_max}")
        print(f"El promedio de los numeros pares es: {average}")            
    elif option==2:
        phrase=input(f"{name_u}, ingrese una frase: ").lower()
        for letter in phrase:
            #se va recorriendo la frase y se van guardando la cantidad de cada vocal en un indice diferente de la lista.
            if letter=='a':
                vowels[0]+=1
            elif letter=='e':
                vowels[1]+=1
            elif letter=='i':
                vowels[2]+=1
            elif letter=='o':
                vowels[3]+=1
            elif letter=='u':
                vowels[4]+=1
        print(f"La cantidad de 'a' en la frase es: {vowels[0]}")
        print(f"La cantidad de 'e' en la frase es: {vowels[1]}")
        print(f"La cantidad de 'i' en la frase es: {vowels[2]}")
        print(f"La cantidad de 'o' en la frase es: {vowels[3]}")
        print(f"La cantidad de 'u' en la frase es: {vowels[4]}")
    else:
        print(f"{name_u}, Ha ingresado una opcion incorrecta pruebe nuevamente")