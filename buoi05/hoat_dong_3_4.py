print("====Bai3 bang cuu chuong====")
n = int(input("nhap so:"))
for i in range(1, 11):
    print(n, "x", i, "=", n*i)

print("\n====Bai4 tinh giai thua====")
n = int(input("nhap so:"))
giai_thua = 1
i=1
while i <= n:
    giai_thua = giai_thua * i
    i = i + 1
print(n,"!=",giai_thua)

print("\n====Bai5 tong cac chu so====")
so = int(input("nhap mot so:"))
so_tam = so
tong = 0

while so_tam > 0:
    tong += so_tam % 10
    so_tam = so_tam // 10
print("Tong cac chu so la:", tong)