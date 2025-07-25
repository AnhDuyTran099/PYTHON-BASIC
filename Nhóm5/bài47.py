def check_year(n):
    if (n%4==0 and n%100!=0) or n%400==0:
        return True
    return False
month,year=map(int,input().split())
if month<=7:
    if month==2:
        if check_year(year):
            print(29)
        else:
            print(28)
    elif month%2==0:
        print(30)
    else:
        print(31)
else:
    if month%2==0:
        print(31)
    else:
        print(30)