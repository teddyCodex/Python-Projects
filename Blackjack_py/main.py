import random

print(
    '''
                                                                                       
88          88                       88        88                       88         
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P"       
    '''
)

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
# dealer_turn = False

# function to deal a card
def deal_card():
    return random.randrange(1, 12)

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


# bet = 50
# input('Type bet amount: ')


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

# print(player_cards)