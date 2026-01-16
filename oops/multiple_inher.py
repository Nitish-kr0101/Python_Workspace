# Parent class 1
class Fly:
    def fly_ability(self):
        print("This animal can fly")

# Parent class 2
class Swim:
    def swim_ability(self):
        print("This animal can swim")

# Child class (Multiple Inheritance)
class Duck(Fly, Swim):
    def quack(self):
        print("The duck says quack!")

# Create instance
donald = Duck()
donald.fly_ability()
donald.swim_ability()
donald.quack()
