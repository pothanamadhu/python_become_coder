def perfect(n):
      p=0
      for i in range(1,n):#
            if n%i==0:
                  p=p+i
      return p
n=int(input())
p=perfect(n)
if n==p:
      print("perfect")
else:
      print("not perfect")














"""
def count(n):
      c=0
      while n:
            n=n//10
            c=c+1
      return c
def am(n,c):#1,1
      s=0
      while n:
            r=n%10
            n=n//10
            s=s+r**c
      return s
n=int(input())#4
for i in range(n+1):#20
      c=count(i)
      if i==am(i,c):#1==am(1,1)
            print(i)#0
"""
            
