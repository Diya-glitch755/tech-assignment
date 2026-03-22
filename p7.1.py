def add(a, b):
    print("Result:", a + b)

def sub(a, b):
    print("Result:", a - b)

def mul(a, b):
    print("Result:", a * b)

def div(a, b):
    print("Result:", a / b)

def mod(a, b):
    print("Result:", a % b)

while True:
    print("\n1.Add  2.Sub  3.Mul  4.Div  5.Mod  6.Exit")
    ch = int(input("Enter choice: "))

    if ch == 6:
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if ch == 1:
        add(a, b)
    elif ch == 2:
        sub(a, b)
    elif ch == 3:
        mul(a, b)
    elif ch == 4:
        div(a, b)
    elif ch == 5:
        mod(a, b)