a = input("Enter a string: ")

v = 0
c = 0
s = 0
l = 0

for i in a:
    if i in "aeiouAEIOU":
        v += 1
    elif i.isalpha():
        c += 1
    if i == " ":
        s += 1
    if i.islower():
        l += 1

print("a)", v)
print("b)", c)
print("c)", s)
print("d)", l)