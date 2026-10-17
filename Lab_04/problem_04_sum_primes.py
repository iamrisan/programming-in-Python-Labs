# Lab 04 - Problem 4: Sum of all prime numbers below 1000
total = 0

for number in range(2, 1000):
    is_prime = True
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            is_prime = False
            break
    if is_prime:
        total += number

print("Sum of primes below 1000:", total)
