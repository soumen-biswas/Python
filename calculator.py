# Function Definitions for Calculator Operations
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error! Division by zero."


def modulus(a, b):
    try:
        return a % b
    except ZeroDivisionError:
        return "Error! Division by zero."


# User Input Handling
def get_operation_choice():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")

    while True:
        choice = input("Enter choice (1/2/3/4/5): ")
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        else:
            print("Invalid input. Please enter a valid choice.")


def get_number_input(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Main Function
def calculator():
    while True:
        choice = get_operation_choice()

        num1 = get_number_input("Enter first number: ")
        num2 = get_number_input("Enter second number: ")

        if choice == '1':
            result = add(num1, num2)
            operation = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            operation = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            operation = '*'
        elif choice == '4':
            result = divide(num1, num2)
            operation = '/'
        elif choice == '5':
            result = modulus(num1, num2)
            operation = '%'

        print(f"{num1} {operation} {num2} = {result}")

        # Ask the user if they want to perform another calculation
        next_calculation = input("Would you like to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break


# Run the calculator
calculator()
