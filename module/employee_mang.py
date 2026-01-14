

import logging
from employee_utility.salary_calculator import calculate_final_salary

logging.basicConfig(level=logging.INFO)

basic_salary = float(input("Enter Basic Salary: "))
designation = input("Enter Designation (coder/designer/manager): ")
leaves_taken = int(input("Enter Leaves Taken: "))

logging.info("Starting final salary calculation")

final_salary = calculate_final_salary(basic_salary, designation, leaves_taken)

print("Final Salary:", final_salary)

logging.info("Salary calculation completed successfully")
