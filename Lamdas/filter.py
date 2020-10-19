nums=[0,1,2,3,4,5,6,7,8,9,10]

odds=filter(lambda i:i %2 !=0,nums)
print(list(odds))

#combining filter and map:
names=['udyan', 'saha' , 'upal']
show=list(map(lambda name :f'my name is {names}',filter(lambda value :len(value)<5,names)))
print(show)
a=[f'my name is {names}' for i in names if len(i)==5]
print(a)