import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import csdl_sinh_vien as db

DANH_SACH_LOP = ["CNTT K15", "KTPM K15", "KHMT K15", "HTTT K15", "Khac"]

class UngDungQuanLySV(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quan ly Sinh vien")
        self.geometry("620x520")
        self.resizable(False, False)

        db.tao_bang_neu_chua_co()
        self.khoi_tao_giao_dien()
        self.tai_lai_danh_sach()

    def khoi_tao_giao_dien(self):
        khung_nhap = tk.LabelFrame(self, text="Thong tin sinh vien", padx=10, pady=10)
        khung_nhap.pack(pady=10, padx=10, fill="x")

        tk.Label(khung_nhap, text="Ma SV:").grid(row=0, column=0, sticky="w", pady=5)
        self.o_nhap_ma_sv = tk.Entry(khung_nhap, width=30)
        self.o_nhap_ma_sv.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Ho ten:").grid(row=1, column=0, sticky="w", pady=5)
        self.o_nhap_ho_ten = tk.Entry(khung_nhap, width=30)
        self.o_nhap_ho_ten.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Lop:").grid(row=2, column=0, sticky="w", pady=5)
        self.chon_lop = ttk.Combobox(khung_nhap, values=DANH_SACH_LOP, width=27, state="readonly")
        self.chon_lop.current(0)
        self.chon_lop.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Diem TB:").grid(row=3, column=0, sticky="w", pady=5)
        self.o_nhap_diem = tk.Entry(khung_nhap, width=30)
        self.o_nhap_diem.grid(row=3, column=1, padx=10, pady=5)

        tk.Button(khung_nhap, text="Them sinh vien", command=self.xu_ly_them_sv, bg="#2e7d32", fg="white", font=("Arial", 9, "bold")).grid(row=4, column=0, columnspan=2, pady=10)

        khung_danh_sach = tk.LabelFrame(self, text="Danh sach sinh vien", padx=10, pady=5)
        khung_danh_sach.pack(pady=5, padx=10, fill="both", expand=True)

        self.listbox_sv = tk.Listbox(khung_danh_sach, width=80, height=12)
        self.listbox_sv.pack(side="left", fill="both", expand=True)

        thanh_cuon = tk.Scrollbar(khung_danh_sach, orient="vertical", command=self.listbox_sv.yview)
        thanh_cuon.pack(side="right", fill="y")
        self.listbox_sv.config(yscrollcommand=thanh_cuon.set)

        khung_nut = tk.Frame(self)
        khung_nut.pack(pady=10)

        tk.Button(khung_nut, text="Xoa sinh vien", command=self.xu_ly_xoa_sv, bg="#d32f2f", fg="white").grid(row=0, column=0, padx=10)
        tk.Button(khung_nut, text="Thong ke xep loai", command=self.xu_ly_thong_ke, bg="#ed6c02", fg="white").grid(row=0, column=1, padx=10)

    def tai_lai_danh_sach(self):
        self.listbox_sv.delete(0, tk.END)
        self.danh_sach_hien_tai = db.lay_toan_bo_sinh_vien()
        for sv in self.danh_sach_hien_tai:
            id_sv, ma_sv, ho_ten, lop, diem_tb, xep_loai = sv
            self.listbox_sv.insert(tk.END, f"[{ma_sv}] {ho_ten} - Lop: {lop} | Diem TB: {diem_tb} -> Xep loai: {xep_loai}")

    def xu_ly_them_sv(self):
        ma_sv = self.o_nhap_ma_sv.get().strip()
        ho_ten = self.o_nhap_ho_ten.get().strip()
        lop = self.chon_lop.get()
        diem_str = self.o_nhap_diem.get().strip()

        if ma_sv == "" or ho_ten == "" or diem_str == "":
            messagebox.showerror("Loi", "Vui long nhap day du thong tin sinh vien.")
            return

        try:
            diem_tb = float(diem_str)
            if diem_tb < 0 or diem_tb > 10:
                messagebox.showerror("Loi", "Diem trung binh phai tu 0.0 den 10.0")
                return
        except ValueError:
            messagebox.showerror("Loi", "Diem trung binh phai la mot so thuc hop le.")
            return

        db.them_sinh_vien(ma_sv, ho_ten, lop, diem_tb)
        self.o_nhap_ma_sv.delete(0, tk.END)
        self.o_nhap_ho_ten.delete(0, tk.END)
        self.o_nhap_diem.delete(0, tk.END)
        self.tai_lai_danh_sach()
        messagebox.showinfo("Thanh cong", f"Da them sinh vien: {ho_ten}")

    def xu_ly_xoa_sv(self):
        lua_chon = self.listbox_sv.curselection()
        if not lua_chon:
            messagebox.showerror("Loi", "Vui long chon sinh vien trong danh sach de xoa.")
            return
        id_sv = self.danh_sach_hien_tai[lua_chon[0]][0]
        db.xoa_sinh_vien(id_sv)
        self.tai_lai_danh_sach()
        messagebox.showinfo("Thanh cong", "Da xoa sinh vien khoi danh sach.")

    def xu_ly_thong_ke(self):
        du_lieu = db.thong_ke_theo_xep_loai()
        if not du_lieu:
            messagebox.showinfo("Thong bao", "Chua co du lieu sinh vien de thong ke.")
            return

        danh_sach_xep_loai = [dong[0] for dong in du_lieu]
        so_luong = [dong[1] for dong in du_lieu]

        plt.figure(figsize=(6, 4))
        bars = plt.bar(danh_sach_xep_loai, so_luong, color="mediumseagreen")
        plt.title("THONG KE SINH VIEN THEO XEP LOAI")
        plt.xlabel("Xep loai")
        plt.ylabel("So luong sinh vien")

        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval + 0.05, int(yval), ha='center', va='bottom')

        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    ung_dung = UngDungQuanLySV()
    ung_dung.mainloop()