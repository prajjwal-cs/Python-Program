f=open("yt1.txt",'w')
print("Enter text (@ at end) ")
while str!='@':
    str=input()
    if(str!='@'):
        f.write(str + "\n")
f.close()        
f=open("yt1.txt",'r')
str=f.read()
print(str)
f.close()