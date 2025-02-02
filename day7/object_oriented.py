# object = A "bundle" of relate attributes (variables) and methods (functions)
#          Ex. phone, cup, book
#          You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

from car import Car
        
car1 = Car("Dodge", 1969, "black", False)
car2 = Car("Corvette", 2025, "yellow", True)
car3 = Car("Mustang", 2020, "red", True)

# car1.drive()
# car1.stop()
car1.describe()