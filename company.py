'''
SIMPLE CALCULATOR
'''

# Add two numbers
def add(x, y):
    return x + y

# Subtract two numbers
def subtract(x, y):
    return x - y

# Multiplie two numbers
def multiply(x, y):
    return x * y

# Divide two numbers
def divide(x, y):
    return x / y

while True:
    # take operator input from the user
    choice = input("Enter the operation ( + , - , * , / ) : ")

    # check if choice is one of the four options
    if choice in ('+', '-', '*', '/'):
        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number: "))

        if choice == '+':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '*':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '/':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation, if 'no', break the while loop
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")
