arr= [2,3,1,4,5,25,6,4]
arr1= [2,3,1,4,5,25,6,4]

for i in range(0, len(arr)):
    for j in range(i, len(arr)):
        if(arr[j]<arr[i]):
            arr[i],arr[j]=arr[j],arr[i]
        if(arr1[j]> arr1[i]):
            arr1[i],arr1[j]=arr1[j],arr1[i]

print(f"Sorted array in ascending is {arr}")
print(f"Sorted array in descending is {arr1}")