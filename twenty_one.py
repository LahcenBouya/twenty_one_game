import os
import random
import time


black_jack = """
888     888                888       d8b                888      
888     888                888       Y8P                888      
888     888                888                          888      
88888b. 888 8888b.  .d8888b888  888 8888 8888b.  .d8888b888  888 
888 "88b888    "88bd88P"   888 .88P "888    "88bd88P"   888 .88P 
888  888888.d888888888     888888K   888.d888888888     888888K  
888 d88P888888  888Y88b.   888 "88b  888888  888Y88b.   888 "88b 
88888P" 888"Y888888 "Y8888P888  888  888"Y888888 "Y8888P888  888 
                                     888                         
                                    d88P                         
                                  888P"     
"""



def clear_screen():
    """this function clear the terminal"""
    os.system("cls" if os.name == "nt" else "clear")


def deal_card():
    """this function return random numbers"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """this function calculate the score of players"""
    #if the sum of cards equal 21 => blackjack
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    #if the sum of cards over than 21 and the player had card 11
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    """this function compare between scores"""
    results = {
        "darw" : "It's a draw😀\n\n",
        "user_over" : "Sorry, the computer is the winner😂\n\n",
        "computer_over" : "the computer is over 21 so you win😁\n\n",
        "user_21" : "you win with blackjack😎\n\n",
        "computer_21" : "computer has blackjack🙄\n\n",
        "user_win" : "congratulations, you win\n\n",
        "user_lose" : "you lose\n\n",
    }

    if user_score == computer_score:
        return results["darw"]
    elif user_score == 0:
        return results["user_21"]
    elif computer_score == 0:
        return results["computer_21"]
    elif user_score > 21:
        return results["user_over"]
    elif computer_score > 21:
        return results["computer_over"]
    elif user_score > computer_score:
        return results["user_win"]
    else:
        return results["user_lose"]








def game():
    """this function is the main program"""
    #list comprehension
    user_cards = [deal_card() for _ in range(2)]
    computer_cards = [deal_card() for _ in range(2)]
    game_continue = True
    while game_continue:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"\n\n\nyour cards are {user_cards}, current score is {sum(user_cards)}")
        print(f"computer's first card is {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21 or computer_score > 21:

            game_continue = False

        else:
            user_take_another_card = input("get another cards? y/n: ").lower()
            if user_take_another_card == "y":
                user_cards.append(deal_card())
            else:
                game_continue = False
        
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(f"your final hand: {user_cards} with score {user_score}")
    print(f"computer's final hand: {computer_cards} with score {computer_score}")
    time.sleep(2)
    print(compare(user_score, computer_score))
    time.sleep(10)
    clear_screen()
    print("please wait...")
    time.sleep(3)
    clear_screen()



while input("choose a game to start........\n\n1- Froggy\n2- Twenty one\n3- Snake\n\n").lower() == "twenty one":
    time.sleep(2)
    print("please wait.....")
    time.sleep(2)
    clear_screen()
    print(black_jack)
    game()
