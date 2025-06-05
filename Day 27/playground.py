# Learning about optional arguments (*args) and key word arguments (**kwargs)
# the type of *args is: Tuple
# the type of **kwargs is: Dict

def add(*args: int):
    print(args[1])

    soma = 0
    for n in args:
        soma += n
    print(soma)

add(10, 15, 20, 5)

def calculate(**kwargs):
    print(kwargs)
    print(type(kwargs))

    for key,value in kwargs.items():
        print(key)
        print(value)

calculate(add=3, multiply=5)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make") # Using .get so it don't crate any errors
        self.model = kwargs.get("model")
        self.colour = kwargs.get("colour")
        self.seats = kwargs.get("seats")

my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)
print(my_car.colour) # None (wasn't declared)