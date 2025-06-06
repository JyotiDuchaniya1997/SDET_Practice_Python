num1=4
num2=5
#using third variable
num3=num1
num1=num2
num2=num3
print("num1= ",num1," and num2 is ", num2)

# without using third variable
num1=num1+num2
num2= num1-num2
num1=num1-num2
print("num1= ",num1," and num2 is ", num2)

#usaing xor
num1=num1^num2
num2=num1^num2
num1=num1^num2
print("num1= ",num1," and num2 is ", num2)