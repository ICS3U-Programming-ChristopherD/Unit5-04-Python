#!/usr/bin/env python3

# Created by: Chris Di Bert
# Date: Nov.30, 2022
# This program performs calculations on two number


def Calculator(num1, num2, operation):

    # Match case statement structure used for each possible operation
    match operation:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2
        case "%":
            return num1 % num2
        case _:
            return "-1"


def main():
    # Gets the two numbers from the user
    num1_str = input("Enter a number: ")

    num2_str = input("Enter a second number: ")

    # Tries casting the numbers to float
    try:
        num1_user = float(num1_str)
        num2_user = float(num2_str)
    except:
        input("You must enter a number for both inputs.")

    print("\nOperations: +, -, *, /, %")

    # Gets the operation from the user
    operation_user = input("Enter an operation: ")

    # Storing return value inside the result variable
    result = Calculator(num1_user, num2_user, operation_user)

    # Body code executed if the user entered an invalid operation
    if result == -1:
        print(f"\n{operation_user} is not a valid operation.")

    else:
        # Displays the sum/product of the calculation
        print(f"\n{num1_user} {operation_user} {num2_user} = {result}")


if __name__ == "__main__":
    main()
