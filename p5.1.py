a = tuple(map(int, input("Enter integers: ").split()))

print("a)", len(a))
print("b)", a[-1])
print("c)", a[::-1])

if 5 in a:
    print("d) 5 is present")
else:
    print("d) 5 is not present")

b = a[1:-1]
print("e)", b)