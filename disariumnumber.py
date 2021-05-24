def isdisarium(n):
      s=0
      i=1
      while n:
            r=n%10
            n=n//10
            s=s+(r**i)
            i=i+1
      return s
n=int(input())
t=n
s=0
while n:
      r=n%10
      n=n//10
      s=s*10+r
print(t==isdisarium(s))
