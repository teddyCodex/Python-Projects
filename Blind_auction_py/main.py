import art

# function to clear screen
def clear():
    print("\033[H\033[J")

print(art.logo)
print('Welcome to the James Dean Blind Auction\n')

bidders = {}

while True:
    user_name = input("Please enter your name: \n")
    user_bid = input("Please enter your bid: \n$")

    def collect_bids(name, bid):
        global bidders
        bidders[name] = bid

    collect_bids(name=user_name, bid=user_bid, )

    while True:
        more_bids = input('Are there more bids? (Yes or No): \n').lower()
        if more_bids == 'yes':
            clear()
            break
        elif more_bids == 'no':
            break
        else:
            print("Invalid Input")
    if more_bids == 'no':
        break

def max_bid(dict):
    list_of_names = []
    list_of_bids = []
    for i in dict:
        list_of_names.append(i)
        list_of_bids.append(dict[i])
    
    highest_bid = max(list_of_bids)
    index_of_highest_bid = list_of_bids.index(highest_bid)
    winner = list_of_names[index_of_highest_bid]
    print(f"The Winner of the James Dean Silent Auction is {winner} with a bid of ${highest_bid}\n")

max_bid(bidders)