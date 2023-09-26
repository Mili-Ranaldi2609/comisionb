from funciones_calculadora import *
#MENU

while True:

    '''Mostramos las operaciones al usuario'''
    print('Seleccion la operacion que desea realizar:')
    print('1 - Suma\n2 - Resta\n3 - Multiplicacion\n4 - División')

    '''Capturamos la opcion que ingrese el usuario y la guardamos en una variable'''
    opcion = input('Opcion: ')

    if opcion in ('1','2','3','4'):
        '''Pedimos al usuario que ingrese los operandos'''
        num1 = input('Ingrese el primer número a operar: ')
        num2 = input('Ingrese el segundo valor a operar: ')

        if opcion == '1':
            print(f'{num1} + {num2} = {suma(num1,num2)}')
        elif opcion == '2':
            print(f'{num1} - {num2} = {resta(num1,num2)}')
        elif opcion == '3':
            print(f'{num1} * {num2} = {multiplicacion(num1,num2)}')
        elif opcion == '4':
            print(f'{num1} / {num2} = {division(num1,num2)}')
    else:
        print('Operación inválida.')

    '''Daremos al usuario la opcion de terminar la ejecucion o continuar operando'''
    salir = input('Quiere seguir operando? Para salir ingrese X, de lo contrario ingrese cualquier letra: ').lower()

    if salir == 'x':
        break
    else:
        continue