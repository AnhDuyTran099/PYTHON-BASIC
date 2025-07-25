#Tự thử đi, lười ví dụ rồi =￣ω￣=
import random
def tung_xu(so_lan):
    ket_qua = []
    for _ in range(so_lan):
        ket_qua.append('Ngửa' if random.random() < 0.5 else 'Sấp')
    return ket_qua
def tung_xuc_xac(so_matso_lan):
    return [random.randint(1, so_mat) for _ in range(so_lan)]
def doan_so(min_val,max_val):
    secret = random.randint(min_val, max_val)
    print(f"Đã chọn một số trong khoảng [{min_val}, {max_val}]. Hãy đoán!")
    lan = 0
    while True:
        lan += 1
        guess = int(input("Nhập dự đoán: "))
        if guess < secret:
            print("Số quá nhỏ, thử lại.")
        elif guess > secret:
            print("Số quá lớn, thử lại.")
        else:
            print(f"Chúc mừng! Bạn đoán đúng sau {lan} lần.")
            break
def bai_cao_thap():
    suits=['♥','♦','♣','♠']
    ranks=list(range(1, 14))
    deck=[(r, s) for s in suits for r in ranks]
    random.shuffle(deck)
    player_card=deck.pop()
    computer_card=deck.pop()
    def card_str(card):
        r,s=card
        if r==1:
            name='A'
        elif r==11:
            name = 'J'
        elif r == 12:
            name = 'Q'
        elif r == 13:
            name = 'K'
        else:
            name = str(r)
        return f"{name}{s}"
    print(f"Bạn rút:     {card_str(player_card)}")
    print(f"Máy rút:     {card_str(computer_card)}")
    if player_card[0] > computer_card[0]:
        print("Bạn thắng!")
    elif player_card[0] < computer_card[0]:
        print("Máy thắng!")
    else:
        print("Hòa nhau!")