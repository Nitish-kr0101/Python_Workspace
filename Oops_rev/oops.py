class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display(self):
        print("The employee details are", self.name, self.emp_id)


emp1 = Employee("JC", 101)
emp2 = Employee("KC", 100)
emp3 = Employee("VC", 101)

emp = [emp1, emp2, emp3]

new_emp = Employee("KK", 101)

exists = False
for e in emp:
    if e.emp_id == new_emp.emp_id:
        exists = True
        break

if not exists:
    emp.append(new_emp)
else:
    print("Employee ID already exists")

for e in emp:
    e.display()

#dictionary
emp_dict = {}

for e in [emp1, emp2, emp3]:
    if e.emp_id not in emp_dict:
        emp_dict[e.emp_id] = e
    else:
        print(f"Duplicate ID found in dictionary: {e.emp_id}, not adding {e.name}")

if new_emp.emp_id not in emp_dict:
    emp_dict[new_emp.emp_id] = new_emp
else:
    print(f"Employee ID {new_emp.emp_id} already exists in dictionary, not adding {new_emp.name}")

print("\nEmployees in dictionary:")
for e in emp_dict.values():
    e.display()

