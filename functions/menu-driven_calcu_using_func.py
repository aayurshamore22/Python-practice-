def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter choice: "))

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if choice == 1:
    print(add(x, y))
elif choice == 2:
    print(sub(x, y))
elif choice == 3:
    print(mul(x, y))
elif choice == 4:
    print(div(x, y))
else:
    print("Invalid Choice")
