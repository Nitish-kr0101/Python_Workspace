# Base class
class Phone:

    def __init__(self, brand, color, model):
        self.brand = brand
        self.color = color
        self.model = model

    def call(self, number):
        print(f"The {self.color} {self.brand} {self.model} is calling {number}!")

# Derived class inheriting from Phone
class SmartPhone(Phone):

    def __init__(self, brand, color, model, os):
        super().__init__(brand, color, model)  # Initialize attributes from Phone
        self.os = os  # New attribute specific to SmartPhone

    def browse(self, website):
        print(f"The {self.brand} {self.model} running {self.os} is browsing {website}.")

# Creating an instance of SmartPhone
my_smartphone = SmartPhone("Samsung", "Blue", "Galaxy S21", "Android")

# Accessing attributes and methods from both Phone and SmartPhone
print(my_smartphone.brand)
print(my_smartphone.color)
print(my_smartphone.model)
print(my_smartphone.os)

my_smartphone.call("987-654-3210")
my_smartphone.browse("www.smartphone.com")
