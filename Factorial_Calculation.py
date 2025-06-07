def factorial(num):
    if(num==1): return 1
    return num* factorial(num-1)

num1= int(input("Enter the number: "))
if(num1<=0):
    print('Invalid length hence no series to display')
else:
    print(f"The factorial of {num1} is {factorial(num1)}")