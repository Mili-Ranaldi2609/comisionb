#Ejercicio 1 
print("Ejercicio 1")
passenger_list= []
list_cities = []

# Función para agregar pasajeros a la lista de viajeros
def add_passenger():
    name = input("Nombre del pasajero: ").lower()
    dni = int(input("DNI del pasajero: "))
    destination= input("Destino del pasajero: ").lower()
    passenger_list.append((name, dni, destination))
    print("Pasajero agregado con éxito.")

# Función para agregar ciudades a la lista de ciudades
def add_city():
    city = input("Nombre de la ciudad: ").lower()
    country = input("País de la ciudad: ").lower
    list_cities.append((city, country))
    print("Ciudad agregada con éxito.")

# Función para buscar el destino de un pasajero por DNI
def search_destinationDni(dni):
    for p in passenger_list:
        if p[1] == dni:
            return p[2]
    return None

# Función para contar la cantidad de pasajeros que viajan a una ciudad
def count_passenger_cities(city):
    count = 0
    for p in passenger_list:
        if p [2] == city:
            count += 1
    return count

# Función para buscar el país de destino de un pasajero por DNI
def search_countryDni(dni):
    destination = search_destinationDni(dni)
    for city, country in list_cities:
        if city == destination:
            return country
    return None

# Función para contar la cantidad de pasajeros que viajan a un país
def count_passenger_country(country):
    count = 0
    for p in list_cities:
        destination = search_destinationDni(p[1])
        city, destination_country = [city_country for city_country in list_cities if city_country[0] == destination][0]
        if destination_country == country:
            count += 1
    return count

# Menú iterativo
while True:
    print("\nMenú:")
    print("1. Agregar pasajero")
    print("2. Agregar ciudad")
    print("3. Buscar destino por DNI")
    print("4. Contar pasajeros por ciudad")
    print("5. Buscar país por DNI")
    print("6. Contar pasajeros por país")
    print("7. Salir")
    option = input("Elija una opción: ")

    if option == '1':
        add_passenger()
    elif option == '2':
        add_city()
    elif option == '3':
        dni = int(input("Ingrese el DNI del pasajero: "))
        destination = search_destinationDni(dni)
        if destination:
            print(f"El pasajero viaja a {destination}.")
        else:
            print("El pasajero no se encuentra en la lista.")
    elif option == '4':
        city = input("Ingrese el nombre de la ciudad: ")
        count = count_passenger_cities(city)
        print(f"{count} pasajeros viajan a {city}.")
    elif option == '5':
        dni = int(input("Ingrese el DNI del pasajero: "))
        country = search_countryDni(dni)
        if country:
            print(f"El pasajero viaja a {country}.")
        else:
            print("El pasajero no se encuentra en la lista.")
    elif option == '6':
        country = input("Ingrese el nombre del país: ")
        count = count_passenger_country(country)
        print(f"{count} pasajeros viajan a {country}.")
    elif option == '7':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intente nuevamente.")

#Ejercicio 2
print("Ejercicio 2 (calles y domicilio)")
def obtain_invoice_addresses(sales):
    invoice_addresses= set()  # Utilizamos un conjunto para almacenar los domicilios únicos
    
    for s in sales:
        customer, _, _, home = s 
# Desempaquetamos la tupla
        invoice_addresses.add(home)  

# Agregamos el domicilio al conjunto
    
    # Convertimos el conjunto en una lista para el resultado
    list_invoice_addresses= list(invoice_addresses)
    
    return list_invoice_addresses
#principal
print("Ventas realizadas")
sales = [('Nuria Costa', 5, 1234.5, 'Calle 1 - 456'), ('Jorge Russo', 7, 3999, 'Calle 2 - 741'),
('Nuria Costa', 12, 789.0, 'Calle 1 - 456')]
print(sales)
print("Domicilios a enviar la factura: ")
addresses = obtain_invoice_addresses(sales)
print(addresses)

#Ejercicio 3
# Definir el diccionario con los socios fundadores
members = {
    1: ['Amanda Nuñez','17/03/2009','True']  ,
    2: ['Barbara Molina', '17/03/2009','True'],
    3: ['Lautaro Campos','17/03/2009', 'True'],
    4:['Jose Hernandez','13/03/2018', 'False'],
    5:['Lucas Bustamante','13/03/2018', 'True']
}

# Función para marcar las cuotas al día de un socio
def pay_fee(members):
    while True:
        try:
            member_num = int(input(f"\n Ingrese el N° del socio: "))
            if member_num > len(members):
                print("Ese N° de socio no existe.\n")
                break
            else:
                if members[member_num][2] == 'True':
                    print("El socio ya estba al día.\n")
                else:
                    members[member_num][2] = 'True'
                    print("Ahora el socio está al día.\n")
                break
        except ValueError:
            print("Ingrese un N° de socio válido")
# Función para modificar la fecha de ingreso de los socios del 13/03/2018
def fix_date(members):
    dates_to_fix = 0
    for key in members:
        if members[key][1] == "13/03/2018":
            members[key][1] = "14/03/2018"
            dates_to_fix += 1
    if dates_to_fix > 0:
        print("Fechas Corregidas.\n")
    else:
        print("No habian fechas a corregir.\n")

# Función para dar de baja a un socio

def delete_member(members):
    member_name = input("Ingrese el Nombre y Apellido del socio: ").title()
    keys_to_delete = []  
# Crear una lista de claves a eliminar
    for key in members:
        if members[key][0] == member_name:
            keys_to_delete.append(key)  # Agregar la clave a la lista de claves a eliminar

    for key in keys_to_delete:
        del members[key]  # Eliminar las claves después de completar el bucle

    if keys_to_delete:
        print(f"El socio {member_name} se ha dado de baja")
    else:
        print(f"No se encontró al socio {member_name}")
#Imprimir la lista completa de socios
def show_members(members):
    for key in members:
        name = members[key][0]
        join_date = members[key][1]
        if members[key][2] == "s":
            fee = "Cuota al día"
        else:
            fee = "Adeuda cuotas"
        print(f"Socio N°{key}, {name}, ingresó: {join_date}, {fee}")
#Principal
print("¡Bienvenido al club, Bellavista!")
while True:
    print("Ingrese la opcion deseada: ")
    print("1-Cantidad de socios del club")
    print("2-Deudas Pagadas")
    print("3-Eliminar socio")
    print("4-Corregir fechas de ingreso")
    print("5-Listado de socios")
    print("6-Salir")
    option3=int(input(""))
    if option3==1:
        print(f"La cantidad de socios es: {len(members)}")
    elif option3==2:
        pay_fee(members)
    elif option3==3:
        delete_member(members)
    elif option3==4:
        fix_date(members)
    elif option3==5:
        show_members(members)
    elif option3==6:
        break
    else:
        print("La opcion ingresada es invalida reinicie el programa")
        break
