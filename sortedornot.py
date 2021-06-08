def is_sorted(n,data):
      k=m=0
      for i in range(n-1):
            if data[i]>data[i+1]:
                  k=k+1
            elif data[i]<data[i+1]:
                  m=m+1
      if m==n-1 or k==n-1:
            return True
      else:
            return False
n=int(input())
data=list(map(int,input().split()))
print(is_sorted(n,data))
