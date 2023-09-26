#Funciones
def add_digits(number):
    add=0
    
    while number!=0:
        digit=number%10
        add+=digit
        number//=10
        
    return add
def sum_digits(num):
    sumD=0
    sumD+=add_digits(num)
    return sumD
#Programa principal
number1=1

while number1!=0:
    number1=int(input("Ingrese el numero a procesar: "))
    print(f"Suma: {add_digits(number1)}")

