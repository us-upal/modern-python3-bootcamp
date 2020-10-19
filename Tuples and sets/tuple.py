# number=(1,2,3,4,5) #tuples
# print(number)
# for i in number:
#     print(i)
# #sets===
# s={1,2,3,3.0,33/11,5}
# print(s) 
# for i in s:
#     print(i)
# #gets all unique values:
# ss=[1,2,33,2,3,1,3,2,3]
# ss=set(ss)
# print(ss)
# #set methods
# numbers={1,2,3}
# numbers.add(4)
# numbers.remove(1)
# n=numbers.copy()
# print(n)
# print(numbers)
#math notation of sets
a={1,2,3} 
b={3,4,5}
print(b|a) #union
print(a & b) #intersection

#===============SET COMPREHENSION===============
#1
s1={i**2 for i in range(0,11)}
s2={i:i**2 for i in range(0,11)}
print(s1)
print(s2) #now its ordered and dict.

#2
str='ds0'
str1={i for i in str if i in 'aeiou'}
print(str1)
 
