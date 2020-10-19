# _name
# __name
#  __name__ (Dunder--> double underscore)
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age  # underscore here is for telling that it's use must be private rather than others.
        self.__uni = "north south University"


p1 = Person("Elon Mask", 49)
print(p1.name)
print(p1._age)
print(p1.__uni)
