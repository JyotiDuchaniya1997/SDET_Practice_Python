list1=[3,5,6,4,2,1]
list2=[1,299,8,0,6]
common=[]
for i in list1:
    if i in list2:
        common.append(i)

print(f"Common elements in array i.e. {list1} and second array i.e. {list2} are {common}")