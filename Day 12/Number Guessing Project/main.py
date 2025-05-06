import random
from art import logo
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5

def check_answer(u_guess,actual_no,turns):
    if u_guess>actual_no:
        print("too high")
        return turns-1
    elif u_guess<actual_no:
        print("too low")
        return turns-1
    else:
        print(f"you made the right guess that is {actual_no}")

def set_difficulty():
    level = input("choose a difficulty level easy or hard: ")
    if level=="easy":
        return EASY_LEVEL_TURNS
    if level=="hard":
        return HARD_LEVEL_TURNS


def play_game():
    print(logo)
    print("welcome to the number guessing game: ")
    print("i am thinking of a number between 1 and 100")
    chosen_no=random.randint(1,100)
    print(f"Pssst, the correct answer is {chosen_no}")

    turns=set_difficulty()

    guess=0
    while guess!=chosen_no:
        print(f"you have {turns} left to attempt.")
        guess = int(input("guess a no : "))
        turns=check_answer(guess,chosen_no,turns)
        if turns==0:
            print("you have run out of lives.")
            return
        elif guess!=chosen_no:
            print("guess again")
play_game()




