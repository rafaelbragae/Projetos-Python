# Step 1
from playsound import playsound
import random
import os

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["algoritmo", "barco", "camelo", "dado", "empada", "faca", "gorila", "helicoptero", "pasta", "macaco",
             "xadrez"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
# #Testing code
# print(f'The solution is {chosen_word}.')
print("Bem Vindo ao Jogo da Forca\n")
# TODO-2: - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
for letter in chosen_word:
    display += "_"

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
vidas = 6
stage = 6
finish = False
win = False
lose = False
letras = []
print(f"{' '.join(display)}")
print(stages[6])
while finish == False:
    guess = input("Tente adivinhar uma letra: ").lower()
    letras.append(guess)

    # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Loop through each position in the chosen_word;
    aux = 0

    print("\n\n\n")
    print(f"Letras já escolhidas: {letras}")
    while aux < len(chosen_word):
        if guess not in chosen_word:
            print("Você escolheu uma letra que não existe nessa palavra. Perdeu uma vida.")
            vidas -= 1
            stage -= 1
            if vidas == 0:
                finish = True
            break
        else:
            if chosen_word[aux] == guess:
                display[aux] = guess
        aux += 1

    print(f"{' '.join(display)}")
    print(stages[stage])
    if '_' not in display:
        finish = True
        win = True
if win == True:
    playsound("claps-44774.mp3")
    print("\nVocê ganhou! 😁")

else:
    playsound("boo-6377.mp3")
    print(f"\nVocê perdeu o jogo! 😢\nA palavra correta era {chosen_word}.")
