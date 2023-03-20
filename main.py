import random

score = 0
player1_score = 0
player2_score = 0

# reset cumulative score only
def reset():
    global score
    score = 0

# function to toss a coin
def coin_toss():
    toss_coin = random.randint(1,2)
    # toss_coin = 1
    return toss_coin


def player2_turn():
    global player2_score
    print('\n*** PLAYER 2 TURN ***\n')
    print(f'player 2 score: {player2_score}')
    roll = input('Type Roll to roll dice: ').lower()
    if roll == 'roll':
        def dice_roll():
            global score
            global player2_score
            roll_dice = random.randint(1,6)
            print(f'You rolled {roll_dice}')
            if roll_dice == 1:
                print('Player lost Turn')
                reset()
                print(f'player 2 score: {player2_score}') # test
                player1_turn()
            else:
                score += roll_dice
                print(f'Your score this round is {score}\n')
                def next_turn():
                    global score
                    global player1_score
                    global player2_score
                    turn = input('Roll or Hold: ').lower()
                    if turn == 'roll':
                        dice_roll()
                    elif turn == 'hold':
                        player2_score += score
                        print(f'Your current held score is: {player2_score}')
                        print(f'player 2 score: {player2_score}') # test
                        reset()
                        print(f'player 2 score: {player2_score}') # test
                        player1_turn()
                    else:
                        print('Invalid Input!')
                        next_turn()
                next_turn()
    else:
        print('Invalid Input! Try Again.')
        player2_turn()
    dice_roll()


# player turn sequence
def player1_turn():
    global player1_score
    print('\n*** PLAYER 1 TURN ***\n')
    print(f'player 1 score: {player1_score}')
    roll = input('Type Roll to roll dice: ').lower()
    if roll == 'roll':
        def dice_roll():
            global score
            roll_dice = random.randint(1,6)
            print(f'You rolled {roll_dice}')
            if roll_dice == 1:
                print('Player lost Turn')
                reset()
                print(f'player 1 score: {player1_score}') # test
                player2_turn()
            else:
                score += roll_dice
                print(f'Your score this round is {score}\n')
                def next_turn():
                    global score
                    global player1_score
                    global player2_score
                    turn = input('Roll or Hold: ').lower()
                    if turn == 'roll':
                        dice_roll()
                    elif turn == 'hold':
                        player1_score += score
                        print(f'Your current held score is: {player1_score}')
                        print(f'player 1 score: {player1_score}') # test
                        reset()
                        print(f'player 1 score: {player1_score}') # test
                        player2_turn()
                    else:
                        print('Invalid Input!')
                        next_turn()
                next_turn()
    else:
        print('Invalid Input! Try Again.')
        player1_turn()
    dice_roll()



# start game sequence
def start_game():
    start = input("\nType start to toss coin: ").lower()
    if start == 'start':
        print('\n***** Coin Toss!! *****\n')
        result = coin_toss()
        if result == 1:
            print('Heads!')
            print(f'Player 1 to start!!')
            player1_turn()
            # return result
            # player1_turn()
        else:
            print('Tails!')
            print('Player 2 to start!!')
            player2_turn()
            # return result
    else:
        print('Invalid Input')
        start_game()




# print(start_game())
start_game()