# BAI 1.1
def uscln(a,b):
    while b!=0:
        a,b = b,a%b
    return a
def bscnn(a,b):
    return a*b // uscln(a,b)

def kiem_tra_nguyen_to(n):
    if n<2:
        return False

    for i in range(2,n):
        if n%i==0:
            return False

    return True
def kiem_tra_so_hoan_thien(n):
    tong_uoc = 0
    for i in range ( 1, n):
        if n%1==0:
            tong_uoc +=1

    return tong_uoc == n
print("USCLN:")
print(uscln(24,36))
print(uscln(10,15))
print(uscln(18,27))

print("BSCLN")
print(bscnn(4,6))
print(bscnn(10,15))
print(bscnn(3,5))

print("SO NGUYEN TO:")
print(kiem_tra_nguyen_to(2))
print(kiem_tra_nguyen_to(7))
print(kiem_tra_nguyen_to(10))

print("so hoan thien:")
print(kiem_tra_so_hoan_thien(6))
print(kiem_tra_so_hoan_thien(28))
print(kiem_tra_so_hoan_thien(10))

# Bai2

def in_loi_chao(ten):
    print("xin chao," ,ten)
    return
    
def chia_lay_thuong_du(a,b):
    return a // b, a % b
in_loi_chao("Duong")
thuong, du= chia_lay_thuong_du(17,5)
print("thuong:",thuong)
print("Du",du)

# HOAT DONG 2

def gioi_thieu(ten,tuoi=20,lop="DH14C1" ):
    print("Ten:",ten)
    print("tuoi",tuoi)
    print("lop",lop)

gioi_thieu("Duong")
gioi_thieu("Hong",20)
gioi_thieu("Anh",lop="12A5")
gioi_thieu("Khoi",lop="12A5",tuoi=20)

# HOAT DONG 3.1

def tinh_tong(*args):
    tong=0
    for so in args:
        tong+=so

    return tong
print(tinh_tong(1,2,3))
print(tinh_tong(5,10,15,20))
print(tinh_tong())

# HOAT DONG 3.2

def in_thong_tin(ho_ten, tuoi, **kwargs):
    print("Ho ten:", ho_ten)
    print("Tuoi:", tuoi)

    for khoa, gia_tri in kwargs.items():
        print(khoa, ":", gia_tri)


in_thong_tin(
    "Nguyen Hoang Duong",
    20,
    lop="12a5",
    que_quan="Ha Noi"
)

in_thong_tin(
    "Phung Dinh khoi",
    20,
    email="dnasuccess123.com"
)