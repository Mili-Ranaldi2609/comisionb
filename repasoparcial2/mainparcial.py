from cartonBingo import BingoCard, get_unique_number
import random 
card_numbers = set()
for _ in range(25):
    card_numbers.add(get_unique_number("Ingresa un número (1-75): ", card_numbers, 1, 75))

player_card = BingoCard()
player_card.generate_card(list(card_numbers))
player_card.display_card()

drawn_numbers = set()
while True:
    input("Presiona Enter para sacar una bola...")
    drawn_number = random.randint(1, 75)
    drawn_numbers.add(drawn_number)
    print(f"Has sacado el número {drawn_number}")
    player_card.mark_number(drawn_number)
    player_card.display_card()

    if player_card.check_bingo():
        print("¡Bingo! ¡Has ganado!")
        break

    play_again = input("¿Quieres continuar jugando con el carton? (s/n): ").lower()
    if play_again == 'n':
        break
    elif play_again != 's':
        play_again=input("Caracter invalido ingrese nuevamente: ").lower()
        
