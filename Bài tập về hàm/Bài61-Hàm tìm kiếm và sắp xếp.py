def max_min(arr):
    return max(arr),min(arr)
def linear_search(arr,gt):
    for i,x in enumerate(arr):
        if x==gt:
            return i
    return -1
def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-1-i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return arr
def selection_sort(arr):
    n=len(a)
    for i in range(n-1):
        mi=i
        for j in range(i+1,n):
            if a[j]<a[mi]:
                mi=j
        a[i],a[mi]=a[mi],a[i]
    return a
"""
    Ví dụ a=[1,5,7,2,7] (gt=5 đối với hàm linear_search)
    Thì:
        -Hàm max_min sẽ trả về 2 giá trị là 7 và 1
        -Hàm linear_search sẽ trả về giá trị là 2
        -Hàm bubble_sort và selection_sort đều trả về là [1,2,5,7,7]
"""