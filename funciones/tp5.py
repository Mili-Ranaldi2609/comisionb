from funcionestp5 import *
#Ejercicio1 
print("Veremos si el dni que ingrese es valido.")
dni=input("Ingrese el numero de dni ")
valid_dni(dni)

#Ejercicio2
print("Calcularemos la longitud del ultimo caracter que ingrese.")
string=str(input("Ingrese la frase: "))
print(f"La longitud de la ultima palabra es: {lengths_of_last_word(string)}")

#Ejercicio3
print("Crearemos un ID para cada socio que ingrese del club.")
while True:
    full_name = input("Ingrese el nombre completo del socio (o dejar vacío para finalizar): ")
    
    if full_name== "":
        break
    
    dni = input("Ingrese el número de DNI del socio: ")
    dni = valid_dni3(dni)
    
    identifier = partner_identifier(full_name, dni)
    
    print("ID ->", identifier)

#Ejercicio4
print("Veremos si los numeros que ingreses son multiplos")
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
if num2==0:
    print("No es posible dividir por 0 (Reinicie el programa)")
elif num1==num2:
    print("Los numeros ingresados son iguales")
elif(is_multiple(num1, num2)):
    print("¡Uno de los números es múltiplo del otro!")
else:
    print("Ninguno de los números es múltiplo del otro.")

#Ejercicio5
print("Calcularemos la temperatura media de cada dia que ingreses.")
num_days = int(input("Ingrese el número de días: "))

for i in range(num_days):
    temp_max = float(input(f"Ingrese la temperatura máxima del día {(i+1)}: "))
    temp_min = float(input(f"Ingrese la temperatura mínima del día {(i+1)}: "))
    temperature = medium_temperature(temp_max, temp_min)
    print(f"La temperatura media del dia {(i+1)} es: {temperature}")

#Ejercicio6
print("Le agregaremos espacios a tu texto.")
text= input("Ingresa un texto: ")
result = add_spaces(text)
print(result)

#Ejercicio7
numbers7 = []
print("Calcularemos el maximo y el minimo de una lista de nuneros.")
while True:
    num=input("Ingresa un numero: ")
    numbers7.append(float(num))
    option = input("Ingresa enter para salir///Ingresa cualquier caracter para seguir ")
    if option == "":
        break
maximum, minimum = maximum_and_minimum(numbers7)
print("El máximo es:", maximum)
print("El mínimo es:", minimum)

#Ejercicio8
print("Calcularemos el area y el perimetro de una circunferencia.")
radio8 = float(input("Ingresa el radio de la circunferencia: "))
area, perimeter= area_and_perimeter(radio8)
print("El área de la circunferencia es:", area)
print("El perímetro de la circunferencia es:", perimeter)

#Ejercicio9
print("Logueo:")
attemps = 0
while attemps < 3:
    username = input("Nombre de usuario: ")
    password = input("Contraseña: ")
    res, attemps= login(username, password, attemps)
    
    if res:
        print("¡Inicio de sesión exitoso!")
        break
    else:
        print("Nombre de usuario o contraseña incorrectos. Intenta de nuevo.")
if attemps == 3:
    print("Has excedido el número máximo de intentos.")

#Ejercicio10
print("Calcularemos los descuento a aplicar al carrito de compras")
shopping_cart={
    "lechuga": 123,
    "tomate": 212,
    "papa": 350,
    "zanahoria":220
}
shopping_cart2={
    "gomitas": 123,
    "caramelos":212,
    "chocolate": 150
}
shopping_cart3={
    "leche": 1200,
    "queso":660,
    "yogurt": 321
}

#final_price= apply_discount(shopping_cart)
#final_price= apply_discount(shopping_cart2)
final_price= apply_discount(shopping_cart3)
print(f"El precio final de la compra es: {final_price}$" )

#Ejercicio11
print("Aplicaremos funciones sobre una lista")
numbers11=[12,23,1,4,100,50,31]
print("La lista es:")
print("[",end="")
for i in numbers11:
    print(f"{i},", end=" ")
print("]")

result=apply_funcion(multiply_by_two,numbers11)
print("El resultado de multiplicar los numeros de la lista 'x2' es: ",result)

#Ejercicio 12
#phrase = "Mucho gusto un placer en conocerte"
#phrase2="Mi comida favorita son las papas fritas"
phrase3="No me gusta la comida picante"
print("Contaremos la cantidad de letras que tiene cada palabra de la frase: '",phrase3,"'")
result12 = count_lenght_words(phrase3)
print("La frase dividida por  palabra es: ")
print(result12)