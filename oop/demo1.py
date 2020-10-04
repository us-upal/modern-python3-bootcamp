class User:
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age
    def MyName(self,first,last):
        self.fname=first
        self.lname=last
        return  f'myname is {first} {last}'


        #print(f'My name is {ffname} {lfname} ')

user1 = User('upal','saha','45')
y=user1.MyName('udyan''saha','45')
print(y)
