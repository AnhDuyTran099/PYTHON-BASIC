year=int(input())
print("Nam nhuan" if (year%4==0 and year%100!=0) or year%400==0 else "Khong phai nam nhuan")
