import random
from art import logo, vs
from game_data import data

import random

def select_random_item(data_list, quantity = 2, filter_name = str):
    if quantity not in (1, 2):
        raise ValueError("A quantity de itens deve ser 1 ou 2.")
    
    if quantity == 2:
        selector1 = random.randint(0, len(data_list) - 1)
        selector2 = random.randint(0, len(data_list) - 1)
        while selector1 == selector2:
            selector2 = random.randint(0, len(data_list) - 1)
        
        itemA = data_list[selector1]
        itemB = data_list[selector2]
        return itemA, itemB
    else:
        selector = random.randint(0, len(data_list) - 1)
        item = data_list[selector]
        while item['name'] == filter_name:
            selector = random.randint(0, len(data_list)-1)
        print(f"Item singular retornado: {item}")
        return item


def game_start(a, b):
    print(logo)
    print(f"Compare a. {a['name']}, a {a['description']}, from {a['country']}")
    print(vs)
    print(f"b. {b['name']}, a {b['description']}, from {b['country']}")

    guess = input("Wich one do you think has the most followers (a/b)? ")
    return guess


def highest_follower(a, b):
    print(f"Follower_count A = {a['follower_count']}")
    print(f"Follower_count B = {b['follower_count']}")
    if a["follower_count"] > b["follower_count"]:
        return "a"
    else:
        return "b"


def verify_guess(user_guess, anwser):
    if user_guess == anwser:
        print(f"Caso 1: {user_guess}, anwser: {anwser}")
        return True
    # elif user_guess == anwser:
    #     print(f"Caso 2: {user_guess}, anwser: {anwser}")
    #     return True
    else:
        print(f"Caso 2: {user_guess}, anwser: {anwser}")
        return False
    

def correct_anwser(a, b, score):
    print(logo)
    print(f"Congratulations, you got it right! Your score: {score} ")
    print(f"Compare a. {a['name']}, a {a['description']}, from {a['country']}")
    print(vs)
    print(f"b. {b['name']}, a {b['description']}, from {b['country']}")

    guess = input("Wich one do you think has the most followers (a/b)? ")
    return guess


def wrong_anwser():
    print(logo)
    print("Sorry, you got the wrong anwser :(")
    repeat = input("Do you wish to play again (y/n)? ")
    return repeat


def main():
    score = 0
    game_data = data
    item_a, item_b = select_random_item(game_data, 2)
    anwser = highest_follower(item_a, item_b)
    guess = game_start(item_a, item_b)
    print(f"Guess: {guess}")

    while True:
        if guess == "a":
            print("If A")
            verification = verify_guess(guess, anwser)
            if verification:
                score += 1
                game_data.remove(item_a)
                item_b = select_random_item(game_data, 1, item_b["name"])
                print(f"Item A: {item_a}, Item B: {item_b}")
                anwser = highest_follower(item_a, item_b)
                guess = correct_anwser(item_a, item_b, score)
            else:
                repeat = wrong_anwser()
                if repeat == "y":
                    main()
                else:
                    print("Thanks for playing!")
                    break
        else:
            print("Else")
            verification = verify_guess(guess, anwser)
            if verification:
                score += 1
                game_data.remove(item_b)
                item_a = item_b
                item_b = select_random_item(game_data, 1, item_a["name"])
                print(f"item A: {item_a}, item b: {item_b}")
                anwser = highest_follower(item_a, item_b)
                guess = correct_anwser(item_a, item_b, score)
            else:
                repeat = wrong_anwser()
                if repeat == "y":
                    main()
                else:
                    print("Thanks for playing!")
                    break


main()