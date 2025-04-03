# Interface Segregation Principle (ISP)

# The Interface Segregation Principle (ISP) states:
# - Clients should not be forced to depend on interfaces they do not use.
# In other words, a class should not be required to implement methods it does not need. Instead, 
# large interfaces should be divided into smaller, more specialized ones.

# 💡 Key Idea:
# - It is better to create several small interfaces rather than one large interface that forces classes to implement unnecessary methods.
# - Classes should implement only the methods they actually need.
# - This makes the system more flexible, easier to maintain, and less prone to changes.

# ❌ Violation of ISP

from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

# Human can eat and work
class Human(Worker):
    def work(self):
        return "I am working!"
    
    def eat(self):
        return "I am eating!"

# Robot can work, but no eating
class Robot(Worker):
    def work(self):
        return "I am working!"
    
    def eat(self): # ❌  Robot dont need this method! But realisation is required! Its wrong!
        raise Exception("Robots do not eat!")

# ✅ Correct ISP Implementation

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    def eat(self):
        pass


class Human(Workable, Eatable):
    def work(self):
        return "I am working!"
    
    def eat(self):
        return "I am eating!"

class Robot(Workable):
    def work(self):
        return "I am working!"
    

def let_work(worker: Workable):
    return worker.work()

def let_eat(eater: Eatable):
    return eater.eat()

human = Human()
robot = Robot()

print(let_work(human)) # ✅ correct
print(let_work(robot)) # ✅ correct
print(let_eat(human))  # ✅ correct
print(let_eat(robot))  # ❌ dont have the method eat