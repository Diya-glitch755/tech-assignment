for a in range(1, 6):
    for b in range(1, a + 1):
        print(b, end="")
    print()

for a in range(1, 6):
    for b in range(1, a + 1):
        print(a, end="")
    print()
for a in range(1, 6):
    for b in range(a, 0, -1):
        print(b, end="")
    print()
for a in range(1, 6):
    for b in range(1, a + 1):
        if b % 2 == 0:
            print(0, end="")
        else:
            print(1, end="")
    print()
a = 2
for b in range(1, 5):
    for c in range(b):
        print(a, end=" ")
        a = a + 2
    print()
for a in range(1, 6):
    for b in range(a):
        print("*", end="")
    print()