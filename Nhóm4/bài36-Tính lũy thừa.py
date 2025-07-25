a,n=map(int,input().split())
if n==0:
    print(1)
else:
    m=a
    for i in range(1,n):
        a*=m
    print(a)
