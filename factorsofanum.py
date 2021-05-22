from math import *
j=2
k=2
def fac(n,s):#25 5
      global j,k
      if j>s:
            return k
      if n%j==0:
            if j==n//j:
                  k=k+1
                  j=j+1
                  return fac(n,s)
            k=k+2
            j=j+1
            return fac(n,s)
      j=j+1
      return fac(n,s)
n=int(input())
s=int(sqrt(n))
print(fac(n,s))
"""
      k=0
      for i in range(2,s+1):
            if n%i==0:
                  if i==n//i:
                        k=k+1
                  else:
                        k=k+2
      return k
"""
