# Lab 04 - Problem 2: Countdown from a user-given number to zero
number = int(input("Enter a non-negative number: "))

if number < 0:
    print("Please enter a non-negative number.")
else:
    while number >= 0:
        print(number)
        number -= 1
