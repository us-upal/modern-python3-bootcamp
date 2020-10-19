class User:
    active_user = 2

    @classmethod
    def show_active_users(cls):
        print(f"there are currently {cls.active_user} users")

    @classmethod
    def str_formater(cls, str):
        fname, lname, age = str.split(",")
        return cls(fname, lname, age)

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


user1 = User("udyan", "saha", 24)
user2 = User("elon", "mask", 49)

print(User.show_active_users())  # there are currently 4 users
user1 = User("udyan", "saha", 24)
user2 = User("elon", "mask", 49)
print(User.show_active_users())  # there are currently 6 users
upal = User.str_formater("Udyan,upal,24")
print(upal.fname)
print(upal.lname)
print(upal.age)
print(user1)