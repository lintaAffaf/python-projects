print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age=int(input("what is your age?"))
    if age<=12:
        print("pay 5 Rs")
    elif age<=18:
        print("pay 10 Rs")
    else:
        print("pay 20 Rs")
else:
    print("Sorry you have to grow taller before you can ride.")
