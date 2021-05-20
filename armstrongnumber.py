def count(n):
      c=0
      while n:
            n=n//10
            c=c+1
      return c
def arstrng(n,c):
      s=0
      while n:
            r=n%10
            n=n//10
            s=s+pow(r,c)
      return s
n=int(input())
c=count(n)
a=arstrng(n,c)
if n==a:
      print(True)
else:
      print(False)
