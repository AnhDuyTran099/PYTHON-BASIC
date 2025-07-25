import math
"""
        -Hàm lần lượt trả về:
            +Diện tích hình vuông
            +Diện tích hình chữ nhật
            +Diện tích hình tròn
            +Diện tích hình tam giác
"""
def square_area(n):
    if n<=0:
        return "Loi: Canh phai duong"
    return n**2
def rectangle_area(a,b):
    if a<=0 or b<=0:
        return "Loi: Cac canh phai duong"
    return a*b
def circle_area(r):
    if r<=0:
        return "Loi: Ban kinh phai duong"
    return math.pi*(r**2)
def triangle_area(a,b,c): #heron formula
    if a<=0 or b<=0 or c<=0:
        return "Loi: Cac canh phai duong"
    if a+b<=c or a+c<=b or b+c<=a:
        return "Loi: Cac canh phai duong"
    s=(a+b+c)/2
    s=s*(s-a)*(s-b)*(s-c)
    return math.sqrt(s)
#Hình vuông
"""
    n=int(input())
    print(square_area(n))
"""
#Hình chữ nhật
"""
    a,b=map(int,input().split())
    print(rectangle_area(a,b))
"""
#Hình tròn
"""
    r=int(input())
    print(circle_area(r))
"""
#Hình tam giác theo công thức Heron
"""
    a,b,c=map(int,input().split())
    print(triangle_area(a,b,c))
"""