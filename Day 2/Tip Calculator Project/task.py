print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_percent=tip/100
total_tip_amount=tip_percent*bill
total_bill=total_tip_amount+bill
bill_per_person=total_bill/people
round(bill_per_person, 2)

#bill_me= (bill + ((tip/100)*bill))/people

print(f"Each person should pay : {bill_per_person}")


