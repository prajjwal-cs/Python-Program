
def letter(s):
     upper=0
     lower=0
     for i in range(len(s)):
           if (ord(s[i])>=97 and ord(s[i])<=122):
                lower+=1
           elif (ord(s[i])>=65 and ord(s[i])<=90):
                 upper+=1
     print("No. of lowerCase letter:")
     print(lower)
     print("No. of uppercase letters :")
     print(upper)
    
a="The quick Brow Fox"
letter(a)
