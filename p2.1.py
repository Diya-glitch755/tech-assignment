a = float(input("Enter voltage (V): "))
b = float(input("Enter resistance (R): "))

c = a / b

print("Current:", c)

if c < 0.5:
    print("Low current")
elif c <= 2:
    print("Normal current")
else:
    print("High current")