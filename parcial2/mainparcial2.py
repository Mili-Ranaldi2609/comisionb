from clasesparcial2 import MutantDetector

while True:
    print("////Menú////")
    print("(1) Detectar si un ADN es mutante")
    print("(2) Salir")   
    option = input(": ")

    if option == "1":
        adn = []
        for i in range(6):
            while True:
                row = input(f"Ingrese la fila {(i+1)} de la secuencia de ADN (exactamente 6 letras): ").upper()
                # Verifica que la fila tenga  6 letras:
                if len(row) == 6 and all(c in "ATCG" for c in row):#Se verifica que las letras ingresadas sean A,T,C o G
                    break
                else:
                    print("Error: Debe ingresar exactamente 6 letras válidas (ATCG).")
            adn.append(row)

        detector = MutantDetector(adn)
        if detector.is_mutant():
            print("El humano es mutante (ºOº). Sera reclutado por MAGNETO.")
        else:
            print("El humano no es mutante (-_-). Prueba finalizada.  ")
    elif option == "2":
        print("Programa finalizado (>u<)")
        break
    else:
        print("Opcion invalida. Por favor, elija nuevamente.")
"""
#Caso A (True)
adn_mutante_o_no = [ 
        "ATGCTA" ,
        "TCAGTC",
        "TTTTAA",
        "AGTAAA",
        "GGTTCA" ,
        "AAAATA"
        ]
si_es=MutantDetector(adn_mutante_o_no)
if si_es.is_mutant():
    print("Caso A: El humano es mutante.")
else:
    print("Caso A: El humano no es mutante.")

#Caso B(False)
adn_mutante_o_no2=[
        "AAATTT",
        "GGGCCC",
        "ATCGAT",
        "TTAAAG",
        "GGGCCC",
        "AAAATA"

]
no_es=MutantDetector(adn_mutante_o_no2)
if no_es.is_mutant():
    print("Caso B: El humano es mutante.")
else:
    print("Caso B: El humano no es mutante.")"""





