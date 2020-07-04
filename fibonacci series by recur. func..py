def series(x):
    if x<=1:
        return x
    else:
        return(series(x-1)+series(x-2))

for i in range(1,10):
    print(series(i))


    
