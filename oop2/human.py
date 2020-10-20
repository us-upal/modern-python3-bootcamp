class Human:
    def __init__(self, f, l, a):
        self.l = l
        self.f = f
        self.a = a
        if a > 0:
            self._a = a
        else:
            self._a = 0

    def get_age(self):
        return self._a

    def set_age(self, new_age):
        if new_age > 0:
            self._a = new_age
        else:
            self._a = 0


upal = Human("udyan", "upal", -24)
print(upal.get_age())
upal.set_age(25)
print(upal.get_age())