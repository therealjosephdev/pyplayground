# Static methods = A method that belong to a class rather than any object from that class (instance)
#                  Usually used for general utility functions

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility function that do not need access to class data

class Employee:
    
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    def get_infO(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager" "Cashier", "Cook", "Janitor"]
        return position in valid_positions
    
employee1 = Employee("Eugune", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")
    
print(Employee.is_valid_position("Programmer"))
print(employee1.get_infO())
print(employee2.get_infO())
print(employee3.get_infO())