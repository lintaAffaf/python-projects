print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill=5
        print("child tickets are $5.")
    elif age <= 18:
        bill=7
        print("youth tickets are $7.")
    else:
        bill=10
        print("adult tickets are $12.")
        wants_photo=input("do u want to take a photo y for yes and N for no :")
        if wants_photo=="y":
            bill += 3
            print(f"your total bill is  {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
