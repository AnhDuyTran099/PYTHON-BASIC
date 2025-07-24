import math
def check(n):
    if n<2:
        return False
    if n<=3:
        return True
    if n%2==0 or n%3==0:
        return False
    k=math.isqrt(n)
    for i in range(5,k+1,6):
        if n%i==0 or n%(i+2)==0:
            return False
    return True
n=int(input())
print("La so nguyen to" if check(n) else "Khong phai la so nguyen to")