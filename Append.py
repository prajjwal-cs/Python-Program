f=open("yt.txt",'a+')
print("Enter text to append in file: ")
while str!='@':
      str=input()
      if str!='@'
          f.write(str+"\n")
f.seek(0,0)
str1=f.read()
print(str1)      
f.close()    