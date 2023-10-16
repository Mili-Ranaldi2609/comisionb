#Ejercicio 1

corrimiento=int(input("Ingrese la cantidad de espacios que se correran las letras: "))
alfabeto="abcdefghijklmnñopqrstuvwxyz"

for i  in range(5):
    mensaje=input("Mensaje a encriptar: ").lower()
    mensaje_encriptado=''
    for letra in mensaje:
        if letra in alfabeto:
            indice=alfabeto.find(letra)
            indice=(indice+corrimiento)%27
            mensaje_encriptado+=alfabeto[indice]
        else: 
            mensaje_encriptado+=letra 
    print(f'El mensaje encriptado es: {mensaje_encriptado}')

#Ejercicio 2

num=1
i=1
while (num>0 and num!=0):
    par=0
    impar=0
    var=0
    num=input("Ingrese un numero, si es menor a 1 el programa se da por finalizado: ")
    while var<len(num):#condicion de salida
        i=int(num[var])
        if(i%2==0):
            par+=1
        else:
            impar+=1
        var+=1
    print("la cantidad de digitos pares son: ",par, "y la cantidad de digitos impares son: ", impar)

