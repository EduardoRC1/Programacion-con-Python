# Calculadora interactiva usando funciones y un bucle while
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

print("Simple Calculator")
print("Operations: +, -, *, /")
print("Type 'quit' to exit\n")

while True:
    user_input = input("Enter operation (e.g. 5 + 3): ")
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break

    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid format. Use: number operator number")
        continue

    try:
        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Invalid numbers. Try again.")
        continue

    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
    else:
        print("Unknown operator. Use +, -, *, /")
        continue

    print(f"Result: {result}\n")
