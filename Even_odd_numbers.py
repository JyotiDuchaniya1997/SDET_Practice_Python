list1=[2,3,43,6,4,2,4,6,465,67]
even=0
odd=0
for i in list1:
    if i%2==0: even+=1
    else: odd+=1
print(f"List is - {list1} with even count as {even} and odd as {odd}")