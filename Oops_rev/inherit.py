class Employee:
    def __init__(self,id,name,salary):
        self.__id = id
        self.__name = name
        self.__salary = salary  
    def get_id(self):
        return "The id is " ,self.__id
    def show_details(self):
        print("The employee details are ",self.__id,self.__name,self.__salary)

class Manager(Employee):
    def __init__(self,id,name,salary,no_of_team):
        super().__init__(id,name,salary)
        self.__no_of_team = no_of_team
    
emp = Employee(101,"JC",50000)
emp.show_details()
mgr = Manager(201,"KC",80000,5)
mgr.show_details()