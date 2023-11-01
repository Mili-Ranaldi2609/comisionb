class MutantDetector:
    def __init__(self, adn):
        # Constructor
        self.adn = adn

    def is_mutant(self):
        def check_sequence(sequence):# Funcion  para verificar si una secuencia de ADN contiene cuatro letras consecutivas e iguales
            return any(all(sequence[i] == sequence[i + 1] for i in range(3)) for i in range(len(sequence) - 3))
        #Numero de filas y columnas de la matriz 
        rows = len(self.adn)
        cols = len(self.adn[0])
        #CONTADOR DE LAS VECES QUE SE CUMPLEN LA SECUENCIA DE 4 LETRAS IGUALES
        mutant_count = 0
        for i in range(rows):
            for j in range(cols):
                #Comprobar cada celda de la matriz
                #Horizontal
                
                if j + 3 < cols and check_sequence([self.adn[i][j], self.adn[i][j + 1], self.adn[i][j + 2], self.adn[i][j + 3]]):
                    mutant_count += 1#SECUENCIA MUTANTE +1
                

                #Vertical
                if i + 3 < rows and check_sequence([self.adn[i][j], self.adn[i + 1][j], self.adn[i + 2][j], self.adn[i + 3][j]]):
                    mutant_count += 1#SECUENCIA MUTANTE +1
                

                #Diagonal de izquierda a derecha
                if i + 3 < rows and j + 3 < cols and check_sequence([self.adn[i][j], self.adn[i + 1][j + 1], self.adn[i + 2][j + 2], self.adn[i + 3][j + 3]]):
                    mutant_count += 1 #SECUENCIA MUTANTE +1
                

                #Diagonal de derecha a izquierda
                if i + 3 < rows and j - 3 >= 0 and check_sequence([self.adn[i][j], self.adn[i + 1][j - 1], self.adn[i + 2][j - 2], self.adn[i + 3][j - 3]]):
                    mutant_count += 1#SECUENCIA MUTANTE +1
                    
        if  mutant_count > 1:
            return True
        else:
            return False




