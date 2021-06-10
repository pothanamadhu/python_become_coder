def matrix(cols):
      k=[]
      for i in range(cols):
            k=list(map(int,input().split()))
            return k
rows=int(input())
cols=int(input())
arr1=[]
arr2=[]
arr3=[]
k1=0
for i in range(rows):
            arr1.append(matrix(cols))
for i in range(rows):
            arr2.append(matrix(cols))
for i in range(rows):
      for j in range(cols):
            for k in range(cols):
                  k1+=arr1[i][k]*arr2[k][j];
            arr3.append(k1)
            k1=0
for i in range(len(arr3)):
      print(arr3[i],end=" ")
      if i+1==cols:
            print()

            
      
      
