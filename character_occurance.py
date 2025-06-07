str1="hjsgducgihebibbcewncaaaaa"
occurance={}

for ch in str1:
    if ch in occurance:
        occurance[ch]+=1
    else:
        occurance[ch]=1

print("The character occurance is as below:\n")
for key,value in occurance.items():
    print(f"{key} : {value}\n")