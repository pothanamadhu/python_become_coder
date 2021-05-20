def perfect(n):
      s=0
      for i in range(1,n):
            if n%i==0:
                  s=s+i
      return s
n=int(input())
if perfect(n)==n:
      print("perfect number")
else:
      print("not a perfect number")
