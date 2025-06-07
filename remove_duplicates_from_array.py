# using inbuilt functions
my_array=[1,5,7,34,3,6,7,3,23,45,5]
print(f"Non duplicates array is {list(set(my_array))}")

# using non inbuilt functaions
my_array=[23,5,7,45,3,3,5,7,4,6,4]
uniques=[]
for i in my_array:
    if i in uniques:
        pass
    else:
        uniques.append(i)
print(f"Unique emelents of the array is {uniques}")