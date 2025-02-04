from idlelib.debugger_r import restart_subprocess_debugger

from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = float(input("What's the first number?: "))

while True:
    for symbol in operations:
        print(symbol)
    op = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))

    result = operations[op](num1, num2)

    print(f"{num1} {op} {num2} = {result}")

    keep = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

    if keep == "y":
        num1 = result
    else:
        print("\n" * 20)
        print(logo)
        num1 = float(input("What's the first number?: "))