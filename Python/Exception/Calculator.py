# Features:
# Addition: Add two numbers.
# Subtraction: Subtract one number from another.
# Multiplication: Multiply two numbers.
# Division: Divide one number by another.
# Exception Handling: Implement try-except blocks to handle potential errors,
# such as division by zero or invalid input.
import argparse

def check_for_invalid_data(*args):
    for arg in args:
        if arg is None:
            raise ValueError("One of the argument is None")
        if type(arg) != int:
            raise ValueError("One of the argument is not a number")
        if int(arg) < 0:
            raise ValueError("Negative values are invalid")


def add(a, b):
    check_for_invalid_data(a, b)
    return a + b


def sub(a, b):
    check_for_invalid_data(a, b)
    return a - b


def mul(a, b):
    check_for_invalid_data(a, b)
    return a * b


def div(a, b):
    check_for_invalid_data(a, b)
    return a // b

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Calculator',
        description='this program runs basic calculations')
    parser.add_argument('operations', choices=['add', 'sub', 'mul', 'div'],
                        help="operations for calculation")
    parser.add_argument('--num1', type=int, help="number1")
    parser.add_argument('--num2', type=int, help="number1")
    args = parser.parse_args()

    if args.operation == "add":
        add(a=args.number1, b=args.number2)
    elif args.operation == "sub":
        sub(a=args.number1, b=args.number2)
    elif args.operation == "mul":
        mul(a=args.number1, b=args.number2)
    elif args.operation == "div":
        div(a=args.number1, b=args.number2)
    else:
        raise ValueError("Invalid operation")



