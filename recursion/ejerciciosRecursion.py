import random
#EJERCICIO 1
print("¿Cuanto tiempo le llevara salir a la rata del laberinto?")
def simulate_experiment(time_elapsed=0):
    decision = random.choice([1, 2, 3])  # Elegir uno de los 3 caminos al azar
    time_elapsed += decision  
    time_elapsed+= decision 
# Sumar el tiempo de la decisión

    if decision == 3:  # Si la rata eligió el camino 3, salió de la jaula
        return time_elapsed

    # Llamada recursiva para continuar el experimento
    return simulate_experiment(time_elapsed)

# Llamamos a la función para simular el experimento
departure_time = simulate_experiment()

print(f"La rata salió de la jaula en {departure_time} minutos.")

# EJERCICIO 2
print("Crea una funcion recursiva que reciba un numero entero y lo devuelva de manera invertida")
def f(n):
    s=str(n)
    if len(s)<=1:
        return s
    return s[-1]+ f(int(s[:-1]))

while True:
    num=int(input("Ingrese un numero: "))
    if num<10 and num>-10:
        print("Debe ingresar un numero de mas de un caracter")
    else:
        reverse=f(num)
        break
print("El numero invertido es: ", reverse)