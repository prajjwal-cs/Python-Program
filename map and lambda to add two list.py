lst=[0,1,2]
lst1=[100,200,300]
n=[]
t=list(map(lambda x:list(map(lambda y:n.append(x+y),lst1)),lst))
print(n)
