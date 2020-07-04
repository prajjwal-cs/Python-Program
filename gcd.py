#prajjwal pachauri

def gcd(x,y):
      rem=x%y
      if(rem==0):
          return y
      else:
          return gcd(y,rem)
print(gcd(20,40))        
