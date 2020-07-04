lst=[0,1,2]
lst1=[100,200,300]
print(list(map(sum,[(x,y) for x in lst for y in lst1])))
    
