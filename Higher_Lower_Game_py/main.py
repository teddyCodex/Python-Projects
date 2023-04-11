# function to clear screen
def clear():
    print("\033[H\033[J")
    print(art.logo)

import random
import art
from game_data import data

clear()

score = 0
# generate random info from the game data list
list_len = len(data)

def random_data():
    random_number = random.randint(0, list_len - 1)
    str_format = f"{data[random_number]['name']}, a {data[random_number]['description']} from {data[random_number]['country']}"
    followers = data[random_number]['follower_count']
    return str_format, followers, random_number



# def run_game()
game_active = True

A, a_followers, a_random_num = random_data()
while game_active:
    if score != 0:
        print(f"You're right! Current Score: {score}")
    B, b_followers, b_random_num = random_data()
    if a_random_num == b_random_num:
        B, b_followers, b_random_num = random_data()
    else:
        def correct():
            global score, a_followers, b_followers, a_random_num, b_random_num, A, B
            score += 1
            A = B
            a_followers = b_followers
            a_random_num = b_random_num
            clear()            
        print(f"\nCompare A: {A}")
        print(art.vs)
        print(f"Compare B: {B}\n")
        answer = input("Who has more IG followers? 'A' or 'B': ").lower()
        if answer == 'a':
            if a_followers > b_followers:
                correct()
            else:
                print(f"Sorry, that's wrong. Final score: {score}\n")
                game_active = False
        elif answer == 'b':
            if b_followers > a_followers:
                correct()
            else:
                print(f"Sorry, that's wrong. Final score: {score}\n")
                game_active = False
        else:
            print('Invalid Input')
