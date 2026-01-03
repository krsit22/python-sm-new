a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Choose operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter choice (1-4): "))

match choice:
    case 1:
        print("Result:", a + b)
    case 2:
        print("Result:", a - b)
    case 3:
        print("Result:", a * b)
    case 4:
        if b != 0:
            print("Result:", a / b)
        else:
            print("Division by zero not allowed")
    case _:
        print("Invalid choice")