a = input("Enter name: ")
b = input("Enter employee ID: ")
c = input("Enter department: ")
d = float(input("Enter basic salary: "))

e = 0.92 * d
f = 0.58 * d
g = 0.30 * d
h = 500

i = d + e + f + g - h

print("Name:", a)
print("Employee ID:", b)
print("Department:", c)
print("Net Salary:", i)