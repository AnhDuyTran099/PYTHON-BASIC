import random
ans=random.randint(1,100)
d=0
while True:
    guess=int(input("Ban doan so: "))
    d+=1
    if guess==ans:
        print(f"Dung roi! Ban da doan sau {d} lan.")
        break
    else:
        if guess>ans:
            print("Lon hon")
        else:
            print("Nho hon")