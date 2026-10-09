import tkinter as tk

# Khởi tạo cửa sổ
cua_so = tk.Tk()
cua_so.title("Ung dung demo")
cua_so.geometry("400x300")

# Không cho kéo giãn cửa sổ (Bài 1.2)
cua_so.resizable(False, False)

# Thêm nhãn nội dung (Bài 1.2)
nhan = tk.Label(cua_so, text="Xin chao Tkinter!", font=("Arial", 16))
nhan.pack(pady=20)

# Vòng lặp sự kiện duy nhất ở cuối file
cua_so.mainloop()