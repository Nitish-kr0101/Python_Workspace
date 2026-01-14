
from employee_utility.leave_calculator import calculate_leave_deduction

def calculate_bonus(basic_salary, designation):
    designation = designation.lower()

    if designation == "coder":
        return basic_salary * 0.10
    elif designation == "designer":
        return basic_salary * 0.15
    elif designation == "manager":
        return basic_salary * 0.05
    else:
        return 0


def calculate_final_salary(basic_salary, designation, leaves_taken):
    bonus = calculate_bonus(basic_salary, designation)
    deduction = calculate_leave_deduction(basic_salary, leaves_taken)

    final_salary = basic_salary + bonus - deduction
    return final_salary
