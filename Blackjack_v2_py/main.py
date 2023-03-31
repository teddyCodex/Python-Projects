import secrets
from art import logo

if input("\nType 'y' to play Blackjack: ").lower() == 'y':
    print(logo)
else:
    quit()

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

blackjack_multiplier = 2.5
win_multiplier = 2