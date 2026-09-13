#Remove duplicate value
num=[12,4,5,3,4,6,7,6,5,6,5,6,6]
un=[]
for i in num:
    if i not in un:
        un.append(i)
        print("output list=",un)