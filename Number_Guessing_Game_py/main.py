from art import logo
import random

print(logo)
print('\nCan you read my mind?\n')

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

def reduce_turns(correct_guess):
    '''
    Takes a boolean to determine whether to reduce user_turns
    Returns user_turns less 1.
    '''
    if correct_guess == False:
        return user_turns - 1

def turns_equal_one():
    '''
    Checks if user score is not equal to one
    if true, prints Guess Again to the console
    '''
    if user_turns != 1:
        print('Guess Again.')

random_number = random.randint(1, 101)
# print(f"\nThe number is {random_number}\n")

while user_turns > 0:
    if user_turns == 1:
        print(f"You have {user_turns} guess left.")
    else:
        print(f"You have {user_turns} guesses left.")
    try:
        guess = int(input('\nGuess my number: '))
        if guess == random_number:
            print(f'\nYou guessed right!! The number is {random_number}')
            break
        elif guess > random_number:
            print('\nToo High.')
            if user_turns != 1:
                print('Guess Again.')
            user_turns = reduce_turns(False)
        else:
            print('\nToo Low.')
            if user_turns != 1:
                print('Guess Again.')
            user_turns = reduce_turns(False)
    except ValueError:
        # catch non-integer inputs
        print("\nOops! That's not a number. Try Again.")

if user_turns == 0:
    print('\nYou ran out of turns. Game Over!')
    print(f'The number was {random_number}\n')