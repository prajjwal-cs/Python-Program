'''
seek(offset,fromwhere)
offset-----> how many bytes to move
fromwhere---->from which position to move
0---> from begining
1---> from current position
2--->last position EOF

'''
f=open("yt1.txt",'w+')
print("Enter text (@ at end) ")
print(f.tell())
while str!='@':
    str=input()
    if(str!='@'):
        f.write(str + "\n")
print(f.tell())

f.seek(0,0)
str=f.read()
print(str)
f.close()