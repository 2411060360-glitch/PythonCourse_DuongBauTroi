# =========================
# HOAT DONG 6
# DE QUY
# =========================


# Bai 6.1 - Giai thua bang de quy

def giai_thua_de_quy(n):
    if n <= 1:
        return 1

    return n * giai_thua_de_quy(n - 1)


# Giai thua bang vong lap

def giai_thua_lap(n):
    ket_qua = 1

    for i in range(1, n + 1):
        ket_qua = ket_qua * i

    return ket_qua


# So sanh

print("Giai thua bang de quy:", giai_thua_de_quy(5))
print("Giai thua bang vong lap:", giai_thua_lap(5))


# =========================
# Bai 6.2 - Fibonacci
# =========================

def fibonacci_de_quy(n):
    if n <= 1:
        return n

    return fibonacci_de_quy(n - 1) + fibonacci_de_quy(n - 2)


print("10 so Fibonacci dau tien:")

for i in range(10):
    print(fibonacci_de_quy(i), end=" ")

print()