def rev(n):
      s=0
      while(n):
            r=n%10
            n=n//10
            s=s*10+r
      return s
def maxer(n,data):
      s=max(data)
      print(s)
      r=rev(s)
      for i in range(len(data)):
            if data[i]==s:
                  data[i]=r
      k=max(data)
      print(k)
      return r==k
                  
n=int(input())
data=list(map(int,input().split()))
d=maxer(n,data)
print(d)
