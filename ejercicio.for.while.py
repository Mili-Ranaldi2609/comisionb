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
digito_p=0
digito_imp=0
while int(num>0 and num!=0):
    
    num=int(input("Ingrese un numero: "))
    if int(num%2==0):
        digito_p=1+digito_p
    elif int(num%2!=0):
        digito_imp=1+digito_imp
        

print(f"digito pares: {digito_p}") 
print(f"Digito impares:{digito_imp}")