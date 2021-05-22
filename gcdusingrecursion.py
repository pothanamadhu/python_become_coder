def gcd(a,b):
      if a>b:
                  a,b=b,a
      if b%a==0:
            return a
      else:
            return gcd(a,b%a)
      
a,b=map(int,input().split())
print(gcd(a,b))
"""
while True:
            if a>b:
                  a,b=b,a
            if b%a==0:
                  return a
            else:
                  b=b%a
"""
            
