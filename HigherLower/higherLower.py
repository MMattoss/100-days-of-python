import random
from art import logo, vs
from game_data import data

def select_random_item():
    selector1 = random.randint(1, len(data))
    selector2 = random.randint(1, len(data))

    while selector1 == selector2:
        selector2 = random.randint(1, len(data))

    itemA = data[selector1]
    itemB = data[selector2]

    return itemA, itemB


item_a, item_b = select_random_item()

def game_start():

    print(logo)
    print(f"Compare a. {item_a['name']}, a {item_a['description']}, from {item_a['country']}")
    print(vs)
    print(f"b. {item_b['name']}, a {item_b['description']}, from {item_b['country']}")

    guess = input("Wich one you think has more followers (a/b)? ")

game_start()


# Define which one has the most followers
def highest_follower(a, b):
    if a > b:
        
# Define if user selected the correct one

# If the user got it right -> Add a point, lowest item becomes item A, highest is removed from the data list and new
# item from data list becomes item B (Loop)

# If the user got it wrong -> Print losing message, quit loop and ask if they want to play again
