def even(x):
    if x%2==0:
        return True
    else:
        False
lst=[2,3,4,5,7,8,99]
list1=list(filter(even,lst))
print(list1)
