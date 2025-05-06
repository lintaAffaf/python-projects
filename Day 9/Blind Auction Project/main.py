# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

def find_highest_bidder(bidding_record):
    highest_bid=0
    winner=""
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"the winner is {winner }with bid ${highest_bid}")

bid={}
continue_bidding=True
while continue_bidding:
    name=input("what is your name?")
    price=int(input("write your bid price:  $"))
    bid[name]=price
    should_continue=input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue=="no":
        continue_bidding=False
        find_highest_bidder(bid)
    else:
        print("\n"*20)






