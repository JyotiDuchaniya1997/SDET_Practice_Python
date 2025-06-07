my_array=[2,4,1,3,5,2,3,1,23]
occur={}
for i in my_array:
    if i in occur:
        occur[i]+=1
    else:
        occur[i]=1
print("duplicate items are: ")
for key in occur:
    if occur[key]>=2:
        print(key)