import logo

print(logo.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operators = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide,
}

def calculator():
    num1 = float(input("Input the first number: "))

    while True:
        for i in operators:
            print(i)
        chosen_operator = input('Choose an operation: ')

        num2 = float(input("Input the next number: "))

        answer = operators[chosen_operator](num1, num2)

        print(f"{num1} {chosen_operator} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            print("\033[H\033[J")
            calculator()

calculator()