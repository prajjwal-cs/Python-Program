f=open("yt.txt",'w')
while  str!='@':
    str=input()
    f.write(str + '\n\
f.close()

f=open("yt.txt",'r')
print(f.read())
f.close()
