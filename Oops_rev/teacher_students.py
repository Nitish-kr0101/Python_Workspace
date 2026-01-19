class Student:
    def __init__(self, id, name, total_marks):
        self.id = id
        self.name = name
        self.total_marks = total_marks
        self.division = self.get_division()

    def get_division(self):
        if self.total_marks >= 60:
            return "1st Division"
        elif 45 <= self.total_marks < 60:
            return "2nd Division"
        elif 35 <= self.total_marks < 45:
            return "3rd Division"
        else:
            return "Fail"


class Teacher:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.students = []

    def add_student(self, student):
        if student.total_marks < 20:
            print(f"Sorry cant be added {student.name}, marks less than 20")
        else:
            self.students.append(student)

    def total_strength(self):
        return len(self.students)

    def count_distinction(self):
        return sum(1 for s in self.students if s.total_marks >= 75)

    def get_students_desc_with_marks(self):
        students_list = [(s.name, s.total_marks) for s in self.students]
        students_list.sort(reverse=True)
        return students_list


s1 = Student(101, "A", 80)
s2 = Student(102, "B", 65)
s3 = Student(103, "C", 45)
s4 = Student(104, "D", 72)
s5 = Student(105, "E", 90)
s6 = Student(106, "F", 70)

t1 = Teacher(1, "Mr. Smith")

for s in [s1, s2, s3, s4, s5, s6]:
    t1.add_student(s)

print("Students (Name , Marks):")
for name, marks in t1.get_students_desc_with_marks():
    print(name, "-", marks)

