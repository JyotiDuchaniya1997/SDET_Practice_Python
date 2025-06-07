arr1=[12,15,16,17,18,20,21]
original_arr1=arr1.copy()
print(arr1, original_arr1)
if original_arr1 == sorted(arr1):
    print('Array Is sorted')
else:
    print("array is not sorted")
