from clasestp9.Persona import Persona
from clasestp9.Cuenta import Cuenta
from clasestp9.Triangulo import Triangulo
from clasestp9.Agenda import Agenda
#1
persona1=Persona("Jose Hernandez", 21, 23456782)
persona1.mostrar()
persona1.set_nombre()
persona1.set_edad()
persona1.set_dni()
print("¿Es mayor de edad?", persona1.esMayorDeEdad())

persona2=Persona("Lucas Jofre",16,12345)
persona2.mostrar()
persona2.set_nombre()
persona2.set_edad()
persona2.set_dni()
print("¿Es mayor de edad?", persona2.esMayorDeEdad())

persona3=Persona("Maicol Emanuel", 2, 123087265)
persona3.mostrar()
persona3.set_nombre()
persona3.set_edad()
persona3.set_dni()
print("¿Es mayor de edad?", persona3.esMayorDeEdad())
#2
cuenta1 = Cuenta("Juan Pérez", 1000.0)
cuenta1.mostrar()
cuenta1.ingresar(500.0)
cuenta1.retirar(200.0)

cuenta2= Cuenta("Jose Gutierrez",500.0)
cuenta2.mostrar()
cuenta2.retirar(300.00)
cuenta2.ingresar(50.00)
#3
lado1=float(input("Ingrese el lado 1 del triangulo "))
lado2=float(input("Ingrese el lado 2 del triangulo "))
lado3=float(input("Ingrese el lado 3 del triangulo "))
triangulo1= Triangulo(lado1,lado2,lado3)
triangulo1.imprimir_lado_mayor()
tipo_trian=triangulo1.determinar_tipo()
print(f"El tipo del triangulo es: {tipo_trian}")
#4
mi_agenda = Agenda()

while True:
        print("\nMenú de Agenda:")
        print("1. Añadir contacto")
        print("2. Lista de contactos")
        print("3. Buscar contacto")
        print("4. Editar contacto")
        print("5. Cerrar agenda")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del contacto: ").lower()
            telefono = input("Teléfono del contacto: ")
            email = input("Email del contacto: ").lower()
            mi_agenda.agregar_contacto(nombre, telefono, email)
        elif opcion == "2":
            mi_agenda.listar_contactos()
        elif opcion == "3":
            nombre = input("Nombre del contacto a buscar: ").lower()
            mi_agenda.buscar_contacto(nombre)
        elif opcion == "4":
            nombre = input("Nombre del contacto a editar: ").lower()
            nuevo_telefono = input("Nuevo teléfono: ")
            nuevo_email = input("Nuevo email: ").lower()
            mi_agenda.editar_contacto(nombre, nuevo_telefono, nuevo_email)
        elif opcion == "5":
            print("Agenda cerrada. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")
