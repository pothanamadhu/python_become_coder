def original(n,data):
      t=list(set(data))
      return t
n=int(input())
k=0
data=list(map(int,input().split()))
d=original(n,data)
print(*d)
for i in range(len(d)):
      if data[i]==d[i]:
            k=k+1
print(k)
