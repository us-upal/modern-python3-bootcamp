class User:
    active_user = 2

    def __init__(self, fname, lname, age):
        self.fname = fname  # Self keywords refers to the current instance of the class
        self.lname = lname
        self.age = age
        User.active_user += 1

    def logged_in(self):
        User.active_user += 1
        return f"{self.fname} logged in successfully"

    def logged_out(self):
        User.active_user -= 1
        return f"{self.fname} just logged out"

    def full_name(self):
        return f"{self.fname} {self.lname}"

    def name_initials(self):
        return f"{self.fname[0]}.{self.lname[0]}."

    def alma_mater(self, uni):
        return f"{self.fname} studied @ {uni}"

    @property
    def is_voter(self):
        return self.age >= 18


print(User.active_user) # 2
user1 = User("udyan", "saha", 24)
user2 = User("elon", "mask", 49)
print(User.active_user) # 4
print(user2.logged_out()) # elon just logged out
print(User.active_user) # 3
print(user1.logged_in()) # udyan just logged in
print(User.active_user) # 4






# user1 = User("udyan", "saha", 24)
# user2 = User("elon", "mask", 49)
# print(user2.full_name())  # elon mask
# print(user1.name_initials())  # u.s.
# print(user2.name_initials())  # e.m.
# print(user1.alma_mater("north south university"))  # udyan studied @ north south university
# print(user1.is_voter())


