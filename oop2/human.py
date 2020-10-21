class Human:
    def __init__(self, f, l, a):
        self.l = l
        self.f = f
        # self.a = a
        if a > 0:
            self._a = a
        else:
            self._a = 0

    def get_age(self):
        return self._a

    # def set_age(self, new_age):
    #     if new_age > 0:
    #         self._a = new_age
    #     else:
    #         self._a = 0

    @property  # it makes method like a attribute
    def age(self):
        return self._a

    @age.setter
    def age(self,new_age):
        if new_age >= 0:
            self._a = new_age
        else:
            raise ValueError("age is -ve")

    @property
    def full_name(self):
        return f"{self.f} {self.l}"

    @full_name.setter
    def full_name(self, name):
        self.f, self.l = name.split(" ")


upal = Human("udyan", "upal", -24)
# print(upal.get_age())
# upal.set_age(25)
# print(upal.get_age())
upal.age = 34    # this is also acts attribute.
print(upal.age)  # here age is a method but because of '@property' we can use it like a attribute. NO NEED OF ()
upal.full_name = "elon mask"
print(upal.f)    # elon
print(upal.l)    # mask
print(upal.__dict__)

