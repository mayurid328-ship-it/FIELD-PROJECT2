# Program to display the sum of all even numbers between 1 and 50

sum_even = 0  # Variable to store the sum

# Loop through numbers from 1 to 50
for i in range(1, 51):
    if i % 2 == 0:  # Check if the number is even
        sum_even += i

# Display the result
print("The sum of all even numbers between 1 and 50 is:", sum_even)

sum_even = 0
for i in range(2, 51, 2):  # start=2, stop=51, step=2
    sum_even += i

print("The sum of all even numbers between 1 and 50 is:", sum_even)
