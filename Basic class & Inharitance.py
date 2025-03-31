class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("subclass must implamemt abstract metod")
    
class Dog(Animal):
    def speak(self):
        return "Raaa!"
    
dog = Dog("Buddy")
print(dog.speak())  # Raaa!