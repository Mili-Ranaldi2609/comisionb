class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    def imprimir_lado_mayor(self):
        lados = [self.lado1, self.lado2, self.lado3]
        lado_mayor = max(lados)
        print(f"El lado con mayor longitud es: {lado_mayor}")

    def determinar_tipo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "isósceles"
        else:
            return "escaleno"
