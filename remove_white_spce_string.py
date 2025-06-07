str="hello there mate"
str_list_without_space= str.split(" ")
result=""
for word in str_list_without_space:
    result= result+ word
print(f"Without spaces is : {result}")