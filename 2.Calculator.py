import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def modulus(x, y):
    return x % y

def power(x, y):
    return x ** y

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def calculator():
    print("Simple Calculator")
    print("Operations: + (Addition), - (Subtraction), * (Multiplication), / (Division), % (Modulus), ** (Power), sin, cos, tan")

    while True:
        operation = input("\nEnter the operation (+, -, *, /, %, **, sin, cos, tan): ").strip().lower()

        if operation in ['sin', 'cos', 'tan']:
            try:
                num = float(input("Enter the angle in degrees: ").strip())
                if operation == 'sin':
                    result = sine(num)
                elif operation == 'cos':
                    result = cosine(num)
                elif operation == 'tan':
                    result = tangent(num)
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
                continue
        else:
            try:
                num1 = float(input("Enter the first number: ").strip())
                num2 = float(input("Enter the second number: ").strip())

                if operation == '+':
                    result = add(num1, num2)
                elif operation == '-':
                    result = subtract(num1, num2)
                elif operation == '*':
                    result = multiply(num1, num2)
                elif operation == '/':
                    result = divide(num1, num2)
                elif operation == '%':
                    result = modulus(num1, num2)
                elif operation == '**':
                    result = power(num1, num2)
                else:
                    print("Invalid operation! Please choose from +, -, *, /, %, **, sin, cos, tan.")
                    continue

            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

        print(f"Result: {result}")


        cont = input("Do you want to perform another calculation? (yes to continue, any other key to exit): ").strip().lower()
        if cont != 'yes':
            print("Exiting the calculator. Goodbye!")
            break

if __name__ == "__main__":
    calculator()
