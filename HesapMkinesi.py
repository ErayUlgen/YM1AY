import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("350x550")
app.title("🧮 Modern Hesap Makinesi")
app.configure(fg_color="#ecf0f3")

# Giriş alanı
giris = ctk.CTkEntry(app, font=("Helvetica", 28), justify="right", width=300, height=60,
                     corner_radius=15, border_width=2)
giris.pack(pady=30)

# Buton işlevleri
def tikla(deger):
    giris.insert("end", str(deger))

def temizle():
    giris.delete(0, "end")

def hesapla():
    try:
        sonuc = eval(giris.get())
        giris.delete(0, "end")
        giris.insert(0, str(sonuc))
    except:
        giris.delete(0, "end")
        giris.insert(0, "HATA")

def geri_sil():
    giris.delete(len(giris.get()) - 1, "end")

def isaret_degistir():
    try:
        mevcut = giris.get()
        if mevcut:
            sonuc = eval(f"-1*({mevcut})")
            giris.delete(0, "end")
            giris.insert(0, str(sonuc))
    except:
        pass

# Tuş oluşturucu
def olustur_buton(parent, text, command, genislik=65):
    return ctk.CTkButton(parent, text=text, font=("Helvetica", 20), width=genislik, height=65,
                         corner_radius=32, fg_color="#ffffff", hover_color="#d1d8e0",
                         text_color="#2c3e50", command=command)

# Yardımcı tuşlar
yardimci_frame = ctk.CTkFrame(app, fg_color="transparent")
yardimci_frame.pack(pady=5)

olustur_buton(yardimci_frame, "C", temizle).pack(side="left", padx=5)
olustur_buton(yardimci_frame, "⌫", geri_sil).pack(side="left", padx=5)
olustur_buton(yardimci_frame, "+/-", isaret_degistir).pack(side="left", padx=5)
olustur_buton(yardimci_frame, "%", lambda: tikla('%')).pack(side="left", padx=5)

# Ana tuşlar
butonlar = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for satir in butonlar:
    frame = ctk.CTkFrame(app, fg_color="transparent")
    frame.pack(pady=5)
    for btn in satir:
        if btn == "=":
            b = olustur_buton(frame, btn, hesapla)
        else:
            b = olustur_buton(frame, btn, lambda x=btn: tikla(x))
        b.pack(side="left", padx=5)

app.mainloop()
