def maxsort(n,data):#1 2 3 1 4 1 2 3 4 6
      f=w=0
      for i in range(n-1):
            if data[i]<data[i+1]:
                  pass
            else:
                  w=w+1
      return w+1
n=int(input())
data=list(map(int,input().split()))
q=maxsort(n,data)
print(q)
