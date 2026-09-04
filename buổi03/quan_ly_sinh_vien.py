# MINI PROJECT 1
# QUAN LY SINH VIEN

danh_sach_sv = [
    (8.5, "An"),
    (7.0, "Binh"),
    (9.2, "Chi"),
    (6.5, "Dung")
]


print("Danh sach ban dau:")

for diem, ten in danh_sach_sv:
    print(ten, diem)


# Them sinh vien

danh_sach_sv.append((8.0, "Em"))

print("Sau khi them:")

for diem, ten in danh_sach_sv:
    print(ten, diem)


# Xoa Binh

danh_sach_sv.remove((7.0, "Binh"))

print("Sau khi xoa Binh:")

for diem, ten in danh_sach_sv:
    print(ten, diem)


# Sua diem sinh vien dau tien

danh_sach_sv[0] = (9.0, danh_sach_sv[0][1])

print("Sau khi sua diem:")

for diem, ten in danh_sach_sv:
    print(ten, diem)


# Kiem tra Chi

print("Chi co trong danh sach khong?")

print((9.2, "Chi") in danh_sach_sv)


# Sap xep tang dan

danh_sach_sv.sort()

print("Sap xep tang dan:")

for diem, ten in danh_sach_sv:
    print(ten, diem)


# Sap xep giam dan

danh_sach_sv.sort(reverse=True)

print("Sap xep giam dan:")

for diem, ten in danh_sach_sv:
    print(ten, diem)