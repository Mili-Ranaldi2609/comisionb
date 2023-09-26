
import random

def play():

    words = ["while","for","if","else","elif"] # Lista de palabras 
    word = random.choice(words) # Selección al azar de alguna palabra
    guessed_letters = [] # Letras adivinadas
    attempts = 6 # Intentos 

    while attempts > 0:
        hidden_word = ""
        for letter in word:
            if letter in guessed_letters:
                hidden_word += letter
            else:
                hidden_word += "_"

        print("Palabra:", hidden_word)
        print("Intentos restantes:", attempts)
        attempts -= 1 #Se van descontando los intentos
        guess = input("Ingresa una letra, (Aprieta espacio si ya esta completa):").lower() # Ingreso de letra por parte del jugador
        guessed_letters.append(guess) #Se guardan las letras adivinadas en una nueva lista
        if "_" not in hidden_word:
            print("¡FELICIDADES! Adivinaste la palabra:", word)
            break
        elif guess not in word:
            print("¡Letra incorrecta!")
        
    
    if attempts == 0:
        print("¡PERDISTE! La palabra era:", word)


#programa principal
print("Vamos a jugar al ahorcado: ")
print("¡Comencemos!")

#Se llama la funcion play 
play()





