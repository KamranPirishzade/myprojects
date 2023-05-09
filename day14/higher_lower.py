from game_data import data
from art import vs,logo
import random

point=0
game_continue=True
first_item=random.choice(data)
second_item=random.choice(data)
def game():
    global game_continue
    print(f"Compare A: {first_item['name']},{first_item['description']},{first_item['country']}")
    print(vs)
    print(f"Against B: {second_item['name']},{second_item['description']},{second_item['country']}")
    if first_item["follower_count"]>second_item["follower_count"]:
        winner=first_item
    else :
        winner=second_item
    choose=input("Which one is higher A or B :").upper()
    if choose=="A" and winner==first_item:

        game_continue=True
    elif choose=="B" and winner==second_item:
        game_continue=True
    else:
        print(f"You lose, you have {point} point.")
        game_continue=False

while game_continue:
    print(logo)
    point=0
    game()
    while game_continue:
        point+=1
        first_item=second_item
        second_item=random.choice(data)
        while second_item==first_item:
            second_item=random.choice(data)
        print(100000 * "\n")
        print(logo)
        print(f"It is True, Your final score:{point}")
        game()
















