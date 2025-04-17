import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("350x550")
app.title("🧮 Modern Hesap Makinesi")
app.configure(fg_color="#e7f0fd")  # Açık mavi arka plan

# Giriş alanı
giris = ctk.CTkEntry(app, font=("Helvetica", 28), justify="right", width=300, height=60,
                     corner_radius=15, border_width=2, fg_color="#ffffff", text_color="#2c3e50")
giris.pack(pady=30)

# İşlevler
def tikla(deger):
    giris.insert("end", str(deger))

def temizle():
    giris.delete(0, "end")

def hesapla(event=None):
    try:
        sonuc = eval(giris.get())
        giris.delete(0, "end")
        giris.insert(0, str(sonuc))
    except:
        giris.delete(0, "end")
        giris.insert(0, "HATA")

def geri_sil(event=None):
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

# Klavye bağlama
app.bind("<Return>", hesapla)
app.bind("<BackSpace>", geri_sil)
app.bind("<Escape>", lambda e: temizle())

# Tuş oluşturucu
def olustur_buton(parent, text, command, genislik=65, bg="#ffffff", hover="#e0e0e0", yazirenk="#333333"):
    return ctk.CTkButton(parent, text=text, font=("Helvetica", 20), width=genislik, height=65,
                         corner_radius=32, fg_color=bg, hover_color=hover,
                         text_color=yazirenk, command=command)

# Yardımcı tuşlar
yardimci_frame = ctk.CTkFrame(app, fg_color="transparent")
yardimci_frame.pack(pady=5)

yardimci_renk = "#f0c4c4"
hover_yardimci = "#e0a5a5"
yazi_yardimci = "#5a2c2c"
olustur_buton(yardimci_frame, "C", temizle, bg=yardimci_renk, hover=hover_yardimci, yazirenk=yazi_yardimci).pack(side="left", padx=5)
olustur_buton(yardimci_frame, "⌫", geri_sil, bg=yardimci_renk, hover=hover_yardimci, yazirenk=yazi_yardimci).pack(side="left", padx=5)
olustur_buton(yardimci_frame, "+/-", isaret_degistir, bg=yardimci_renk, hover=hover_yardimci, yazirenk=yazi_yardimci).pack(side="left", padx=5)
olustur_buton(yardimci_frame, "%", lambda: tikla('%'), bg=yardimci_renk, hover=hover_yardimci, yazirenk=yazi_yardimci).pack(side="left", padx=5)

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
            b = olustur_buton(frame, btn, hesapla,
                              bg="#b8e0d2", hover="#9fd6c0", yazirenk="#204d40")
        elif btn in ['+', '-', '*', '/']:
            b = olustur_buton(frame, btn, lambda x=btn: tikla(x),
                              bg="#d1d8f0", hover="#bcc6e0", yazirenk="#2f2f49")
        else:
            b = olustur_buton(frame, btn, lambda x=btn: tikla(x),
                              bg="#f7f1e5", hover="#e5dcd0", yazirenk="#3e3e3e")
        b.pack(side="left", padx=5)

app.mainloop()
