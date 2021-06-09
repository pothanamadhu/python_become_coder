def movezeros(n,data):
      c=data.count(0)
      for i in range(c):
            data.remove(0)
            data.append(0)          
n=int(input())
data=list(map(int,input().split()))
movezeros(n,data)
print(*data)
