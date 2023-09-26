# Funciones

'''Función que recibe dos números como parámetros y
devuelve la suma de los mismos'''

def suma(a, b):
    return (a+b)

'''Funcion que recibe dos números como parámetros y
devuelve la resta de los mismos'''

def resta(a, b):
    return (a-b)

'''Funcion que recibe dos números como parámetros y
devuelve la multiplicación de los mismos'''

def multiplicacion(a, b):
    return (a*b)

'''Funcion que recibe dos numeros como parametros y
devuelve la division de los mismos'''

def division(a, b):
    if(b == 0):
        return ("No se puede dividir por cero!")
    else:
        return (a/b)
