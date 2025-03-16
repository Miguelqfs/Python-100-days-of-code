# Just testing python OOP inheritance.

class Animal:
    def __init__(self):
        self.eyes = 2

    def breathe(self):
        print("inhale, exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("while underwater")

    def swim(self):
        print("moving underwater")

fish = Fish()
animal = Animal()

# Now you can test the inheritance by typing:
# fish.argument/method or animal.argument/method