a = float(input("Enter hardness: "))
b = float(input("Enter carbon content: "))
c = float(input("Enter tensile strength: "))

x = a > 50
y = b < 0.7
z = c > 5600

if x and y and z:
    print("Grade is 10")
elif x and y:
    print("Grade is 9")
elif y and z:
    print("Grade is 8")
elif x and z:
    print("Grade is 7")
elif x or y or z:
    print("Grade is 6")
else:
    print("Grade is 5")