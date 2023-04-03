#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import art
import secrets

# print(art.logo)
print('Can you read my mind?\n')

while True:
    difficulty = input("Select Difficulty. 'easy' or 'hard'?: ").lower()
    if difficulty == 'easy':
        user_turns = 10
        break
    elif difficulty == 'hard':
        user_turns = 5
        break
    else:
        print('Invalid Input. Try Again.\n')