def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b if b != 0 else "Error"

operations = {
    1: add,
    2: sub,
    3: mul,
    4: div
}

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
choice = int(input("Enter choice (1-4): "))

result = operations.get(choice, lambda x, y: "Invalid choice")(a, b)
print("Result:", result)