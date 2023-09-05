print("Ingrese los datos tal cual han sido pedidos en el ejemplo")
fecha=input("Ingrese la fecha (dia, DD/MM) ")

dia_semana=fecha[0: fecha.find(',')]
dia=int(fecha[fecha.find(' ') + 1: fecha.find('/')])
mes=int(fecha[fecha.find('/')+1:])

dia_semana=dia_semana.lower()

if (dia_semana!="lunes") and (dia_semana!= "martes") and (dia_semana!= "miercoles") and (dia_semana!="jueves")and (dia_semana!="viernes"):
    print("Se produjo un error reinicie el programa")
else:
    if (dia<=31 and  dia>0 ) and (mes<=12 and mes>0):
        nivel=dia_semana
        if (nivel=="lunes") or (nivel=="martes") or (nivel=="miercoles"):        
            y_n=input("Hubo examenes? (si/no): ")
            y_n=y_n.lower()
            if y_n=="si":
                aprobados=int(input("Ingrese la cantidad de aprobados: "))
                desaprobados=int(input("Ingrese la cantidad de desaprobados: "))
                porcentaje=(aprobados/(aprobados+desaprobados))*100
                print(f"El porcentaje de aprobados es de: {porcentaje}%")
            else:
                print("Termino el programa")
        elif nivel=="jueves":
            asistencia=int(input("Porcentaje de asistencia: "))
            if asistencia>50:
                print("Asistio la mayoria:")
            else:
                print("No asistio la mayoria")
        elif nivel=="viernes":
            if dia==1 and (mes==1 or mes==7):
                print("Comienzo de nuevo ciclo: ")
                alumnos=int(input("Cantidad de alumnos: "))
                arancel=float(input("Arancel por alumno: $"))
                print(f"Ingreso total: ${alumnos*arancel}")