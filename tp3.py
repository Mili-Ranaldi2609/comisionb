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