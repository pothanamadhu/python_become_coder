n=int(input())
data=list(map(str,input().split()))
data1=[]
for i in data:
      k=0
      l=[]
      p=[]
      for j in i:
            if j.isdigit():
                  k=k+int(j)
            else:
                  l.append(j)
      p.append(k)
      p.append("".join(l))
      data1.append(p)
print(data1)

