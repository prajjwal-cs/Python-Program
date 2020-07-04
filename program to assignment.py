def power(a,b):
    if b==1:
        return a
    elif(b!=1):
        return (a*power(a,b-1))
x=int(input("enter the value of a"))
y=int(input("enter the value of b"))
print(power(x,y))


a=[1,2,3,4,5,6]
def arr_sum(l,n):
    if n==0:
        return 0
    else:
        return (l(n-1) + arr_sum(l,n-1))
c=arr_sum(a, len(a))
print(c)

def harmonic_sum(n):
    if
    n<2:
        return 1
    else:
        return 1/n +harmonic_sum(n-1)
a=int(input("enter Limit :"))
print(harmonic_sum(a))

def capital_case(str, i):
    if (str[i]=='0'):
        return 0
    elif(str[i].isupper()):
        return str[i]
    else:
        return capital_case(str, i+1)
s=input("Enter a string :")
r=capital_case(s,0)
if(r==0):
    print("no upper case letter in given string")

else:
    print(r)


def bubble_sort(lst,n):
    for i in range(n-1):
        if lst[i+1]<lst[i]:
            lst[i],lst[i+1]=lst[i+1],lst[i]
    return bubble_sort(lst,n-1)
     
lst=[64,34,25,12,22,11,90]
n=len(lst)
l=bubble_sort(lst,n)
print(l)



def recaman(n):
    arr= [0]*n
    arr[0]=0
    print(arr[0], end=', ')
    for i in range(1,n):
        c=arr[i-1]-1

        for j in range(0,i):
            if((arr[j]==c) or c<0):
                c=arr[i-1]+i
                break
        arr[i]= c
        print(arr[i], end=', ')
n=17
recaman(n)
