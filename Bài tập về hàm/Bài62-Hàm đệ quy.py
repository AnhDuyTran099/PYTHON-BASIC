def fib(n):
    if n==0 or n==1:
        return n
    return (n-1)+(n-2)
def expon(cs,m):
    if m==0:
        return 1
    if m>0:
        return cs*expon(cs,m-1)
    return 1/expon(cs,-m)
def rev(s):
    if s=="":
        return ""
    return rev(s[1:])+s[0]
def gcd(a,b):
    a,b=abs(a),abs(b)
    if b==0:
        return a
    return gcd(b,a%b)
"""
    Ví dụ
    -Với n=7 thì fib(n) có giá trị là 13
    -Với cs=2 và m=3 thì expon(cs,m) có giá trị là 8
    -Với s="reven" thì rev(s) sẽ có kết quả là never
    -Với a=tích 10 hợp số đầu tiên và b=tích 10 số nguyên tố đầu tiên thì gcd(a,b) có giá trị là 210
"""