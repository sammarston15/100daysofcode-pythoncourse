# *args is equal to Unlimited Python Arguments
def add(*args):
    sum = 0
    for n in args:
        sum =+ n


add(3, 5, 9)


# **kwargs is equal to unlimited keyword arguments
def calculate(n, **kwargs):
    # print(kwargs)
    # print(kwargs["add"])
    n += kwargs["add"]
    n += kwargs["multiply"]

calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model") # .get looks for the keyword but doesn't break the code if it is not found


my_car = Car(make="Ford", model="F150")
print(my_car)