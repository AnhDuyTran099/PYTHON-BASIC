def convert_to_bin(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return convert_to_bin(n//2)+str(n%2)
"""
    hàm bin():
    n=???(ví dụ 25)
    *Lấy toàn bộ kể cả chỉ định
        res=bin(25)
        -> res=0b11001 với 0b là chỉ định đây là số nhị phân
    *Chỉ lấy phần nhị phân
        res=bin(25)[2:]
        -> res=11001
"""
n=int(input())
#print(bin(n)[2:])
print(convert_to_bin(n))
