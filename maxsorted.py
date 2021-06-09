def maxsort(n,data):#1 2 3 1 4 1 2 3 4 6
      f=s=0
      for i in range(n-1):
            if data[i]<data[i+1]:
                  f=f+1
            else:
                  if f+1>s:
                        s=f+1
                  f=0
      if f+1>s:
            return f+1
      return s
n=int(input())
data=list(map(int,input().split()))
q=maxsort(n,data)
print(q)
