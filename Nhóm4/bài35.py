n=int(input())
ans=[]
a=[True]*(n+1)
for i in range(2,n+1):
    if a[i]:
        ans.append(i)
        for j in range(i*i,n+1,i):
            a[j]=False
for i in ans:
    print(i,end=" ")