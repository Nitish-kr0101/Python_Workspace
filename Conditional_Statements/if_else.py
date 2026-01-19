print("Enter Your Marks")
marks = int(input())

if marks > 70:
    print("Distinction")
elif marks >= 60 and marks <= 70:
    print("First Division")
elif marks > 50:
    print("Second Division")
else:
    print("Invalid Marks")
