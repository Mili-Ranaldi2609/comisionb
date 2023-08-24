#Ejercicio 1

anio_comp=int(input("Ingrese los años de su computador: "))

if anio_comp<=2:
    print("El computador es nuevo ")
else:
    print("El computador es viejo ")

#Ejercicio 2

anio_comp=int(input("Ingrese los años de su computador: "))

if anio_comp<0:

    print("No se puede ingresar un numero negativo ")

elif anio_comp<=2:
    print("El computador es nuevo ")
else:
    print("El computador es viejo ")

#Ejercicio 3

print("Te pediremos que ingreses dos nombres y los vamos a comparar: ")

nombre01=input("Nombre de la primer persona: ").capitalize()
nombre02=input("Nombre de la segunda persona: ").capitalize()

if nombre01[0]==nombre02[0]:
    print("Coincidencia ")
else:
    print("No hay coincidencia ")
#Ejercicio 18

sal_hora=float(input("Le pediremos por favor que ingrese su salario por hora: "))
mes_hora=float(input("Y sus horas trabajadas durante el mes: "))

hora_t_min=48
hora_extra=mes_hora-hora_t_min

print(f"Horas extras trabajadas: {hora_extra}")

sal_total=(hora_t_min*sal_hora)+(hora_extra*sal_hora*1.1)

print(f"Salario total: ${sal_total}")


#Ejercicio 19

cantidad_lapiz=int(input("Ingrese la cantidad de lapices a comprar: "))
costo_lapiz=60


if cantidad_lapiz>=1000:

    sin_descuento=costo_lapiz*cantidad_lapiz
    descuento=(sin_descuento*7)/100
    costo_total=sin_descuento-descuento
    print(f"El monto total a pagar es de: ${costo_total}")
else:
    sin_descuento=costo_lapiz*cantidad_lapiz
    print(f"El monto total a pagar es de: ${sin_descuento}")



#Ejercicio 20

print("Te pediremos que ingreses tus notas: ")

nota_1=int(input("Primer nota: "))
nota_2=int(input("Segunda nota: "))
nota_3=int(input("Tercer nota: "))
nota_4=int(input("Cuarta nota: "))
    
promedio=(nota_1+nota_2+nota_3+nota_4)/4

if promedio>=6:
    print(f"Aprobaste con: {promedio}")
else:
    print(F"Desaprobaste con: {promedio}")