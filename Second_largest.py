my_array=[32,43,5,43,2,4,7,6]
large=my_array[0]
sec_large=my_array[1]
for i in my_array:
    if large< i:
        sec_large=large
        large=i
    if sec_large <i and i!=large:
        sec_large=i
print(f"List is {my_array} and largest num is {large} and second largest is {sec_large}")