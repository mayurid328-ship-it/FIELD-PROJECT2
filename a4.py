# Program to display grade according to marks using if-else ladder

# Input marks from the user
marks = float(input("Enter your marks: "))

# Check grade using if-else ladder
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: Fail")

