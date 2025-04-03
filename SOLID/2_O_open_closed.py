# Open/Closed Principle (OCP)

# The Open/Closed Principle (OCP) states that software entities (such as classes, modules, and 
# functions) should be open for extension but closed for modification.
# This means that we should be able to add new functionality without modifying existing code. This
# helps prevent unintended bugs and makes the system more maintainable. 
# 💡 Key Idea: Instead of changing an existing class when adding new features, we should extend it
# (e.g., using inheritance or polymorphism).

# ❌ Violation Principle 

def get_animal_sound(animal):
    if animal.name == "lion":
        return "roar"
    if animal.name == "cat":
        return "meow"
    # If we add a new animal (e.g., dog), we must modify this function. This breaks OCP.


# ✅ Correct OCP Implementation
class Animal:    
    def make_sound(self):
        raise NotImplementedError("Subclasses must implement make_sound()")
    
class Lion(Animal):
    def make_sound(self):
        return "roar"
    
class Cat(Animal):
    def make_sound(self):
        return "meow"
    
class Dog(Animal):
    def make_sound(self):
        return "bark"
    
animals = [Lion(), Cat(), Dog()]

def get_animal_sound(animals: list):
    return "\n".join(animal.make_sound() for animal in animals)

sounds = get_animal_sound(animals)
print(sounds)