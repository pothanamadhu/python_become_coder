c=0
def count(n):
      global c
      if n==0:
            return c
      c=c+1
      return count(n//10)
s=0
def arstrng(n,c):
      global s
      if n==0:
            return s
      r=n%10
      s=s+pow(r,c)
      return arstrng(n//10,c)
n=int(input())
c=count(n)
a=arstrng(n,c)
if n==a:
      print(True)
else:
      print(False)
