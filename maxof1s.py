def maxof1(n,data):
      c=0
      count=0
      for i in range(n):
            if data[i]==1:
                  c=c+1
            else:
                  if c>count:
                        count=c
                  c=0
      return max(c,count)
n=int(input())
data=list(map(int,input().split()))
q=maxof1(n,data)
print(q)
