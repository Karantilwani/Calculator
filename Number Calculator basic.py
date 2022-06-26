# This project contains codes to make a basic calculator which can perform basic calculations.

print("Welcome to my calculator!!", "\n""Here you can do basic calculations. So let's start", "\n")


def multiply(a, b):
    return a * b


def subtract(a, b):
    return a - b


def add(a, b):
    return a + b


def divide(a, b):
    return a / b


while True:
    num1 = int(input("Enter Number 1: "))
    num2 = int(input("Enter Number 2: "))

    choice = str(input("Enter action ('+' to add, '-' to subtract, '*' to multiply & '/' to divide): "))

    while True:

        if choice == '*':
            print("The result is =", multiply(num1, num2), "\n")
            break
        elif choice == '-':
            print("The result is =", subtract(num1, num2), "\n")
            break
        elif choice == '+':
            print("The result is =", add(num1, num2), "\n")
            break
        elif choice == '/':
            print("The result is =", divide(num1, num2), "\n")
            break
        else:
            print("Invalid Input!!", "Enter valid Input!!")
            choice = str(input("Enter action ('+' to add, '-' to subtract, '*' to multiply & '/' to divide): "))
