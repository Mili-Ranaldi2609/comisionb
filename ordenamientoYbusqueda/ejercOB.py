from obFunc import *

# Ejemplo de Bubble sort
print("Ordenamiento bubble sort")
array = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(array)
print("Array ordenado:")
for i in range(len(array)):
    print(array[i])

#Ejemplo de Selection sort
print("Ordenamiento selection sort")
listS = [9, 5, 2, 7, 1]
selection_sort(listS)
print(listS)

#Ejemplo de Insert sort
print("Ordenamiento insert sort")
list = [9, 5, 2, 7, 1]
insert_sort(list)
print(list)

#Ejemplo de Merge sort
print("Ordenamiento merge sort")
listM = [9, 5, 2, 7, 1]
merge_sort(listM)
print(listM)

#Ejemplo busqueda lineal
print("Busqueda lineal")
my_list = [1, 3, 5, 7, 9, 11, 13]
element_search = 7
r = linear_search(my_list, element_search)

if r != -1:
    print(f"Elemento {element_search} encontrado en el índice {r}")
else:
    print(f"Elemento {element_search} no encontrado en la lista")

#Ejemplo de busqueda binaria
print("Busqueda binaria")
listB = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
element_s = 11
res = binary_search(listB, element_s)

if res != -1:
    print(f"El elemento {element_s} se encuentra en la posición {res}.")
else:
    print(f"El elemento {element_s} no se encuentra en la lista.")
