def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
a,b=map(int,input().split())
print(f"UCLN: {gcd(a,b)}, BCNN: {(a*b)//gcd(a,b)}")
