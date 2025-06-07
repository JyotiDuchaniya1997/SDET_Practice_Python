num = 5437283
num1=num
digit_sum=0
while(num1>0):
    r= num1%10
    num1=num1//10
    digit_sum+=r

print(f"the digits sum of {num} is {digit_sum}")