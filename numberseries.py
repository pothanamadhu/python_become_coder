def seq(a):
      while a:#6
            print(a,end=" ")#6
            if a%2==0:
                  a=a//2#3
            else:
                  a=3*a+1
            if a==1:
                  print("1")
                  break
a=int(input())
seq(a)
