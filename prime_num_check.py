num1=11
factors=0
for i in range(1,num1+1):
    if( num1%i ==0):
        factors+=1
    if(factors>2):
        print("Not a prime number")
        break
if(factors==2):
    print("prime number")
