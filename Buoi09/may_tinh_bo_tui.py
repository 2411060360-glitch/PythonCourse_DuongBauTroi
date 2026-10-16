import tkinter as tk

cua_so = tk.Tk()
cua_so.title("May tinh bo tui")
cua_so.geometry("320x420")
cua_so.resizable(False, False)

bieu_thuc = ""
bien_hien_thi = tk.StringVar(value="0")

# Man hinh hien thi
entry_hien_thi = tk.Entry(cua_so, textvariable=bien_hien_thi, font=("Arial", 18), justify="right", bd=8)
entry_hien_thi.grid(row=0, column=0, columnspan=4, padx=10, pady=15, sticky="ew")

def nhap_ky_tu(ky_tu):
    global bieu_thuc
    bieu_thuc += str(ky_tu)
    bien_hien_thi.set(bieu_thuc)

def xoa_toan_bo():  # Nut C: Xoa het bieu thuc
    global bieu_thuc
    bieu_thuc = ""
    bien_hien_thi.set("0")

def xoa_mot_ky_tu():  # Nut DEL: Xoa 1 ky tu cuoi cung
    global bieu_thuc
    bieu_thuc = bieu_thuc[:-1]
    bien_hien_thi.set(bieu_thuc if bieu_thuc != "" else "0")

def tinh_ket_qua():
    global bieu_thuc
    try:
        ket_qua = str(eval(bieu_thuc))
        bien_hien_thi.set(ket_qua)
        bieu_thuc = ket_qua
    except Exception:
        bien_hien_thi.set("Loi")
        bieu_thuc = ""

# Danh sach cac nut: (Ten nut, Hang, Cot)
danh_sach_nut = [
    ('C', 1, 0), ('DEL', 1, 1), ('(', 1, 2), (')', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3),
]

for (text, row, col) in danh_sach_nut:
    if text == 'C':
        tk.Button(cua_so, text=text, font=("Arial", 11, "bold"), bg="#ffcdd2", width=5, height=2, command=xoa_toan_bo).grid(row=row, column=col, padx=3, pady=3)
    elif text == 'DEL':
        tk.Button(cua_so, text=text, font=("Arial", 11, "bold"), bg="#ffe0b2", width=5, height=2, command=xoa_mot_ky_tu).grid(row=row, column=col, padx=3, pady=3)
    elif text == '=':
        tk.Button(cua_so, text=text, font=("Arial", 11, "bold"), bg="#c8e6c9", width=5, height=2, command=tinh_ket_qua).grid(row=row, column=col, padx=3, pady=3)
    else:
        tk.Button(cua_so, text=text, font=("Arial", 11), width=5, height=2, command=lambda t=text: nhap_ky_tu(t)).grid(row=row, column=col, padx=3, pady=3)

cua_so.mainloop()