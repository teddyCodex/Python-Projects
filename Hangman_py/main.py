import secrets
import hangman_art

word_list = ['apple', 'banana', 'orange', 'elephant']
lives = 6

# Generate a random word by selecting from the word_list 
chosen_word = secrets.choice(word_list)

print(hangman_art.logo + '\n')

print('Welcome to Hangman!!')

# display to track player progress
display = []
for i in chosen_word:
    display.append('_')

print(f'The chosen word is {chosen_word}')

# check if guessed letter is in the chosen_word
end_of_game = False

while not end_of_game:
    # get player to guess a letter
    guess = input('Guess a letter: ').lower()

    for i in display:
        if guess == i:
            print(f'You\'ve already guessed this letter: {guess}')
            break
    
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        
        if guess == letter:
            display[position] = letter
    print(f"{' '.join(display)}")
    
    if guess not in chosen_word:
        print(f'You guessed {guess}. That\'s not in the word. You lose a life.')
        lives -= 1
        if lives == 0:
            print('Game Over!')
            end_of_game = True

    if '_' not in display:
        end_of_game = True
        print('You Win!!')
    print(hangman_art.stages[lives])