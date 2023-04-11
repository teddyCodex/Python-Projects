# function to clear screen
def clear():
    print("\033[H\033[J")

import random
import art
from game_data import data

score = 0
# generate random info from the game data list
list_len = len(data)

def random_data():
    random_number = random.randint(0, list_len - 1)
    str_format = f"{data[random_number]['name']}, a {data[random_number]['description']} from {data[random_number]['country']}"
    followers = data[random_number]['follower_count']
    return str_format, followers, random_number


game_active = True

A, a_followers, a_random_num = random_data()
while game_active:
    B, b_followers, b_random_num = random_data()
    if a_random_num == b_random_num:
        B, b_followers, b_random_num = random_data()
    else:
        print(f"\nCompare A: {A}")
        print(art.vs)
        print(f"Compare B: {B}\n")
        game_active = False



# def get_random_data():
#     random_number = random.randint(0, list_len - 1)
#     name = data[random_number]['name']
#     description = data[random_number]['description']
#     follower_count = data[random_number]['follower_count']
#     country = data[random_number]['country']
#     return name, description, follower_count, country, random_number

# def comp_a():
#     name, description, follower_count, country, random_number = get_random_data()
#     return name, description, follower_count, country, random_number

# def comp_b():
#     name, description, follower_count, country, random_number = get_random_data()
#     return name, description, follower_count, country, random_number

# def game(func1, func2):
#     global score
#     game_active = True
#     name_a, description_a, follower_count_a, country_a, rand_a = func1
#     name_b, description_b, follower_count_b, country_b, rand_b = func2

#     if rand_a == rand_b:
#         func2
#     else:
#         A = f"\n{name_a}, a {description_a} from {country_a}"
#         while game_active:
#             B = f"{name_b}, a {description_b} from {country_b}\n"
#             print(f"Compare {str()} {A}")
#             print(art.vs)
#             print(B)
#             answer = input("Who has more IG followers? 'A' or 'B'?: ").lower()
#             if answer != 'a' and answer != 'b':
#                 print('Invalid Input')
#             elif answer == 'a' and follower_count_a > follower_count_b:
#                 print(f"A followers: {follower_count_a}")
#                 print(f"B followers: {follower_count_b}")
#                 print("Correct")

#             elif answer == 'b' and follower_count_b > follower_count_a:
#                 print(f"A followers: {follower_count_a}")
#                 print(f"B followers: {follower_count_b}")
#                 print("Correct")

#             else:
#                 print(f"A followers: {follower_count_a}")
#                 print(f"B followers: {follower_count_b}")
#                 print('Wrong')
#                 game_active = False
#                 break


# game(comp_a(), comp_b())
