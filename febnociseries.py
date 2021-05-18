def gen_fib(n):
      a,b,c=0,1,0
      i=j=0
      if n==0 or n==1:
            return True
      while True:
            c=a+b#13
            if  c==n and c<n:
                  print(True)
            elif c>n:#13>10
                  i=n-b#
                  j=c-n#
                  if i<j:
                        print(b)
                        return
                  elif j<i:
                        print(c)
                        return
                  else:
                        print(b,c)
                        return
            a=b#5
            b=c#8
n=int(input())
gen_fib(n)
