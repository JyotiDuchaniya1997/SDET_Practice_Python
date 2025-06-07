seq=[1,2,5,6,7,8,11,13,4,23,19]
seq.sort()
miss=[]
for i in range(1,len(seq)):
    if seq[i] == seq[i-1]+1:
        pass
    else:
        start= seq[i-1]
        end= seq[i]
        while(start< end-1):
            miss.append(start+1)
            start+=1
print(f"Missing elements are {miss}")
