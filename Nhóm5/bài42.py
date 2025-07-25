km=float(input())
if km<=1:
    print(15000)
elif km<=5:
    print(int(15000+(km-1)*12000))
else:
    print(int(15000+4*12000+(km-5)*10000))