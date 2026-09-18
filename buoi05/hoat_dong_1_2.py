print("====Bai1 xep loai hoc luc====")
ho_ten = input("nhap ho ten:")
diem_toan = float(input("nhap diem toan:"))
diem_ly = float(input("nhap diem ly:"))
diem_hoa = float(input("nhap diem hoa"))
dtb = (diem_toan + diem_ly + diem_hoa)/3
if dtb >= 8:
    xep_loai = "gioi"
elif dtb >=6.5:
    xep_loai = "kha"
elif dtb >= 5:
    xep_loai = "trung binh"
else:
    xep_loai = "yeu"
print("ho ten",ho_ten)
print("diem trung binh",dtb)
print("xep loai",xep_loai)


print("\n====Bai2 tim so lon nhat====")
a = float(input("nhap so thu nhat:"))
b = float(input("nhap so thu hai:"))
c = float(input("nhap so thu ba:"))
if a >=b and a >= c:
    lon_nhat = a
elif b >= a and b >=c:
    lon_nhat = b
else:
    lon_nhat = c
print("so lon nhat la:",lon_nhat)