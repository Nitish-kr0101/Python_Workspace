class Phone:

    def __init__(self, brand, color, model):
        self.brand = brand      # Attribute
        self.color = color      # Attribute
        self.model = model      # Attribute

    def call(self, number):
        print(f"The {self.color} {self.brand} {self.model} is calling {number}!")

# Creating an instance of Phone
my_phone = Phone("Apple", "Black", "iPhone 14")

# Accessing attributes
print(my_phone.brand)
print(my_phone.color)
print(my_phone.model)

# Calling the method
my_phone.call("123-456-7890")
