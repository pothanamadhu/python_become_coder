s=0
def rev(n):
      global s
      r=n%10
      if n==0:
            return s
      s=s*10+r
      return rev(n//10)
n=int(input())
p=rev(n)
print(p)
