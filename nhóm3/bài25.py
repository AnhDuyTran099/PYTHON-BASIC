a,b,c=map(float,input().split())
print("Hop le" if a+b>c and b+c>a and a+c>b else "Khong hop le")