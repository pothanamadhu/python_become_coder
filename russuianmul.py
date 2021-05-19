a,b=map(int,input().split())
s=0
while True:
      if a%2:
            s=s+b
      if a==0:
            break
      a=a//2
      b=b*2
print(s)
