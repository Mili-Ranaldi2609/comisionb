#Funcion bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
#Funcion selection sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
#Funcion insert sort
def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
#Funcion merge sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
#Funcion busqueda lineal
def linear_search(list, element):
    for i in range(len(list)):
        if list[i] == element:
            return i  # Devuelve el índice del elemento encontrado
    return -1  # Devuelve -1 si el elemento no se encuentra en la lista
#Funcion busqueda binaria
def binary_search(list, element):
    left, right = 0, len(list) - 1
    
    while left  <= right:
        half= (left + right) // 2
        middle_v = list[half]
        
        if middle_v== element:
            return half
        elif middle_v < element:
            left= half + 1
        else:
            right = half- 1
    
    return -1  # Elemento no encontrado
#Funciones tp7
def get_author(book):
    return book["author"]
#Ordenamiento inserccion por longitud
def insertion_sort_by_length(strings):
    for i in range(1, len(strings)):
        current_string = strings[i]
        j = i - 1
        while j >= 0 and len(current_string) < len(strings[j]):
            strings[j + 1] = strings[j]
            j -= 1
        strings[j + 1] = current_string
#Ordenamiento por burbuja de manera descendente
def bubble_sort_descending(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
#Ordenamiento por conteo
def counting_sort(arr):
    if not arr:
        return arr
    # Encontrar el valor máximo en la lista
    max_val = max(arr)
    
    # Crear una lista de conteo para contar la frecuencia de cada número
    count = [0] * (max_val + 1)
    
    # Contar la frecuencia de cada número en la lista original
    for num in arr:
        count[num] += 1
    
    # Construir la lista ordenada a partir de la lista de conteo
    sorted_arr = []
    for i in range(max_val + 1):
        sorted_arr.extend([i] * count[i])
    return sorted_arr
#Ordenar lista mixta
def sort_numbers_strings_mix(input_list):
    # Separar números y cadenas
    numbers = [x for x in input_list if isinstance(x, (int, float))]
    strings = [x for x in input_list if isinstance(x, str)]
# Ordenar números de menor a mayor
    numbers.sort()
# Ordenar cadenas alfabéticamente
    strings.sort()
# Combinar las listas ordenadas
    sorted_list = numbers + strings

    return sorted_list



