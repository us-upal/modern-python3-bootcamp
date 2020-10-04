a=[[1,2,3],[3,4,5],[6,7,8]]
print(a[2][-1])
#iteraring in nested list through nested for loop
for i in a: #i will get list item
    for j in i: # j will get nested list item 
        print(j)

#=======BOARD EXAMPLE=========
board=[num for num in range(1,4) for val in range(1,4)]
b2=[[num for num in range(1,4)] for num2 in range(1,5)]
b3=[['one' if i==1 else '*' for i in range(1,4)] for j in range(1,5)]

print(board)
print(b2)
print(b3)