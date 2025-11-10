# Program to find the greatest among three numbers

# Input three numbers from the user
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

# Compare the numbers using if-else
if a >= b and a >= c:
    print(f"The greatest number is {a}")
elif b >= a and b >= c:
    print(f"The greatest number is {b}")
else:
    print(f"The greatest number is {c}")
