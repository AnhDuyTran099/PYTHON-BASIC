def check_prime(n):
    if n<2:
        return False
    if n<=3:
        return True
    if n%2==0 or n%3==0:
        return False
    m=n**0.5
    for i in range(5,m+1,6):
        if n%i==0 or n%(i+2)==0:
            return False
    return True
n=int(input())
print(check_prime1(n))