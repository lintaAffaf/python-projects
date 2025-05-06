from game_data import data
from art import logo,vs
import random

#format account data and return into printable format
def format_data(account):
    account_name=account["name"]
    account_desc=account["description"]
    account_country=account["country"]
    return f"{account_name} ,a {account_desc} from  {account_country}"

#check user guess
def check_answer(user_guess,a_followers,b_followers):
    if a_followers>b_followers:
        return user_guess=="a"
    else:
        return user_guess=="b"
#print logo
print(logo)
score=0
game_should_continue=True
#take a random account from data
account_b=random.choice(data)

#make game repeatable
while game_should_continue:
#making acc at position B equal to  A
    account_a = account_b
    account_b = random.choice(data)

    if account_a==account_b:
        account_b=random.choice(data)
     #compare
    print(f"compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
#ask the user for a guess
    guess=input("who has more followers,type A or B:")
#clear the screen
    print("\n"*20)
#get follower count of each account
    a_followers=account_a["follower_count"]
    b_followers=account_b["follower_count"]
    #check if he is right
    is_correct=check_answer(guess,a_followers,b_followers)
#give feedback
#score keeping
    if is_correct:
        score+=1
        print(f"you are right current score is: {score} \n account A:{format_data(account_a)} has {a_followers} followers \n account B  {format_data(account_b)} has {b_followers} followers")


    else:
        print(f"you are wrong score is :{score} \n account A:{format_data(account_a)} has {a_followers} followers \n account B  {format_data(account_b)} has {b_followers} followers")
        game_should_continue=False





