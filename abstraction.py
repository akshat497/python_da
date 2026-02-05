from abc import ABC,abstractmethod

class animal(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def sound(self):
        pass
    
class dog(animal):
    def sound(self):
        print("bark")
        
class cat(animal):
    def sound(self):
        print("meow")
        
        
a=cat()
b=animal()
a.sound()