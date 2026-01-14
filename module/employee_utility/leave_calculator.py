
def calculate_leave_deduction(basic_salary, leaves_taken):
    allowed_leaves = 15
    per_day_salary = basic_salary / 30

    if leaves_taken > allowed_leaves:
        extra_leaves = leaves_taken - allowed_leaves
        deduction = extra_leaves * per_day_salary
        return deduction
    else:
        return 0
