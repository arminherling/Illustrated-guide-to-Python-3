# Exercise: Create a class to represent a cat. What can a cat do? What are the properties of a cat?
# Create a subclass of a cat for a tiger. How does it behave differently?

class Cat:
    
    def __init__(self, size):
        self._size = size
        self._growl = "Meow"


    def size(self):
        return size

    
    def growl(self):
        return self._growl




class Tiger(Cat):

    def __init__(self, size):
        self._size = size
        self._growl = "Rawr"




cat = Cat(6)
tiger = Tiger(12)

print(cat.growl())
print(tiger.growl())