my_array1=[23,34,6,76,34,2]
original_my_array=my_array1.copy()
print(my_array1)
#without using inbuilt functions
start=0
end=len(my_array1)-1
while(start<end):
    my_array1[start], my_array1[end] = my_array1[end], my_array1[start]  # Pythonic swap
    start+=1
    end-=1
print(f"Reversed array for original list i.e {original_my_array} is {my_array1}")

#using inbuilt functaions
print(f"Reversed array using indexing is {original_my_array[::-1]}")

original_my_array.reverse()
print(f"Reversed array is {original_my_array}")