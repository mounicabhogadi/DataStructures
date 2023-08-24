# Features:
# Addition: Add two numbers.
# Subtraction: Subtract one number from another.
# Multiplication: Multiply two numbers.
# Division: Divide one number by another.
# Exception Handling: Implement try-except blocks to handle potential errors,
# such as division by zero or invalid input.
import argparse


class NegativeNumberException(Exception):
    pass


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
    print(a + b)


def sub(a, b):
    check_for_invalid_data(a, b)
    if a < b:
        raise ValueError("Number1 can't be less than Number2")
    print(a - b)


def mul(a, b):
    check_for_invalid_data(a, b)
    print(a * b)


def div(a, b):
    check_for_invalid_data(a, b)
    print(a // b)


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
        try:
            sub(a=args.number1, b=args.number2)
        except ValueError:
            print("Subtracting number2 from number1 is not possible, hence swap")
            sub(a=args.number2, b=args.number1)
    elif args.operation == "mul":
        mul(a=args.number1, b=args.number2)
    elif args.operation == "div":
        try:
            div(a=args.number1, b=args.number2)
        except ZeroDivisionError:
            print("Division with zero is invalid, instead divide with 1")
            div(a=args.number1, b=1)
        except NegativeNumberException:
            print("Numbers cannot be negative, converting positive")
            div(a=abs(args.number1), b=abs(args.number2))
    else:
        raise ValueError("Invalid operation")



