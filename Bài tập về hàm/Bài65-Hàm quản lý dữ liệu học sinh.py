def them_hoc_sinh(danh_sach,ten,tuoi,diem):
    hs={'ten':ten.strip(),'tuoi': tuoi,'diem': diem}
    danh_sach.append(hs)
def tim_hoc_sinh(danh_sach,ten):
    key=ten.strip().lower()
    return [hs for hs in danh_sach if key in hs['ten'].lower()]
def xep_loai_hoc_sinh(diem):
    if diem>=8.0:
        return 'Giỏi'
    elif diem>=6.5:
        return 'Khá'
    elif diem>=5.0:
        return 'Trung bình'
    else:
        return 'Yếu'
def thong_ke_lop(danh_sach):
    if not danh_sach:
        return {'so_luong': 0, 'diem_trung_binh': 0, 'phan_loai': {}}
    n=len(danh_sach)
    t=sum(hs['diem'] for hs in danh_sach)
    avg=t/n
    phan_loai={}
    for hs in danh_sach:
        l=xep_loai_hoc_sinh(hs['diem'])
        phan_loai[l]=phan_loai.get(l,0)+1
    return{
        'so_luong': n,
        'diem_trung_binh': avg,
        'phan_loai': phan_loai
    }
def sap_xep_theo_diem(danh_sach,giam_dan:bool = True):
    return sorted(danh_sach,key=lambda hs: hs['diem'],reverse=giam_dan)
#Ví dụ

lop=[]
them_hoc_sinh(lop,"Nguyễn Văn A", 15, 8.5)
them_hoc_sinh(lop,"Trần Thị B", 16, 6.8)
them_hoc_sinh(lop,"Lê Văn C", 15, 4.2)
them_hoc_sinh(lop,"Phạm Thị D", 17, 9.1)   
print("Tất cả HS:")
for hs in lop:
    print(hs)
print("\nTìm tên 'Văn':", tim_hoc_sinh(lop, "Văn"))
print("\nPhân loại từng HS:")
for hs in lop:
    print(f"{hs['ten']}: {xep_loai_hoc_sinh(hs['diem'])}")
stats=thong_ke_lop(lop)
print("\nThống kê lớp:", stats)
print("\nSắp xếp theo điểm giảm dần:")
for hs in sap_xep_theo_diem(lop):
    print(hs)
print("\nSắp xếp theo điểm tăng dần:")
for hs in sap_xep_theo_diem(lop, giam_dan=False):
    print(hs)
