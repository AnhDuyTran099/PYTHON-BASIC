def countWord(s):
    """
        Một từ được định nghĩa là dãy ký tự tách biệt bởi khoảng trắng
        -> Tách theo whitespace và bỏ các phần rỗng
    """
    a=[i for i in s.strip().split() if i]
    return len(a)
def rev(s):
    return s[::-1]
def check_palin(s):
    s=''.join(s.split()).lower()
    return s==s[::-1]
def stdd_name(s):
    a=[i.lower().capitalize() for i in s.strip().split() if i]
    return ' '.join(a)
"""
    Ví dụ s="Hoàng CỬU bẢo is chinese"
    Thì:
        -Hàm countWord sẽ trả về giá trị là 5
        -Hàm rev sẽ trả về là esenihc si oẢb UỬC gnàoH
        -Hàm check_palin sẽ trả về giá trị False
        -Hàm stdd_name sẽ trả về là Hoàng Cửu Bảo Is Chinese
"""