n=int(input())
if n==1:
    print(0)
elif n==2:
    print(0,1)
else:
    print(0,1,end=" ")
    a=0
    b=1
    n-=2
    while n>0:
        c=a+b
        a=b
        b=c
        print(c,end=" ")
        n-=1