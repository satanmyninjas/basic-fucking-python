base = int(input("Enter your base:\n"))
exponent = int(input("Enter your exponent:\n"))

for _ in range(1, exponent+1):
    print(base, '^', _, '=', base**_)
