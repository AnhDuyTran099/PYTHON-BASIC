def xep_loai(point):
    if point>=9:
        return "Xuat sac"
    elif point>=8:
        return "Gioi"
    elif point>=6.5:
        return "Kha"
    elif point>=5:
        return "Trung binh"
    else:
        return "Yeu"
n=int(input())
a=list(map(float,input().split()))
DTB=sum(a)/n
print(f"Diem TB: {DTB:.2f}, Xep loai: {xep_loai(DTB)}")