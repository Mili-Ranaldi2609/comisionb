import random

#Ejercicio 1
print("Ejercicio 1 (guardaremos los numeros en una lista)")
numbers1 = []

while True:
    num = int(input("Ingrese un número (ingrese 0 para finalizar): "))
    if num== 0:
        break
    numbers1.append(num)

print("Lista de números ingresados:", numbers1)

#Ejercicio 2
print("Ejercicio 2 (eliminando ocurrencia del numero)")
# Solicitar al usuario que ingrese un número
number2 = int(input("Ingrese un número: "))
print("Se verificara si el numero esta en la lista del punto anterior")

if number2 in numbers1:
    # Eliminar la primera ocurrencia del número en la lista
    numbers1.remove(number2)
    print("El número ha sido eliminado de la lista.")
else:
    print("No es posible eliminar el número, no se encuentra en la lista.")

#Ejercicio 3
print("Ejercicio 3 (sumando los numeros de la lista)")
add_list = [5, 6, 45, 69, 12, 26]
print("Lista a sumar")
print(add_list)
add_result = 0
for element in add_list:
    add_result += element
print(f"La sumatoria es: {add_result}")

#Ejercicio 4
print("Ejercicio 4 (iterando la lista)")
number7 = int(input("Ingrese un número: "))
original_list = [1, 5, 10, 15, 20]
print("Lista original")
print(original_list)
new_list = [element for element in original_list if element < number7]
print("Nueva lista")
for element in new_list:
    print(element)

#Ejercicio 5
print("Ejercicio 5 (tuplas elementos )")
original_list5 = [5, 16, 2, 5, 57, 5, 2]

# Creamos un diccionario para contar la frecuencia de cada número
frequency = {}
for number in original_list5:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

# Convertimos el diccionario en una lista de tuplas
new_list5 = list(frequency.items())
print(new_list5)

#Ejercicio 6

primary_names = []
secondary_names = []

print("Ingresar los nombres de los alumnos de nivel primario (ingresar x para finalizar):")
while True:
    name = input("Nombre: ")
    if name == 'x':
        break
    primary_names.append(name)


print("Ingresar los nombres de los alumnos de nivel secundario (ingresar 'x' para finalizar):")
while True:
    name = input("Nombre: ")
    if name == 'x':
        break
    secondary_names.append(name)
#a)
unique_primary_names= list(set(primary_names))
unique_secondary_names = list(set(secondary_names))
print("Nombres de nivel primario:")
for name in unique_primary_names:
    print(name)

print("Nombres de nivel secundario:")
for name in unique_secondary_names:
    print(name)

#b)
repeated_names = set(unique_primary_names).intersection(unique_secondary_names)
if repeated_names:
    print("Nombres que se repiten entre nivel primario y secundario:", repeated_names)
else:
    print("No hay nombres que se repitan entre nivel primario y secundario.")

#c)
no_repeated_primary = set(unique_primary_names).difference(unique_secondary_names)
if no_repeated_primary:
    print("Nombres de nivel primario que no se repiten en nivel secundario:", no_repeated_primary)
else:
    print("Todos los nombres de nivel primario se repiten en nivel secundario.")

#Ejercicio 7
print("Ejercicio 7 (50 strings)")
#diccionario para contar las ocurrencias
repetition={}
#string ya procesados
saved=0


while saved<50:
    entrance=input("ingrese un string(o presione enter para terminar): ")
    if not entrance:
        break


    saved+=1
    for character in entrance:
        if character in repetition:
            repetition[character]+=1
        else:
            repetition[character]=1


for character, quantity in repetition.items():
    print(f"'{character}':{quantity}")



#Ejercicio 8
rows= 10
columns = 10
#Crea 10 columnas por cada una de las 10 filas de la lista
goals = [[0 for j in range(columns)] for i in range(rows)]

#Declara la cantidad de goles por partido
for r in range(rows):
    for c in range(columns):
        if r == c :
            goals[r][c] = 0
        else:
            goals[r][c] = random. randint(0, 6)

#Imprime la matriz
print("La tabla de goles: ")
for row in goals:
    print(row)

for r in range(rows):
    goals_scored = 0
    goals_allowed = 0
    win = 0
    lose= 0
    tie = 0
    print(f"-----Equipo {(r+1)}-----")
    for c in range(columns):
        #Sumar los goles anotados
        goals_scored += goals[r][c]
        #Suma de goles recibidos
        goals_allowed += goals[c][r]
        #Compara con la posicion contraria en la matriz
        if goals[r][c]> goals[c][r]:
            win += 1
        elif goals[r][c]==goals[c][r]:
            tie += 1
        else:
            lose +=1
    print(f"La cantidad de victorias es {win}")
    print(f"La cantidad de derrotas es {lose}")
    print(f"La cantidad de empates es {tie}")
    print(f"Goles hechos {goals_scored}\nGoles recibidos {goals_allowed}")


