def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def main():
    try:
        print("\nSimple Calculator")

        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        operation = input("Enter operation (+, -, *, /): ")

        if operation == "+":
            result = add(x, y)
        elif operation == "-":
            result = subtract(x, y)
        elif operation == "*":
            result = multiply(x, y)
        elif operation == "/":
            result = divide(x, y)
        else:
            print("Invalid operation.")
            return

        print(f"Result: {result}")

    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()