list1=[23,45,76,345,23,45,"sdf",34,"6745","dfsag"]
even_index=[]
odd_index=[]
for i in list1:
    if(list1.index(i)%2==0):
        even_index.append(i)
    else:
        odd_index.append(i)
print(f"Original List: {list1} \n Even index list: {even_index} \n odd index list: {odd_index}")