#Ejercicio 9
print("!Jugaremos al METATEST¡")
# Crear una matriz para el tablero
board= []
rows = 4
columns = 4

# Crear una lista con las imágenes posibles
images = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# Inicializar el tablero con cartas boca abajo
for i in range(rows):
    row = []
    for j in range(columns):
        row.append('*')
    board.append(row)

# Asignar aleatoriamente las parejas de cartas iguales
couples= images * 2
random.shuffle(couples)

# Función para mostrar el tablero actualizado
def show_board():
    for row in board:
        print(' '.join(row))

# Función para voltear una carta en el tablero
def flip_card(row, column):
    board[row][column] = couples[(row * columns + column) // 2]

# Inicializar el seguimiento de las parejas encontradas
found_couples = 0


# Juego principal
while found_couples< len(images):
    show_board()
    
    # Solicitar al jugador las coordenadas de la primera carta a voltear
    while True:
        row_flip = int(input("Ingrese la fila de la primera carta a voltear (0-3): "))
        column_flip = int(input("Ingrese la columna de la primera carta a voltear (0-3): "))
        if 0 <= row_flip < rows and 0 <= column_flip< columns:
            break
        else:
            print("Coordenadas fuera de los límites. Inténtalo de nuevo.")
    
    # Voltear la primera carta seleccionada por el jugador
    flip_card(row_flip, column_flip)
    show_board()

# Solicitar al jugador las coordenadas de la segunda carta a voltear
    while True:
        row_flip2 = int(input("Ingrese la fila de la segunda carta a voltear (0-3): "))
        column_flip2 = int(input("Ingrese la columna de la segunda carta a voltear (0-3): "))
        if 0 <= row_flip2 < rows and 0 <= column_flip2 < columns:
            break
        else:
            print("Coordenadas fuera de los límites. Inténtalo de nuevo.")
    
    # Voltear la segunda carta seleccionada por el jugador
    flip_card(row_flip2, column_flip2)
    show_board()
# Verificar si las cartas son iguales
    if board[row_flip][column_flip] == board[row_flip2][column_flip2]:
        print("¡Encontraste una pareja!")
        found_couples += 1
    else:
        print("No es una pareja. Inténtalo de nuevo.")

print("¡Felicidades, encontraste todas las parejas!")

#Ejercicio 10
print("Ejercicio 10 (Veremos la diagonal inversa y principal de la matriz) ")
matrix_dimension=int(input("Ingrese el tamaño de la matriz (solo un numero): "))
#a
matrix=[]
i=0
j=0
while i<matrix_dimension:
    matrix.append([])
    while j<matrix_dimension:
        if i==j:
            matrix[i].append(0)
        else:
            matrix[i].append(1)
        j+=1
    j=0
    i+=1
for i in matrix:
    print(i)
#b
matrix_b=[]
print("matriz con diagonal inversa: ")
for n in range(matrix_dimension):
    matrix_b.append([])
    for f in range(matrix_dimension):
        if n+f==matrix_dimension-1:
            matrix_b[n].append(0)
        else:
            matrix_b[n].append(1)
for i in matrix_b:
    print(i)

#Ejercicio 11
print("Ejercicio 11 (divisas)")

currency_dictionary = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}
badge = input("Ingrese una divisa (ejemplo: Dollar) ").capitalize()


# Obtener el símbolo de la divisa o mostrar un mensaje de aviso
if badge in currency_dictionary:
    symbol = currency_dictionary[badge]
    print(f"El símbolo de {badge} es {symbol}")
else:
    print("Divisa no encontrada en el diccionario")

#Ejercicio 12
print("Ejercicio 12 (datos personales)")
name = input("Ingrese su nombre: ").capitalize()
age = input("Ingrese su edad: ")
address = input("Ingrese su dirección: ").capitalize()
phone = input("Ingrese su número de teléfono: ")

user_data = {
    "nombre": name,
    "edad": age,
    "dirección": address,
    "teléfono": phone
}

message = f"{user_data['nombre']} tiene {user_data['edad']} años, vive en {user_data['dirección']} y su número de teléfono es {user_data['teléfono']}."
print(message)

#Ejercicio 13
print("Ejercicio 13 (diccionario de frutas)")
fruit_prices = {
    'manzana': 1.5,
    'banana': 0.5,
    'naranja': 0.75,
    'pera': 1.0,
    'uva': 2.0
}

# Preguntar al usuario por una fruta y el número de kilos
fruit = input("Ingrese el nombre de una fruta: ").lower()
kilos = float(input("Ingrese el número de kilos: "))

# Calcular el precio de la fruta ingresada por el usuario
if fruit in fruit_prices:
    total_price = fruit_prices[fruit] * kilos
    print(f"El precio de {kilos} kilos de {fruit} es: {total_price}")
else:
    print("La fruta ingresada no está en el diccionario de precios.")

