#Using inbuilt functions
list1=[1,7,3,4,1,9,56]
list1.sort()
print(list1[-1])

# not using inbuilt functions]
list2= [65,8,4,2,80,8,5,56]
maximum= list2[0]
for i in range(1, len(list1)):
    if list2[i] > maximum:
        maximum= list2[i]
print("Maximum number in list 2: ", list2, "is : ", maximum)