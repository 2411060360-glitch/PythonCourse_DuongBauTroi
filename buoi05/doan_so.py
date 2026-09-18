import random

print("===== TRO CHOI DOAN SO =====")

so_can_doan = random.randint(1, 100)

so_luot_toi_da = 7
luot_hien_tai = 0

while luot_hien_tai < so_luot_toi_da:

    luot_hien_tai = luot_hien_tai + 1

    print("Luot", luot_hien_tai, "/", so_luot_toi_da)

    so_doan = int(input("Nhap so ban doan tu 1 den 100: "))

    if so_doan == so_can_doan:
        print("Chinh xac!")
        print("Ban da doan dung sau", luot_hien_tai, "luot")
        break

    elif so_doan < so_can_doan:
        print("So can doan LON HON")

    else:
        print("So can doan NHO HON")

if so_doan != so_can_doan:
    print("Ban da het luot")
    print("So can tim la:", so_can_doan)