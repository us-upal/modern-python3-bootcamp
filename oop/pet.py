class Pet:
    allowed_color = ["white", "blue", "red", "almond"]

    def __init__(self,name,color):
        if color not in Pet.allowed_color:
            raise ValueError(f"you can't allowed to choose {color} color")

        self.name = name
        self.color = color

    def set_color(self,color):
        if color not in Pet.allowed_color:
            raise ValueError(f"you can't allowed to choose {color} color")
        self.color = color


cat = Pet("Bonku","blue")
dog = Pet("bull", "white")
print(dog.set_color("green")) # ValueError: you can't allowed to choose green color
