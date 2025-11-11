# Program to find the factorial of a number using a loop

# Input a number from the user
num = int(input("Enter a number: "))

# Initialize factorial variable
factorial = 1

# Calculate factorial using a for loop
for i in range(1, num + 1):
    factorial *= i  # same as factorial = factorial * i

# Display the result
print(f"The factorial of {num} is {factorial}")

# Program to find factorial using a while loop

num = int(input("Enter a number: "))
factorial = 1
i = 1

while i <= num:
    factorial *= i
    i += 1

print(f"The factorial of {num} is {factorial}")
