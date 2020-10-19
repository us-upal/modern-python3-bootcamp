class Animal:
    cool = True # here cool is class attribute

    def make_noise(self, sound):
        print(f"this animal says {sound}")


class Cat(Animal):
    pass


a = Cat()
a.make_noise("meao")
