import customtkinter as ctk

ctk.set_appearance_mode("light")  # veya "dark"
ctk.set_default_color_theme("blue")  # renk teması

# Ana pencere
app = ctk.CTk()
app.geometry("300x400")
app.title("Modern Hesap Makinesi")

# Giriş ekranı
giris = ctk.CTkEntry(app, font=("Arial", 24), justify="right", width=250, height=50)
giris.pack(pady=20)

# Buton fonksiyonu
def tikla(deger):
    mevcut = giris.get()
    giris.delete(0, ctk.END)
    giris.insert(0, mevcut + str(deger))

def temizle():
    giris.delete(0, ctk.END)

def hesapla():
    try:
        sonuc = eval(giris.get())
        giris.delete(0, ctk.END)
        giris.insert(0, str(sonuc))
    except:
        giris.delete(0, ctk.END)
        giris.insert(0, "HATA")

# Tuşlar
butonlar = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

# Tuşları yerleştir
for satir in butonlar:
    frame = ctk.CTkFrame(app)
    frame.pack(pady=5)
    for btn in satir:
        if btn == "=":
            b = ctk.CTkButton(frame, text=btn, width=50, command=hesapla)
        else:
            b = ctk.CTkButton(frame, text=btn, width=50, command=lambda x=btn: tikla(x))
        b.pack(side="left", padx=5)

# Temizle butonu
temizle_btn = ctk.CTkButton(app, text="Temizle", command=temizle)
temizle_btn.pack(pady=10)

app.mainloop()
