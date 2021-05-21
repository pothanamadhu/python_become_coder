t=2
def lcm(a,b):#16 24
      global t
      if a%b==0 or b%a==0:
            if a>b:
                  return a
            else:
                  return b
      if t>=a or t>=b:
            return a*b
      if a%t==0 and b%t==0:
            return t*lcm(a//t,b//t)#2*2*2*lcm(2,3)
      else:
            t=t+1
            return t*lcm(a//t,b//t)#3*lcum(1,2)
a,b=map(int,input().split())
t=lcm(a,b)
print(t)
