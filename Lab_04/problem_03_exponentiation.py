# Lab 04 - Problem 3: Calculate exponentiation using a loop
base = float(input("Enter base: "))
exponent = int(input("Enter integer exponent: "))

if base == 0 and exponent < 0:
    print("Undefined: zero cannot have a negative exponent.")
else:
    result = 1
    for _ in range(abs(exponent)):
        result *= base
    if exponent < 0:
        result = 1 / result
    print("Result:", result)
