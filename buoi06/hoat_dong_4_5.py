# =========================
# HOAT DONG 4
# BIEN LOCAL VA GLOBAL
# =========================

so_luot_truy_cap = 0


def tang_luot_truy_cap():
    global so_luot_truy_cap
    so_luot_truy_cap += 1


def vi_du_bien_local():
    so_luot_truy_cap = 100
    print("Ben trong ham:", so_luot_truy_cap)


tang_luot_truy_cap()
tang_luot_truy_cap()

print("So luot truy cap:", so_luot_truy_cap)

vi_du_bien_local()

print("Sau khi goi ham:", so_luot_truy_cap)


# =========================
# HOAT DONG 5
# LAMBDA, MAP, FILTER, SORTED
# =========================

danh_sach_so = [1, 2, 3, 4, 5]


# Bai 5.1 - map()

binh_phuong = list(
    map(lambda x: x ** 2, danh_sach_so)
)

print("Binh phuong:", binh_phuong)


# Bai 5.2 - filter()

so_chan = list(
    filter(lambda x: x % 2 == 0, danh_sach_so)
)

print("So chan:", so_chan)


# Bai 5.3 - sorted()

danh_sach_sv = [
    {"ten": "An", "diem": 8.5},
    {"ten": "Binh", "diem": 7.0},
    {"ten": "Chi", "diem": 9.2}
]


# Sap xep tang dan

sap_xep_theo_diem = sorted(
    danh_sach_sv,
    key=lambda sv: sv["diem"]
)

print("Tang dan:")

for sv in sap_xep_theo_diem:
    print(sv["ten"], "-", sv["diem"])


# Sap xep giam dan

sap_xep_giam_dan = sorted(
    danh_sach_sv,
    key=lambda sv: sv["diem"],
    reverse=True
)

print("Giam dan:")

for sv in sap_xep_giam_dan:
    print(sv["ten"], "-", sv["diem"])