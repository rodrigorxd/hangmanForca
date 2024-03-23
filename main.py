import random
import hangman_phases

wordlist = ["football", "computer", "mango", "banana", "mouse", "water", "window", "apple"]

out_of_chances = False
correct = False
chances_left = 6
word_progress = []

#Choosing a word from the given list - Escolhendo uma palavra da lista dada
selected_word = random.choice(wordlist)

word_length = len(selected_word)

#Creating a string that will be replaced as the user scores - String que será trocada pelas letras a medida que o usuário acerta
for spaces in selected_word:
    word_progress += "_"

print(f"Welcome to the Hangman game!!!{hangman_phases.hangman_phase[6]}\n"
      f"You have 6 chances to answer (ONLY ONE LETTER for guess)!\n"
      f"WORD: {word_length} characters")

#Game code - Lógica do jogo
while (not out_of_chances) and (not correct):
    print(f"\nYou have {chances_left} chances left!\n{hangman_phases.hangman_phase[6 - chances_left]}\n{word_progress}")
    guess = input("Type your guess:").lower()
    #If the guess is correct, write the guessed letter in the respective index - Se acertar a letra, trocar o "_" pela letra no index certo
    if guess in selected_word:
        print("You guessed correct!")
        for i in range(word_length):
           if guess == selected_word[i]:
               word_progress[i] = guess
    else:
        print("You guessed wrong!")
        chances_left -= 1
    #No more blank spaces = win - Sem espaços em branco = vitória
    if "_" not in word_progress:
        #while end
        print(f"\nYou've won!\nThe word was: {selected_word}")
        correct = True
    #No more chances = lose - Sem chances restantes = derrota
    if chances_left == 0:
        #while end
        out_of_chances = True
        print(f"\nYou've run out of chances!\nThe word was: {selected_word}")