try:
    print(10 / 0)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")

try:
    int("abc")
except ValueError:
    print("Error: Invalid number")

try:
    [1, 2, 3][10]
except IndexError:
    print("Error: Index out of range")

try:
    {"name": "Alaguvel"}["age"]
except KeyError:
    print("Error: Key not found")

try:
    num = int("50")
    print("Valid:", num)
finally:
    print("all ok , program finished")
