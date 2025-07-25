import math
n=int(input())
t=0
for i in range(1,math.isqrt(n)+1):
    if n%i==0:
        t+=i
        if i!=n//i:
            t+=n//i
t-=n
print("La so hoan hao" if t==n else "Khong phai so hoan hao")
