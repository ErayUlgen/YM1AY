import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("350x600")
app.title("🧮 Modern Hesap Makinesi")

# Başlangıç teması
mevcut_tema = "light"
tema_buton_text = ctk.StringVar(value="🌙 Tema")

# Renk temaları
temalar = {
    "light": {
        "bg": "#e7f0fd",
        "entry_bg": "#ffffff",
        "entry_text": "#2c3e50",
        "yardimci": ("#f0c4c4", "#e0a5a5", "#5a2c2c"),
        "operator": ("#d1d8f0", "#bcc6e0", "#2f2f49"),
        "sayi": ("#f7f1e5", "#e5dcd0", "#3e3e3e"),
        "esit": ("#b8e0d2", "#9fd6c0", "#204d40")
    },
    "dark": {
        "bg": "#1e1e2e",
        "entry_bg": "#2e2e3e",
        "entry_text": "#ffffff",
        "yardimci": ("#a55c5c", "#8c4646", "#fff"),
        "operator": ("#3b3f5c", "#2e3248", "#ffffff"),
        "sayi": ("#4a4e69", "#3e425c", "#ffffff"),
        "esit": ("#2e8b57", "#256b45", "#ffffff")
    }
}

# Tema değiştirici fonksiyon
def tema_degistir():
    global mevcut_tema
    mevcut_tema = "dark" if mevcut_tema == "light" else "light"
    ctk.set_appearance_mode(mevcut_tema)
    tema_buton_text.set("☀️ Tema" if mevcut_tema == "dark" else "🌙 Tema")
    guncelle_tema()

def guncelle_tema():
    tema = temalar[mevcut_tema]
    app.configure(fg_color=tema["bg"])
    giris.configure(fg_color=tema["entry_bg"], text_color=tema["entry_text"])

    # Butonları renklerine göre güncelle
    for btn, tur in buton_referanslari:
        renk = tema[tur]
        btn.configure(fg_color=renk[0], hover_color=renk[1], text_color=renk[2])

# Giriş alanı
giris = ctk.CTkEntry(app, font=("Helvetica", 28), justify="right", width=300, height=60,
                     corner_radius=15, border_width=2)
giris.pack(pady=15)

# Tema butonu
tema_buton = ctk.CTkButton(app, textvariable=tema_buton_text, width=150,
                           command=tema_degistir, fg_color="#cccccc", text_color="#000")
tema_buton.pack(pady=5)

# Fonksiyonlar
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

app.bind("<Return>", hesapla)
app.bind("<BackSpace>", geri_sil)
app.bind("<Escape>", lambda e: temizle())

# Tuş oluşturucu
buton_referanslari = []

def olustur_buton(parent, text, command, tur="sayi", genislik=65):
    renk = temalar[mevcut_tema][tur]
    btn = ctk.CTkButton(parent, text=text, font=("Helvetica", 20), width=genislik, height=65,
                        corner_radius=32, fg_color=renk[0], hover_color=renk[1],
                        text_color=renk[2], command=command)
    buton_referanslari.append((btn, tur))
    return btn

# Yardımcı tuşlar
yardimci_frame = ctk.CTkFrame(app, fg_color="transparent")
yardimci_frame.pack(pady=5)

olustur_buton(yardimci_frame, "C", temizle, tur="yardimci").pack(side="left", padx=5)
olustur_buton(yardimci_frame, "⌫", geri_sil, tur="yardimci").pack(side="left", padx=5)
olustur_buton(yardimci_frame, "+/-", isaret_degistir, tur="yardimci").pack(side="left", padx=5)
olustur_buton(yardimci_frame, "%", lambda: tikla('%'), tur="yardimci").pack(side="left", padx=5)

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
            b = olustur_buton(frame, btn, hesapla, tur="esit")
        elif btn in ['+', '-', '*', '/']:
            b = olustur_buton(frame, btn, lambda x=btn: tikla(x), tur="operator")
        else:
            b = olustur_buton(frame, btn, lambda x=btn: tikla(x), tur="sayi")
        b.pack(side="left", padx=5)

guncelle_tema()  # İlk tema uygulanmalı
app.mainloop()
