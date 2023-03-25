import random

player_funds = 0
player_cards = []
dealer_cards = []

#   Functions are defined from this point
def init():
    global player_funds, player_cards, dealer_cards
    player_funds = 0
    player_cards = []
    dealer_cards = []

def start():
    global player_funds
    init()
    deposit = int(input('\nHow much will you be playing with today?: '))
    player_funds += deposit
    bet()
    # return player_funds

def bet():
    global player_funds
    if player_funds <= 0:
        print('Player has no funds!')
        start()
    else:
        while True:
            try:
                bet_value = int(input('Enter Bet Amount: '))
                if bet_value > player_funds:
                    print('Player has Insufficient Funds')
                else:
                    player_funds -= bet_value
                    return bet_value
            except ValueError:
                print('Invalid input. Please enter an integer.')
    
def deal():
    card = random.randint(1, 10)
    return card

def first_round():
    global player_cards, dealer_cards
    while True:
        start = input('Type Start or Exit: ').lower()
        if start == 'start':
            for i in range(2):
                player_cards.append(deal())
            dealer_cards.append(deal())
            print(f'Your cards: {player_cards}')
            print(f'Dealers cards: {dealer_cards}')
            return player_cards
            break
        elif start == 'exit':
            exit()
        else:
            print('Invalid Input')
#   Functions End Here


#   Function Calls
start()
first_round()
# bet()
# print(bet())
print(f'\nTests\nPlayer funds = {player_funds}')
print(f'Player Cards = {player_cards}')
# print(deal())
