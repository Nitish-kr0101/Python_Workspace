
try:
    num = int(input("Enter number: "))
    print(".....")
    print(10/num)
    print("HEllo")

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

except ValueError:
    print("Error: Invalid Input!")

finally:
    print("Execution Completed")