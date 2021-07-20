n=int(input())
data=list(map(str,input().split()))
d={}
f=[]
for word in data:
      for i in range(len(word)):
            k=0
            for j in range(i,len(word)):
                  if word[j] not in d.keys():
                        d[word[j]]=1
                  else:
                        break
            if len(d)>k:
                  k=len(d)
                  d.clear()
      f.append(k)

                  
                  
            
