
class BingoCard:
    def __init__(self):
        self.card = [[0]*5 for _ in range(5)]#carton
        self.numbers = set()

    def generate_card(self, numbers):
        for i in range(5):
            for j in range(5):
                self.card[i][j] = numbers.pop()

    def display_card(self):
        print("=== Bingo Card ===")
        for row in self.card:
            print(" ".join(str(num) if num != 0 else 'X' for num in row))
        print("==================")

    def mark_number(self, number):
        for i in range(5):
            for j in range(5):
                if self.card[i][j] == number:
                    self.card[i][j] = 0

    def check_bingo(self):
        for i in range(5):
            if all(num == 0 for num in self.card[i]):
                return True
            if all(num == 0 for num in [self.card[j][i] for j in range(5)]):
                return True
        if all(num == 0 for num in [self.card[i][i] for i in range(5)]) or all(num == 0 for num in [self.card[i][4-i] for i in range(5)]):
            return True
        return False

def get_unique_number(prompt, existing_numbers, lower, upper):
    while True:
        try:
            number = int(input(prompt))
            if number < lower or number > upper:
                print(f"El número debe estar entre {lower} y {upper}")
            elif number in existing_numbers:
                print("¡Ya has ingresado ese número!")
            else:
                return number
        except ValueError:
                print("Por favor, ingresa un número válido.")