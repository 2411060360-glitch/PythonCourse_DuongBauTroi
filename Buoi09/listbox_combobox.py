import tkinter as tk
from tkinter import ttk

cua_so = tk.Tk()
cua_so.title("Hoat dong 3: Listbox & Combobox")
cua_so.geometry("320x450")

# --- BÀI TẬP 3.1: LISTBOX ---
tk.Label(cua_so, text="--- Listbox (Chon mon hoc) ---", font=("Arial", 10, "bold")).pack(pady=(10, 5))

listbox_mon_hoc = tk.Listbox(cua_so, selectmode="single", height=5)
for mon in ["Toan", "Ly", "Hoa", "Van", "Anh"]:
    listbox_mon_hoc.insert(tk.END, mon)
listbox_mon_hoc.pack(pady=5)

def xem_mon_da_chon():
    lua_chon = listbox_mon_hoc.curselection()
    if lua_chon:
        nhan_ket_qua_mon.config(text=f"Mon da chon: {listbox_mon_hoc.get(lua_chon[0])}")

tk.Button(cua_so, text="Xem mon da chon", command=xem_mon_da_chon).pack(pady=5)
nhan_ket_qua_mon = tk.Label(cua_so, text="", fg="blue")
nhan_ket_qua_mon.pack()

# Đường phân cách
tk.Frame(cua_so, height=2, bd=1, relief="sunken").pack(fill="x", padx=15, pady=15)

# --- BÀI TẬP 3.2: COMBOBOX ---
tk.Label(cua_so, text="--- Combobox (Chon thanh pho) ---", font=("Arial", 10, "bold")).pack(pady=5)

combobox_thanh_pho = ttk.Combobox(cua_so, values=["Ha Noi", "Da Nang", "TP.HCM", "Hue"])
combobox_thanh_pho.current(0) # chon gia tri dau tien lam mac dinh
combobox_thanh_pho.pack(pady=5)

def xem_thanh_pho():
    nhan_ket_qua_tp.config(text=f"Ban chon: {combobox_thanh_pho.get()}")

tk.Button(cua_so, text="Xac nhan thanh pho", command=xem_thanh_pho).pack(pady=5)
nhan_ket_qua_tp = tk.Label(cua_so, text="", fg="green")
nhan_ket_qua_tp.pack()

cua_so.mainloop()