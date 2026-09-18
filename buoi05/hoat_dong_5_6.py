print("===== BAI 1: PASS =====")

diem = 6.5

if diem >= 8:
    pass
elif diem >= 5:
    print("Dat yeu cau")
else:
    pass


print("\n===== BAI 2: KIEM TRA SO NGUYEN TO =====")

so = int(input("Nhap mot so: "))

la_so_nguyen_to = True

if so < 2:
    la_so_nguyen_to = False
else:
    for i in range(2, so):
        if so % i == 0:
            la_so_nguyen_to = False
            break

if la_so_nguyen_to == True:
    print(so, "la so nguyen to")
else:
    print(so, "khong phai so nguyen to")


print("\n===== BAI 3: CONTINUE =====")

danh_sach = [5, -3, 8, 0, -1, 12, 7, -9]
danh_sach_hop_le = []

for so in danh_sach:
    if so <= 0:
        continue

    danh_sach_hop_le.append(so)

print("Cac so duong:", danh_sach_hop_le)


print("\n===== BAI 4: TAM GIAC SAO =====")

n = 5

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()


print("\n===== BAI 5: HINH THOI SAO =====")

n = 4

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))