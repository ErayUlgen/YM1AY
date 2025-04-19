import customtkinter as ctk
import pygame

# Pygame ses başlatma
pygame.mixer.init()

# Ses kontrolü
ses_acik = True
def tus_sesi_cal():
    if ses_acik:
        try:
            pygame.mixer.Sound("click.wav").play()
        except:
            pass

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("350x600")
app.title("🧮 Modern Hesap Makinesi")

mevcut_tema = "light"
tema_buton_text = ctk.StringVar(value="🌙 Tema")
ses_buton_text = ctk.StringVar(value="🔊 Ses")

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

def tema_degistir():
    tus_sesi_cal()
    global mevcut_tema
    mevcut_tema = "dark" if mevcut_tema == "light" else "light"
    ctk.set_appearance_mode(mevcut_tema)
    tema_buton_text.set("☀️ Tema" if mevcut_tema == "dark" else "🌙 Tema")
    guncelle_tema()

def ses_degistir():
    global ses_acik
    ses_acik = not ses_acik
    ses_buton_text.set("🔇 Ses" if not ses_acik else "🔊 Ses")
    tus_sesi_cal()

def guncelle_tema():
    tema = temalar[mevcut_tema]
    app.configure(fg_color=tema["bg"])
    giris.configure(fg_color=tema["entry_bg"], text_color=tema["entry_text"])
    for btn, tur in buton_referanslari:
        renk = tema[tur]
        btn.configure(fg_color=renk[0], hover_color=renk[1], text_color=renk[2])

giris = ctk.CTkEntry(app, font=("Helvetica", 28), justify="right", width=300, height=60,
                     corner_radius=15, border_width=2)
giris.pack(pady=15)

tema_frame = ctk.CTkFrame(app, fg_color="transparent")
tema_frame.pack(pady=5)

tema_buton = ctk.CTkButton(tema_frame, textvariable=tema_buton_text, width=150,
                           command=tema_degistir, fg_color="#cccccc", text_color="#000")
tema_buton.pack(side="left", padx=5)

ses_buton = ctk.CTkButton(tema_frame, textvariable=ses_buton_text, width=150,
                          command=ses_degistir, fg_color="#cccccc", text_color="#000")
ses_buton.pack(side="left", padx=5)

def tikla(deger):
    tus_sesi_cal()
    giris.insert("end", str(deger))

def temizle():
    tus_sesi_cal()
    giris.delete(0, "end")

def hesapla(event=None):
    tus_sesi_cal()
    try:
        sonuc = eval(giris.get())
        giris.delete(0, "end")
        giris.insert(0, str(sonuc))
    except:
        giris.delete(0, "end")
        giris.insert(0, "HATA")

def geri_sil(event=None):
    tus_sesi_cal()
    giris.delete(len(giris.get()) - 1, "end")

def isaret_degistir():
    tus_sesi_cal()
    try:
        mevcut = giris.get()
        if mevcut:
            sonuc = eval(f"-1*({mevcut})")
            giris.delete(0, "end")
            giris.insert(0, str(sonuc))
    except:
        pass

# ⌨️ Klavye girişleri
def klavye_girdisi(event):
    tus = event.char
    if tus in "0123456789":
        tikla(tus)
    elif tus in "+-*/.":
        tikla(tus)
    elif tus.lower() == "c":
        temizle()
    elif tus.lower() == "n":
        isaret_degistir()
    elif tus.lower() == "m":
        tikla('%')
    elif tus.lower() == "t":
        tema_degistir()
    elif tus.lower() == "s":
        ses_degistir()
    elif tus == "=" or tus == "\r":
        hesapla()

# 🎯 Klavye kısayollarını bağla
app.bind("<Return>", hesapla)
app.bind("<BackSpace>", geri_sil)
app.bind("<Escape>", lambda e: temizle())
app.bind("<Key>", klavye_girdisi)

buton_referanslari = []

def olustur_buton(parent, text, command, tur="sayi", genislik=65):
    renk = temalar[mevcut_tema][tur]
    btn = ctk.CTkButton(parent, text=text, font=("Helvetica", 20), width=genislik, height=65,
                        corner_radius=32, fg_color=renk[0], hover_color=renk[1],
                        text_color=renk[2], command=command)
    buton_referanslari.append((btn, tur))
    return btn

yardimci_frame = ctk.CTkFrame(app, fg_color="transparent")
yardimci_frame.pack(pady=5)

olustur_buton(yardimci_frame, "C", temizle, tur="yardimci").pack(side="left", padx=5)
olustur_buton(yardimci_frame, "⌫", geri_sil, tur="yardimci").pack(side="left", padx=5)
olustur_buton(yardimci_frame, "+/-", isaret_degistir, tur="yardimci").pack(side="left", padx=5)
olustur_buton(yardimci_frame, "%", lambda: tikla('%'), tur="yardimci").pack(side="left", padx=5)

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

guncelle_tema()
app.mainloop()
