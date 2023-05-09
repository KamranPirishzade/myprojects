from logo import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def game():
        print(logo)
        your_cards = []
        computer_cards = []
        comp_total=0
        current_score=0
        comp_condition = True
        if playing_game=="y":
            for c in range(2):
                computer_cards.append(random.choice(cards))
                your_cards.append(random.choice(cards))
            current_score=sum(your_cards)
            print(f"Your cards {your_cards} , current score: {current_score}")
            comp_total=sum(computer_cards)
            print(f"Computer first card: {computer_cards[0]}")
            if current_score>21 :
                new_card="n"
            else:
                new_card = input("Type 'y' to get another card, type 'n' to pass:")
            if comp_total>=17:
                new_card="n"
        while new_card=="y":
            your_cards.append(random.choice(cards))
            current_score =sum(your_cards)
            for xyz in your_cards:
                if xyz==11:
                    current_score>21
                    current_score-=10
                    index_ace_you=your_cards.index(xyz)
                    your_cards[index_ace_you]=1
            print(f"Your card :{your_cards},New card : {your_cards[-1]}")
            print(f"Your score: {current_score}")
            print(f"Computer first card: {computer_cards[0]}")

            if current_score>=21:
                new_card = "n"
            else:
                new_card =input("Type 'y' to get another card, type 'n' to pass:")

        print(f"Computer cards: {computer_cards}, Second computer card:{computer_cards[1]}")
        if comp_total >= 17:
            comp_condition = False
        while comp_condition :
            second_comp_card=random.choice(cards)
            computer_cards.append(second_comp_card)
            print(f"New comp card: {computer_cards[-1 ]}")
            comp_total=comp_total+second_comp_card
            for zyx in computer_cards:
                if zyx==11:
                    if comp_total>21:
                        comp_total-=10
                        index_ace=computer_cards.index(zyx)
                        computer_cards[index_ace]=1
            print(f"Computer cards:{computer_cards}, Computer score: {comp_total} \n")
            if current_score>21:
               comp_condition=False
            if comp_total>=17:
                comp_condition=False

        if current_score>21:
            print("You lose")
        elif current_score>comp_total :
            print("You win.")
        elif current_score<comp_total and comp_total>21:
            print("You win.")
        elif current_score==comp_total:
            print("Draw.")
        elif current_score<comp_total:
            print("You lose.")
        res_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")

playing_game=input("Do you want to play game ? 'y' or 'n': ")
while playing_game=="y":
    game()
