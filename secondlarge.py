def second_lar(n,data):
      k=0
      d=0
      for i in data:
            if i>k:
                  l=k
                  k=i
      return l
                  
n=int(input())
data=list(map(int,input().split()))
print(second_lar(n,data))
