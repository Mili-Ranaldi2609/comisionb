from obFunc import *
#Ejercicio 1
print("(1)Ordenando lista por metodo de burbuja")
list1=[34,21,0,9,8,100]
bubble_sort(list1)
print("Lista ordenada:")
print(list1)
#Ejercicio 2
print("(2)Ordenando lista por metodo de seleccion")
arr = ["perro", "tarea", "programacion","gato"]
selection_sort(arr)
print("Lista ordenada:")
print(arr)
#Ejercicio 3
print("(3)Ordenando lista de libros por autor")
books=[
    {"title":'Sigue mi voz',"author":'Ariana Godoy',"gender":'Ficcion',"year":'21/07/2022'},
    {"title":'Boulevar',"author":'Flor Salvador',"gender":'Ficcion',"year":'17/05/2020'},
    {"title":'Fleur',"author":'Ariana Godoy',"gender":'Ficcion',"year":'08/03/2022'},
    {"title":'Antes de diciembre',"author":'Joana Marcus',"gender":'Ficcion',"year":'11/11/2021'},
    {"title":'Strange',"author":'Alex Mirez',"gender":'Ficcion',"year":'17/06/2021'}
]
# Ordenar la lista de libros por autor
orderer_books_author =sorted(books, key=get_author)

# Imprimir la lista de libros ordenada por autor
for b in orderer_books_author:
    print(b)
#Ejercicio 4 
print("(4)Ordenando cadenas por longitud//Metodo inserccion")
string_list=["Hello","Te amo","Como estas"]
insertion_sort_by_length(string_list)
print("Lista ordenada: ")
print(string_list)
#Ejercicio 5
print("(5)Modificaremos una lista para ordenarla de manera descendente")
#Utilizaremos la lista del punto (1)
print("Lista ordenada")
bubble_sort_descending(list1)
print(list1)
#Ejercicio 6
print("(6)Ordenaremos por conteo una lista de numeros")
numbers6=[12,563,78,3,2,90,46,1]
sorted_numbers = counting_sort(numbers6)
print("Lista ordenada:")
print(sorted_numbers)
#Ejercicio 7
print("(7)ordenar lista mixta")
mixed_list = [5, "estofado", 2, "banana", 1, "frutilla", 7, "chocolate",9]
print("Lista mixta original:")
print(mixed_list)
sorted_mixed_list = sort_numbers_strings_mix(mixed_list)
print("Lista mixta ordenada con números primero y cadenas después:")
print(sorted_mixed_list)
#Ejercicio 8
print("(8)Ordenar numeros con merge sort")
numbers8=[12,34,21.8,90,-3]
print("Lista ordenada")
merge_sort(numbers8)
print(numbers8)