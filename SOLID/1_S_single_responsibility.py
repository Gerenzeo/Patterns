# Single Responsibility Principle (SRP)

# The Single Responsibility Principle (SRP) states that a class should have only one reason to change. 
# This means that a class should have only one responsibility or function within the system. 
# If a class is responsible for multiple things, it becomes harder to maintain and more prone to bugs. 
# By following SRP, we ensure that each class focuses on a single task, making the code more modular, 
# easier to understand, and simpler to test.


# Violation Principle 
class Car:
    def __init__(self, brand, model, color, year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
        self.is_running = False
    
    def start_engine(self):
        self.is_running = True

    def stop_engine(self):
        self.is_running = False
    

# No Violations Principle

class Engine:
    def __init__(self):
        self.is_running = False

    def start_engine(self):
        self.is_running = True

    def stop_engine(self):
        self.is_running = False

class Car:
    def __init__(self, brand, model, color, year):
        self.brand = brand
        self.model = model
        self.color = color
        self.year = year
        self.engine = Engine()
