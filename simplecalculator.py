Simple Calculator
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!" 
    return a / b

print("=" * 22)
print("       SIMPLE CALCULATOR")
print("=" * 34)
print("Addition       : " + str(add(10, 5)))
print("Subtraction    : " + str(subtract(10, 5)))
print("Multiplication : " + str(multiply(35, 5)))
print("Division       : " + str(divide(10, 21)))
print("Division by 0  : " + str(divide(10, 0)))
print("=" * 34)
