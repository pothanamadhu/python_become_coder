n=int(input())
data=list(map(int,input().split()))
s1=1
s2=2
k=0
s=0
for i in range(n):
      k=k+1
      if data[i]==1 or data[i]==3:
            s1,s2=s2,s1
      elif data[i]==-1:
            print(s1,"out")
            s1=max(s1,s2)+1
      if k%6==0:
            print("over-up")
            s1,s2=s2,s1
      print("striker:",s1,"non-striker",s2)
print(s1)
      
            
      
