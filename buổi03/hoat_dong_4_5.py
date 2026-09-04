import math


# HOAT DONG 4 - TUPLE

toa_do = (3, 5)

print(toa_do)
print(type(toa_do))


# Unpacking

x, y = toa_do

print("x =", x)
print("y =", y)


# Doi gia tri 2 bien

a = 10
b = 20

print("Truoc khi doi:")
print("a =", a)
print("b =", b)

a, b = b, a

print("Sau khi doi:")
print("a =", a)
print("b =", b)


# divmod

c = 17
d = 5

thuong_du = divmod(c, d)

thuong, du = thuong_du

print("Thuong:", thuong)
print("Du:", du)


# HOAT DONG 5

diem_a = (2, 3)
diem_b = (7, 8)

xa, ya = diem_a
xb, yb = diem_b

khoang_cach = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)

print("Khoang cach:", round(khoang_cach, 2))


# Yeu cau tinh khoang cach den O(0, 0)

cac_diem = [
    (0, 0),
    (3, 4),
    (6, 8)
]

for diem in cac_diem:
    x, y = diem

    khoang_cach = math.sqrt(x ** 2 + y ** 2)

    print(diem, "khoang cach den O:", round(khoang_cach, 2))