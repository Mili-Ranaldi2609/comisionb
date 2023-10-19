#----1----#
def number_positiv(number):
    number_str=str(number) #convertir el numero en cadena
    return len(number_str) #nos dice cuantos numeros tiene
#----2----#
import math
def power(n,b):
    if b <= 1 or n<=0:
        return False
    log_n_b = math.log(n, b) # nas dara un numero que representa el exponente al q se elevaria b para obtener n
    return log_n_b.is_integer() # verifica si el resultado es un numero entero si es asi la funcion devuelve true
#----3----#
def find_positions_recursive(a, b, start=0, positions=None):
    if positions is None:
        positions = []
    
    # Buscar la próxima ocurrencia de b en a a partir de la posición actual
    index = a.find(b, start)
    if index == -1:
        return positions  # No se encontró más ocurrencias de b en a
    
    positions.append(index) 
# Llamada recursiva para buscar más ocurrencias de b en a
    return find_positions_recursive(a, b, index + 1, positions)
#----4----#
def par(n):
    if n == 0:
        return True  # El 0 se considera par
    else:
        return impar(n - 1)

def impar(n):
    if n == 0:
        return False  # El 1 se considera impar
    else:
        return par(n - 1)
#----5----#
def find_maximum(list):
    # Caso base: Si la lista está vacía, no hay un elemento máximo.
    if len(list) == 0:
        return None

    # Caso base: Si la lista tiene un solo elemento, ese es el máximo.
    if len(list) == 1:
        return list[0]

    # Dividir la lista en dos mitades.
    half = len(list) // 2
    left_half = list[:half]
    right_half = list[half:]

    # Llamada recursiva para encontrar el máximo en ambas mitades.
    max_left = find_maximum(left_half)
    max_right= find_maximum(right_half)

    # Comparar y devolver el máximo de ambas mitades.
    return max(max_left, max_right)
#----6----#
def replicate(list, n):
    # Caso base: Si la lista está vacía o n es igual a 1, no se replican elementos.
    if len(list) == 0 or n == 1:
        return list

    # Caso recursivo: Replicar el primer elemento n veces y luego replicar el resto de la lista.
    element = list[0]
    replicated_list = [element] * n
    return replicated_list + replicate(list[1:], n)
#----7----#
def calculate_sum(n, p):
    # Caso base: Si n es 1, el resultado es simplemente p.
    if n == 1:
        return p
    else:
        # Llamada recursiva para calcular la sumatoria.
        return n * p + calculate_sum(n - 1, p)
#----8----#
def pascal(n, k):
    # Caso base: Los valores en los bordes son siempre 1.
    if k == 0 or k == n:
        return 1
    else:
        # Llamada recursiva para calcular el valor en el triángulo de Pascal.
        return pascal(n - 1, k - 1) + pascal(n - 1, k)
#----9----#
def combinations(list, k, current_string='', res=[]):
    if k == 0:
        # Si hemos formado una cadena de longitud k, la agregamos al resultado.
        res.append(current_string)
    else:
        for char in list:
            # Llamada recursiva para agregar cada carácter posible a la cadena actual.
            combinations(list, k - 1, current_string + char, res)

    return res
#----10----#
def measurements_sheet_A(N):
    if N == 0:
        return (841, 1189)  # Caso base: A0
    # Llama recursivamente a la función para obtener las medidas de A(N-1)
    broad, long = measurements_sheet_A(N - 1)
    # Calcula las nuevas medidas doblando la hoja A(N-1) por la mitad
    new_width = long /2
    new_long= broad
    return (int(new_width), int(new_long))