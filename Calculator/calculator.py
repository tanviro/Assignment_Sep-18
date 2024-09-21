def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Power")
    
    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice in ['1', '2', '3', '4', '5', '6']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(f"Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {divide(num1, num2)}")
        elif choice == '5':
            print(f"Result: {modulus(num1, num2)}")
        elif choice == '6':
            print(f"Result: {power(num1, num2)}")
    else:
        print("Invalid input, please choose a valid operation.")


calculator()
