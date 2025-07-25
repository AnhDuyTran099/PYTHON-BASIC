n=int(input())
a=list(map(int,input().split()))
ma=0
for i in a:
    if ma>i:
        ma=i
print(ma)
