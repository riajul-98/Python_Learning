def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

from art import logo


def calculator():
    print(logo)
    n1 = float(input("What is the first number? "))
    for operand in operations:
        print(operand)
    operation_symbol = input("Please choose an operation from the above: ")
    n2 = float(input("What is the second number? "))
    answer = operations[operation_symbol](n1, n2)

    print(f"{n1} {operation_symbol} {n2} = {answer}")

    go_again = True
    while go_again:
        again = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to restart.: ")
        if again == 'n':
            go_again = False
            calculator()
        operation_symbol = input("Pick another operation: ")
        n3 = float(input("Whats the next number?: "))
        new_answer = operations[operation_symbol](answer, n3)
        print(f"{answer} {operation_symbol} {n3} = {new_answer}")
        answer = new_answer


calculator()
