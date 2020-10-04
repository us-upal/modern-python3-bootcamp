# a=[1,2,'u','upal',1.78,False,None]
# # for i in range(len(a)):
# #     print(a[i])
# print(a[-1])
# print(a[6])

# print(1 in a)
# for i in a:
#     print(i) #python list accessing is mind blowing

# l=[0,1,2,3,4,9]
# l.append('upal') #appned() passes only one argument both item and list
# l.extend(['one','two','three']) #TypeError: extend() takes exactly
# l.insert(-1,'proman dao')
# #intering item in the last
# l.insert(len(l),'proman dao')
# print(l)
# a=[1,2,3,4,5]
# print(a)
# #a.pop(-1 )#argument is item index
# # a.remove(4) #arument is direct item rather than index
# # a.clear()
# a.index(1) #argument is item directly rather than index
# aa=a.index(3,0,4)
# a3=a.count(5)
# a.reverse()
# print(a)
# a.sort() #sort in accending order
# print(a) 
# name=["saha ", 'upal']
# fruit=['banana','mango','orange','grape']
# fruit2=','.join(fruit)
# print(fruit2) #o/p: banana,mango,orange,grape
# print('udyan '.join(name)) #o/p:saha udyan upal

#============SLICING==================
l=[0,1,2,3,4,5,6,7,8,9,10]
#list[start:end:step]|| 'end' is exclusive # ***remember that is ':' (colon)
print(l[0:9:2])  #[0, 2, 4, 6, 8]
print(l[::-1])
print(l[10:0:-1])
#============SLICING==================

#============SWAPING==================
names=["udyan",'upal']
names[0],names[1]=names[1],names[0]
print(names)

# for i in l:
#     print(f"l[{i}]")
