from obFunc import*
# Ejemplo de Bubble sort
array = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(array)
print("Array ordenado:")
for i in range(len(array)):
    print(array[i])

#Ejemplo de Selection sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

"""principal"""
listS = [9, 5, 2, 7, 1]
selection_sort(listS)
print(listS)

#Ejemplo de Insert sort
def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

"""principal"""
list = [9, 5, 2, 7, 1]
insert_sort(list)
print(list)

#Ejemplo de Merge sort
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

"""principal"""
listM = [9, 5, 2, 7, 1]
merge_sort(listM)
print(listM)

