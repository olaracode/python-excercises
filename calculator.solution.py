def add(x, y):
    """This function adds two numbers"""

    return x + y


def subtract(x, y):
    """This function subtracts two numbers"""

    return x - y


def multiply(x, y):
    """This function multiplies two numbers"""

    return x * y


def divide(x, y):
    """This function divides two numbers"""

    return x / y

# Displaying Menu


def menu():
    print("Enter '0' to Exit")
    print("Enter '1' to Add")
    print("Enter '2' to Subtract")
    print("Enter '3' to Multiply")
    print("Enter '4' to Divide")


# Checking for Valid Choice
running = True
while running:
    menu()
    choice = input("Enter your choice(1/2/3/4): ")
    if (choice == '0'):
        running = False
        break
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid input")
