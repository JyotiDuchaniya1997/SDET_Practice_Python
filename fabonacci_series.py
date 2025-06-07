class fabonacci:
    series_len=int(input("Enter the length of desired series: "))
    series=[]
    if(series_len ==0): print("No series as length provided is 0")
    elif(series_len==1): 
        series=[0] 
        print(f"Series is : {series}")
    else:
        series= [0, 1]
        for i in range(2, series_len):
            series.append(series[i-1]+ series[i-2])
        print(f"Fabonnaci Series of length- {series_len} is {series}")