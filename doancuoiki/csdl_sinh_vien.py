import sqlite3

TEN_FILE_CSDL = "quan_ly_sinh_vien.db"

def ket_noi_csdl():
    return sqlite3.connect(TEN_FILE_CSDL)

def tao_bang_neu_chua_co():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("""
    CREATE TABLE IF NOT EXISTS sinh_vien (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ma_sv TEXT NOT NULL,
        ho_ten TEXT NOT NULL,
        lop TEXT NOT NULL,
        diem_tb REAL NOT NULL,
        xep_loai TEXT NOT NULL
    )
    """)
    ket_noi.commit()
    ket_noi.close()

def tinh_xep_loai(diem_tb):
    if diem_tb >= 8.5:
        return "Xuat sac"
    elif diem_tb >= 7.0:
        return "Gioi"
    elif diem_tb >= 5.5:
        return "Kha"
    elif diem_tb >= 4.0:
        return "Trung binh"
    else:
        return "Yeu"

def them_sinh_vien(ma_sv, ho_ten, lop, diem_tb):
    xep_loai = tinh_xep_loai(diem_tb)
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute(
        "INSERT INTO sinh_vien (ma_sv, ho_ten, lop, diem_tb, xep_loai) VALUES (?, ?, ?, ?, ?)",
        (ma_sv, ho_ten, lop, diem_tb, xep_loai)
    )
    ket_noi.commit()
    ket_noi.close()

def lay_toan_bo_sinh_vien():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT id, ma_sv, ho_ten, lop, diem_tb, xep_loai FROM sinh_vien ORDER BY id")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua

def xoa_sinh_vien(id_sv):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("DELETE FROM sinh_vien WHERE id = ?", (id_sv,))
    ket_noi.commit()
    ket_noi.close()

def thong_ke_theo_xep_loai():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("SELECT xep_loai, COUNT(*) FROM sinh_vien GROUP BY xep_loai")
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua