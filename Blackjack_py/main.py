import random
from art import logo

print(logo)

player_cards = []
dealer_cards = []
blackjack = False
outcomes = {
    'win': 'You Win!!\n',
    'lost': 'You Lost!\n',
    'bust': 'Bust! You Lost!\n',
    'draw': 'It\'s a draw!\n',
    'blackjack': 'Blackjack! You Win!!\n'
}

# function to deal a card
def deal_card():
    return random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])

# function to check player total
def check_total(list):
    return sum(list)

# function to display cards
def display_cards(name):
    if name == player_cards:
        display = 'Player\'s Cards: '
    else:
        display = 'Dealer\'s Cards: '
    for i in name:
        display += f' {str(i)} '
    print(display)
    print(f'Total: {check_total(name)}')
    print('\n')


while not blackjack:
    while len(player_cards) < 2:
        player_cards.append(deal_card())
    dealer_cards.append(deal_card())

    if check_total(player_cards) > 21:
        display_cards(player_cards)
        outcomes['lost']
        break
    else:
        display_cards(player_cards)
        display_cards(dealer_cards)

    if check_total(player_cards) == 21:
        print(outcomes['blackjack'])
        blackjack = True
        break
    
    
    while check_total(player_cards) < 21:
        # hit or stand
        choice = input('Hit or Stand?: ').lower()
        if choice == 'hit':
            player_cards.append(deal_card())
            if check_total(player_cards) > 21:
                display_cards(player_cards)
                display_cards(dealer_cards)
                print(outcomes['bust'])
            else:
                display_cards(player_cards)
                display_cards(dealer_cards)
        if choice == 'stand':
            dealer_cards.append(deal_card())
            display_cards(player_cards)
            display_cards(dealer_cards)
            while check_total(dealer_cards) <= 17:
                dealer_cards.append(deal_card())
                # display_cards
            # display_cards(player_cards)
            display_cards(dealer_cards)

            if check_total(player_cards) < check_total(dealer_cards) and check_total(dealer_cards) <= 21:
                print(outcomes['lost'])
                break
            elif check_total(player_cards) == check_total(dealer_cards):
                print(outcomes['draw'])
                break
            else:
                print(outcomes['win'])
                break
    if check_total(player_cards) == 21:
        print(outcomes['win'])



    blackjack = True
