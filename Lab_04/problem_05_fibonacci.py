# Lab 04 - Problem 5: Fibonacci numbers below N
n = int(input("Enter N: "))
a, b = 0, 1

while a < n:
    print(a, end=" ")
    a, b = b, a + b
print()
