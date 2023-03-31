import secrets
from art import logo

if input("\nType 'y' to play Blackjack: ").lower() == 'y':
    print(logo)
else:
    quit()

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
players = {}
player_cards = {}

pot = 0

# len() works for dictionaries

# function to deal cards to the players and dealer
def deal(dict):
    # key = ''
    value = []
    for i in dict:
        # key += i
        while len(value) < 2:
            random_card = secrets.choice(cards)
            value.append(random_card)
        player_cards[i] = value



# this loop collects player name and bets while length of the dictionary is less than or equal to 3.
while len(players) <= 3:
    name = input("\nEnter your name: ")
    bet_amount = int(input("Enter your bet: $"))
    players[name] = bet_amount
    pot += bet_amount
    if input("Are there other players? (y or n): ").lower() == 'n':
        break

if input("Type 'Y' to Deal Cards?").lower() == 'y':
    deal(dict=players)