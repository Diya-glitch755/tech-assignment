a = input("Enter vendor name: ")
b = input("Enter year of association: ")
c = input("Enter contact number: ")
d = input("Enter email ID: ")

total = 0
for i in range(1, 13):
    e = float(input("Enter purchase for month " + str(i) + ": "))
    total = total + e

print("Vendor Name:", a)
print("Annual Purchase:", total)