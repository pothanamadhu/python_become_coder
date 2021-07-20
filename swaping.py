n=int(input())
data=list(map(int,input().split()))
k=1
while True:
      swaps=0
      for i in range(n-1):
            if data[i]>data[i+1]:
                  data[i],data[i+1]=data[i+1],data[i]
                  swaps+=1
      n=n-1
      if swaps==0:
            break
      print("pass[",k,"]=",*data)
      k=k+1
