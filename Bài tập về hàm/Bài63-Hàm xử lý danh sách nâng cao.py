from collections import defaultdict, Counter
from statistics import mean, median, multimode
def loc_so_chan(arr):
    return [i for i in arr if i%2==0]
def bien_doi_danh_sach(arr,ham_bien_doi):
    return [ham_bien_doi(x) for x in arr]
def gom_nhom_theo_dieu_kien(arr,ham_dieu_kien):
    a=defaultdict(list)
    for x in arr:
        k=ham_dieu_kien(x)
        a[k].append(x)
    return dict(a)
def tinh_thong_ke(arr):
    m=mean(arr)
    med=median(arr)
    modes=multimode(arr)
    mode_val=modes[0] if len(modes)==1 else modes
    return {
        'mean': m,
        'median': med,
        'mode': mode_val
    }
"""
-Ví dụ:
    ds = [5, 2, 8, 3, 2, 9, 4]
    #lọc số chẵn
    print("Các số chẵn:", loc_so_chan(ds))
    # nhân đôi mỗi phần tử
    ds2=bien_doi_danh_sach(ds,lambda x:x*2)
    print(ds2)
    # nhóm chẵn/lẻ
    nhom=gom_nhom_theo_dieu_kien(ds, lambda x: 'chan' if x % 2 == 0 else 'le')
    print(nhom)
    # thống kê
    stats=tinh_thong_ke(ds)
    print(stats['mean'])
    print(stats['median'])
    print(stats['mode'])
"""