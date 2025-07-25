n=int(input())
m=n
rev=0
while n:
    rev=rev*10+n%10
    n//=10
print("Doi xung" if rev==m else "Khong doi xung")
