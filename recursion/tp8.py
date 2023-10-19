from funcionesTP8 import *
#EJERCICIO 1
print("(1)Contar cantidad de digitos de un numero")
result=number_positiv(12345)
print(f"el numero tiene {result} digitos.")
#EJERCICIO 2
print("(2)Potencias")
if power(2,4):
    print(f"{2} es una potencia de {4}.")
else:
    print(f"{2} no es una potencia de {4}.")
#EJERCICIO 3
print("(3)Cuantas veces se encuentra 'b' dentro de 'a'.")
a = "Me siento cansado y tu como te sientes"
b = "c"
positions = find_positions_recursive(a, b)
print("Posiciones en donde se encuntra b ")
print(positions)
#EJERCICIO 4
print("(4)Ver si un numero entero es par o no")
#n=10
n=3
if par(n):
    print(f"{n} es un número par.")
else:
    print(f"{n} es un número impar.")


#EJERCICIO 5
print("(5)Calcular el elemento max de la lista")
numbers5 = [3, 7, 1, 9, 4, 2, 6, 8]
r =find_maximum(numbers5)
print("El elemento máximo de la lista es:", r)
#EJERCICIO 6
print("(6)Replicar lista")
numbers6 = [1, 3, 7, 4, 9]
n = 2
res= replicate(numbers6, n)
print("Lista replicada:", res)
#EJERCICIO 7
print("(7)Sumatoria recursiva")
n = int(input("Ingrese el valor de n: "))
p = int(input("Ingrese el valor de p: "))

# Calcular la sumatoria K(n, p) usando la función recursiva.
res = calculate_sum(n, p)

# Imprimir el resultado.
print(f"El resultado de K({n}, {p}) es: {res}")
#EJERCICIO 8
print("(8)Triangulo pascal")
n = int(input("Ingrese el valor de n: "))
k = int(input("Ingrese el valor de k: "))

# Calcular el valor en el triángulo de Pascal usando la función recursiva.
result8 = pascal(n,k)
# Imprimir el resultado.
print(F"El valor en la fila {n} y la columna {k} del triángulo de Pascal es: {result8}")
#EJERCICIO  9
print("(9)Combinaciones")
list9 = ['a', 'b', 'c']
k = 2
r = combinations(list9, k)

print(f"Todas las combinaciones de longitud {k} son:")
for combo in r:
    print(combo)
#EJERCICIO 10
n10= 1
broad, long=measurements_sheet_A(n10)
print(f"Las medidas de A{n10} son: {broad} mm x {long} mm")
