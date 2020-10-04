# a=[1,2,3]
# print(a)
# print(b)

# name='upal'
# print(name)
# name2=[char.upper( ) for char in name]
# print(name2)

num=[i*2 for i in range(0,11)]
print(num)
b=[bool(i) for i in [1,0,'',None]]
print(b)

evens=[i for i in range(0,11) if i%2==0]
print(evens)
odds=[i for i in range(0,11) if i%2 != 0]
print(odds)

a=[i*2 if i%2 !=0 else i*100 for i in range(0,11)] 
print(a)