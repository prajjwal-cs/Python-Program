f=open("2 table.txt",'w+')
a=1
for i  in range(1,11):
     a=2*i
     b=str(a)
     f.write(b + '\n')
f.seek(0,0)
s=f.read()     
print(s)
f.close()     