class Pet:
    def __init__(self, name)
        self.name = name

class Dog(Pet):
    def __init__(self, name, breed = None)  
        super().__init__(name)
        self.breed = breed  

    def say(self)
        return "{0}: waw".format(self.name)

 dog = Dog("aaa", "bbb")      