
#Ejercicio 18

sal_hora=float(input("Le pediremos por favor que ingrese su salario por hora: "))
mes_hora=float(input("Y sus horas trabajadas durante el mes: "))

hora_t_min=48
hora_extra=mes_hora-hora_t_min

print(f"Horas extras trabajadas: {hora_extra}")

sal_total=(hora_t_min*sal_hora)+(hora_extra*sal_hora*1.1)

print(f"Salario total: ${sal_total}")


#Ejercicio 19
#Ejercicio 20