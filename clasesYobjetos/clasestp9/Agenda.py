class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
class Agenda:
    
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, telefono, email):
        nuevo_contacto = Contacto(nombre, telefono, email)
        self.contactos.append(nuevo_contacto)
        print(f"Contacto {nombre} agregado.")

    def listar_contactos(self):
        if not self.contactos:
            print("La agenda está vacía.")
        else:
            print("Lista de contactos:")
            for contacto in self.contactos:
                print(f"Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Email: {contacto.email}")

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                print(f"Contacto encontrado - Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Email: {contacto.email}")
                return
            else:
                print(f"Contacto {nombre} no encontrado.")

    def editar_contacto(self, nombre, nuevo_telefono, nuevo_email):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                contacto.telefono = nuevo_telefono
                contacto.email = nuevo_email
                print(f"Contacto {nombre} actualizado.")
