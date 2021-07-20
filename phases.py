n=int(input())
data=list(map(int,input().split()))#11 32 44 77 33 88 55
data1=data.copy()#11 32 44 77 33 55    88
k=n-1
for i in range(n-1):
      m=max(data1)#88
      data1.remove(m)
      ind=data.index(m)#5
      l=data[k]#55
      data[k]=m
      data[ind]=l
      k=k-1
      print("p#",i+1,"="*data)
      
                  
            
      
