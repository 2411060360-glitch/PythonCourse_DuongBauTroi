print("===== HOAT DONG 3.2 - PEP8 =====")

ten = "Nguyen Van A"
diem_toan = 8.5
diem_van = 7.0
so_luong_mon_hoc = 2
MUC_LUONG_TOI_THIEU = 5000000

print("Ten:", ten)
print("Diem Toan:", diem_toan)
print("Diem Van:", diem_van)
print("So luong mon hoc:", so_luong_mon_hoc)
print("Muc luong toi thieu:", MUC_LUONG_TOI_THIEU)
print("\n===== HOAT DONG 5.1 - TOAN TU SO HOC =====")

a = 17
b = 5

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)
print("\n===== HOAT DONG 5.2 - SO SANH VA LOGIC =====")

diem = 6.5
tuoi = 20

la_kha = diem >= 6.5 and diem < 8.0
chua_du_18_hoac_tren_60 = tuoi < 18 or tuoi > 60
phu_dinh_dieu_kien = not chua_du_18_hoac_tren_60

print("Diem dat loai Kha?", la_kha)
print("Tuoi chua du 18 hoac tren 60?", chua_du_18_hoac_tren_60)
print("Phu dinh dieu kien tren:", phu_dinh_dieu_kien)
print("\n===== HOAT DONG 5.3 - TOAN TU GAN VA DAC BIET =====")

x = 10

x += 5
print("Sau x += 5:", x)

x -= 5
print("Sau x -= 5:", x)

x *= 2
print("Sau x *= 2:", x)

x /= 2
print("Sau x /= 2:", x)

x //= 3
print("Sau x //= 3:", x)

x **= 2
print("Sau x **= 2:", x)

danh_sach = [1, 2, 3, "python"]

print("3 co trong danh_sach?", 3 in danh_sach)

danh_sach_2 = danh_sach
print("Hai bien cung tham chieu mot list?", danh_sach_2 is danh_sach)
print("\n===== HOAT DONG 5.4 - DO UU TIEN TOAN TU =====")

print(2 + 3 * 4 ** 2)
print((2 + 3) * 4 ** 2)
print(10 > 5 and 3 < 1 or not False)
print("\n===== HOAT DONG 6.1 - DYNAMIC TYPING =====")

bien = 10
print(bien, type(bien))

bien = "Xin chao"
print(bien, type(bien))

bien = 3.14
print(bien, type(bien))

bien = True
print(bien, type(bien))
print("\n===== HOAT DONG 6.2 - BAI TOAN TONG HOP =====")

ho_ten = "Nguyen Van A"

diem_toan = 8.0
diem_ly = 7.5
diem_hoa = 9.0

dtb = (diem_toan + diem_ly + diem_hoa) / 3

la_gioi = dtb >= 8.0
la_kha = dtb >= 6.5 and dtb < 8.0
la_trung_binh = dtb >= 5.0 and dtb < 6.5
la_yeu = dtb < 5.0

print(ho_ten, "- DTB:", round(dtb, 2))
print("Dat loai Gioi?", la_gioi)
print("Dat loai Kha?", la_kha)
print("Dat loai Trung binh?", la_trung_binh)
print("Dat loai Yeu?", la_yeu)
print("Kieu du lieu cua la_gioi:", type(la_gioi))