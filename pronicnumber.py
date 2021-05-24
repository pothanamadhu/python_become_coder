import math as m
def pronic(n):
      s=int(m.sqrt(n))
      if s*(s+1)==n:
            return True
      return False
n=int(input())
print(pronic(n))
"""
def pronic(n):
      for i in range(1,n//2+1):
            print(i)
            if i*(i+1)==n:
                  return True
      return False
n=int(input())
print(pronic(n))
"""
