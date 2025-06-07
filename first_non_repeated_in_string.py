str="abcjejkhndasbced"
str_occur={}
for ch in str:
    if ch in str_occur:
        str_occur[ch]+=1
    else:
        str_occur[ch]=1
for ch in str:
    if str_occur[ch]<2:
        print(f"First Non repeated character is string is {ch}")
        break