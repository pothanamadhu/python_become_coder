def gen_fib(n):
      a,b,c=0,1,0
      if n==0 or n==1:
            return True
      f=2
      while True:
            c=a+b#1 2 3 5
            a=b#1 1 2 3
            b=c#1 2 3 5
            f=f+1#3 4 5
            if  c==n:
                  print(f)
                  break
            if c>n:#
                   print(False)
                   break
n=int(input())
gen_fib(n)
