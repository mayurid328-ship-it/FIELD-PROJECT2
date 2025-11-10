# Program to check whether a year is a leap year or not

# Input a year from the user
year = int(input("Enter a year: "))

# Check for leap year
if (year % 400 == 0):
    print(f"{year} is a leap year.")
elif (year % 100 == 0):
    print(f"{year} is not a leap year.")
elif (year % 4 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
