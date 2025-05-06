import art
def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

def calculator():
    print(art.logo)
    should_accumulate=True
    num1 = float(input("what is the number: "))
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol=input("write the operation: ")
        num2=float(input("what is the next number: "))
        answer=operations[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol}{num2} = {answer}")

        choice=input("type y if u want to continue with the answer and n if u want new calculation")
        if choice=="y":
            num1=answer
        else:
            should_accumulate = False
            print("\n"*20)
            calculator()

calculator()






