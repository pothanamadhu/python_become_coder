def original(n,data):
      t=[]
      for i in data:
            if i not in t:
                  t.append(i)
      return t
n=int(input())
data=list(map(int,input().split()))
d=original(n,data)
print(*d)
