A,B,c=input().split()
a,b=float(A),float(B)
if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    print(a/b if b!=0 else "Loi: Khong the chia cho 0")
else:
    print("Phep toan khong hop le")