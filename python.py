# Addition
def add(x, y):
    return x + y

# Subtraction
def subtract(x, y):
    return x - y

# Multiplication
def multiply(x, y):
    return x * y

# Division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y

# Reminder
def reminder(x, y):
    return x % y

# Main  
def main():
    print("Simple Calculator")
    print("-" * 20)
    print("Print ! to exit")
    print("-" * 20)

    while True:
        print("-" * 20)
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Reminder")
        print("-" * 20)
        
        user_input = input("Enter your choice: ")
        if user_input == "!":
            break

        if user_input not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue

        try:
            x = int(input("Enter X: "))
            y = int(input("Enter Y: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if user_input == "1":
            res = add(x, y)
        elif user_input == "2":
            res = subtract(x, y)
        elif user_input == "3":
            res = multiply(x, y)
        elif user_input == "4":
            res = divide(x, y)
        elif user_input == "5":
            res = reminder(x, y)

        print("Answer:", res)

main()
