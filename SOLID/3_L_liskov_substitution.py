# Liskov Substitution Principle (LSP)

# The Liskov Substitution Principle (LSP) states that subtypes must be substitutable for their base types
# without altering the correctness of the program.
# In other words, if class B is a subclass of class A, 
# we should be able to replace A with B without breaking the program.

# 💡 Key Idea:
# - A subclass should extend the behavior of a parent class without changing its meaning.
# - If replacing a parent class with a child class causes unexpected behavior or errors, then LSP is violated.

# ❌ Violation Principle 
class Bird:
    def fly(self):
        return "I can fly"

class Sparrow(Bird):
    pass 

class Penguin(Bird):
    def fly(self): # ❌ This is incorrect because penguins can't fly
        raise Exception("Penguins cannot fly!")

def make_bird_fly(bird: Bird):
    return bird.fly()

sparrow = Sparrow()
# print(make_bird_fly(sparrow)) # correct

penguin = Penguin()
# print(make_bird_fly(penguin)) # Throws an Exception

# ✅ Correct LSP Implementation

# Base class for all birds
from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class FlyingBird(Bird):
    @abstractmethod
    def fly(self):
        pass

class Sparrow(FlyingBird):
    def fly(self):
        return "I can fly!"

    def make_sound(self):
        return "Chirp chirp!"

class Penguin(Bird):
    def make_sound(self):
        return "Honk honk!"

def make_bird_fly(bird: FlyingBird):
    return bird.fly()

sparrow = Sparrow()
print(make_bird_fly(sparrow)) # ✅ Works fine

penguin = Penguin()
print(make_bird_fly(penguin)) # ❌ Won't work because Penguin is not a FlyingBird
