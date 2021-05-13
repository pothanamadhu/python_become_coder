n=int(input())
temp=n
s=c=0
while n:
      n=n//10
      c=c+1
c=k=c-1
n=temp
p=n//(10**c)
q=n%10
while n:#234
      r=n%10#1 2
      n=n//10#234 34
      if c==k:
            r=p
      elif c==0:
            r=q
      s=s*10+r#1
      c-=1#2
print(s)
