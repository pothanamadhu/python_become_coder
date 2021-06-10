def fun(n,data,p,j):
      for i in range(j,n):
            if p<data[i]:
                  return False
      return True
def leadersofthelist(n,data):
      k=[]
      for i in range(n):
            if fun(n,data,data[i],i):
                  k.append(data[i])
      return k
n=int(input())
data=list(map(int,input().split()))
g=leadersofthelist(n,data)
print(*g)
