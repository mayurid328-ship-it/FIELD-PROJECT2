# Program to reverse a given number using a loop

# Input a number from the user
num = int(input("Enter a number: "))

reverse = 0  # Variable to store the reversed number
temp = num   # Keep original number safe for display

# Loop to reverse the digits
while num > 0:
    digit = num % 10           # Get the last digit
    reverse = reverse * 10 + digit  # Add it to the reversed number
    num = num // 10            # Remove the last digit

# Display the reversed number
print(f"The reverse of {temp} is {reverse}")
