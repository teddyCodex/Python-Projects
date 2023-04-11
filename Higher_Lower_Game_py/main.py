import random
import art
from game_data import data

score = 0
list_len = len(data)
game_active = True

# function to clear screen
def clear():
    print("\033[H\033[J")
    print(art.logo)

def main():
    clear()

def random_data():
    random_number = random.randint(0, list_len - 1)
    str_format = f"{data[random_number]['name']}, a {data[random_number]['description']} from {data[random_number]['country']}"
    followers = data[random_number]['follower_count']
    return str_format, followers, random_number

def correct():
    global score, A, B
    score += 1
    A = B
    clear() 

A = random_data()
while game_active:
    if score != 0:
        print(f"You're right! Current Score: {score}")
    B = random_data()
    if A[2] == B[2]:
        B = random_data()
    else:           
        print(f"\nCompare A: {A[0]}")
        print(art.vs)
        print(f"Compare B: {B[0]}\n")
        answer = input("Who has more IG followers? 'A' or 'B': ").lower()
        if answer == 'a':
            if A[1] >= B[1]:
                correct()
            else:
                print(f"Sorry, that's wrong. Final score: {score}\n")
                game_active = False
        elif answer == 'b':
            if B[1] >= A[1]:
                correct()
            else:
                print(f"Sorry, that's wrong. Final score: {score}\n")
                game_active = False
        else:
            print('Invalid Input')

if __name__ == '__main__':
    main()