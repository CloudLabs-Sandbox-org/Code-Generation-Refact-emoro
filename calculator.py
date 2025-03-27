# Create a basic calculator
# that can perform addition, subtraction,
# multiplication, and division operations.
# The calculator should be able to handle
# floating-point numbers and should be able to
# handle exceptions for invalid inputs.

import sys

def display_menu():
    print("=" * 30)
    print(" Welcome to the Basic Calculator ")
    print("=" * 30)
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("=" * 30)

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def perform_operation(choice, num1, num2):
    try:
        if choice == 1:
            return num1 + num2
        elif choice == 2:
            return num1 - num2
        elif choice == 3:
            return num1 * num2
        elif choice == 4:
            if num2 == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            return num1 / num2
    except ZeroDivisionError as e:
        print(e)
        return None

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice == 5:
                print("Thank you for using the calculator. Goodbye!")
                sys.exit()
            elif choice in [1, 2, 3, 4]:
                num1 = get_float_input("Enter the first number: ")
                num2 = get_float_input("Enter the second number: ")
                result = perform_operation(choice, num1, num2)
                if result is not None:
                    print(f"The result is: {result}")
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

