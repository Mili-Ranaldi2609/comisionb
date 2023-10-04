#Funcion ejercicio 1
def valid_dni(number_dni):
    #Se verifica el rango del dni 
    if len(str(number_dni))==7 or len(str(number_dni))==8:
        print("True")
        return True
    
    else:
        print("False")
        return False
#Funcion ejercicio 2

def lengths_of_last_word(str):
    #Se divide la frase y se elminan los espacios:
    words=str.strip().split()
    if words:
        #Se retorna la longitud de la ultima palabra
        return len(words[-1])
    else:
        return 0
#Funcion ejercicio 3
#Se toma como dato el valor del dni, y el nombre completo ingresado por el usuario
#De ahi se genera el identificador unico
def partner_identifier(name, dni3):
    #Se divide el nombre en listas:
    name_lasName= name.split()
    name1 = name_lasName[0]
    lastName = name_lasName[-1]
    dni_tres_digitos = dni3[:3]
    
    identificador = f"{name1}{len(lastName)}{dni_tres_digitos}"
    
    return identificador
#Se verifica que el rango del dni sea correcto
def valid_dni3(dni3):
    while len(dni3) not in [7, 8]:
        dni3 = input("Número de DNI inválido. Ingrese nuevamente: ")
    
    return dni3
#Funcion ejercicio 4
def is_multiple(number1, number2):
    if number1 % number2 == 0 or number2 % number1 == 0:
        return True
    else:
        return False
#Funcion ejercicio 5
def medium_temperature(temp_max, temp_min):
    return (temp_max + temp_min) / 2
#Funcion ejercicio 6
def add_spaces(text):
    result = ''
    for letter in text:
        result += letter + ' '
    return result
#Funcion ejercicio 7
def maximum_and_minimum(list):
    maximum = max(list)
    minimum = min(list)
    return maximum, minimum
#Funcion ejercicio 8
import math
def area_and_perimeter(radio):
    area = math.pi * radio**2
    area2=round(area,2)
    perimeter = 2 * math.pi * radio
    perimeter2=round(perimeter,2)
    return area2, perimeter2
#Funcion ejercicio 9
def login(username9, password9,attemps9):
    if username9 == "usuario1" and password9 == "asdasd":
        return True
    else:
        attemps9+=1
        return False, attemps9
#Funcion ejercicio 10
def apply_discount(cart):
    total = 0
    for product, price in cart.items():
        discount = price * 0.10 # Multiplica por 0.01 para obtener el porcentaje en decimal
        final_price = price - discount
        total += final_price
    return abs(total)
#Funcion ejercicio 11
def apply_funcion(funcion, list11):
    return [funcion(element) for element in list11]

def multiply_by_two(num):
    return num*2
#Funcion ejercicio 12
def count_lenght_words(phrase):
    # Dividir la frase en palabras utilizando split()
    words = phrase.split()
    dictionary = {}
    for i in words:
        dictionary[i] = len(i)

    return dictionary

