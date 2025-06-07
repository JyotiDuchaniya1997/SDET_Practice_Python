str1="gfshjjh5j456234nbb2345gh1g345"
num=""
for i in str1:
    if i.isnumeric():
        num+=i
print(f"Extracted Numbers from string  is : {num}") 