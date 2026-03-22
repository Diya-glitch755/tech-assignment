a = tuple(map(int, input("Enter prices: ").split()))

print("a)", len(a))
print("b)", min(a))
print("c)", max(a))
print("d)", tuple(sorted(a)))

m = max(a)
print("e)", a.count(m))