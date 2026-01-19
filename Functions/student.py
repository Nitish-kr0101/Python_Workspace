"""
Program: Student Utility Program
Purpose: Demonstrates how to define and use functions in Python
"""

def greet_student(name):
    """Displays a greeting message for the student."""
    print(f"Hello {name}, welcome to the Python class!")


def calculate_total(marks):
    """Returns the sum of all marks."""
    return sum(marks)


def calculate_average(total, count):
    """Returns the average of the marks."""
    return total / count


def check_result(average):
    """Checks whether the student has passed or failed."""
    if average >= 40:
        return "PASS"
    return "FAIL"


def display_result(name, marks):
    """Processes marks and displays the complete result."""
    total = calculate_total(marks)
    average = calculate_average(total, len(marks))
    result = check_result(average)

    greet_student(name)
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", average)
    print("Result:", result)


# Program execution starts here
if __name__ == "__main__":
    student_name = "Nitish"
    student_marks = [72, 68, 75, 80, 64]

    display_result(student_name, student_marks)
