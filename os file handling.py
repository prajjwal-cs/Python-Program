import os,sys
filename=input()
if os.path.isfile(filename):
    f=open(filename,'r')
else:
    print(filename + ' Does not exist')
    sys.exit()
str=f.read()
print(str)
f.close()        
