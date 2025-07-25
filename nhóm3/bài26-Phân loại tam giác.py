a,b,c=map(float,input().split())
if a==b==c:
    print("Tam giac deu")
elif a!=b and a!=c and b!=c:
    print("Tam giac thuong")
else:
    print("Tam giac can")
