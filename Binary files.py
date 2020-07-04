#program to create a binary file and store few data
x=20
with open("yt1.txt",'wb') as f:
    n=int(input("Enter no. cities to be stored"))
    for i in range(n):
        c=input("Enter the name of city")
        ln=len(c)
        c=c+(x-ln)*" "
        c=c.encode()
        f.write(c)

