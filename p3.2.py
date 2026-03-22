for a in range(65, 70):
    for b in range(65, a + 1):
        print(chr(b), end="")
    print()
for a in range(1, 6):
    for b in range(a):
        print("#", end=" ")
    print()
a = "python"
for b in range(len(a)):
    print(a[0:b+1])