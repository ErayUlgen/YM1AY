import customtkinter as ctk
import pygame
import math

# Ses başlatma
pygame.mixer.init()
ses_durum = True
memory = None
bilimsel_aktif = False

# Tema ayarları
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("350x700")
app.title("🧲 Modern Hesap Makinesi")

mevcut_tema_index = 0
tema_buton_text = ctk.StringVar(value="🌙 Tema")
ses_buton_text = ctk.StringVar(value="🔊 Ses")
bilimsel_buton_text = ctk.StringVar(value="🔬 Bilimsel")
hafiza_text = ctk.StringVar(value="")

temalar = [
    {
        "ad": "light",
        "bg": "#e7f0fd",
        "entry_bg": "#ffffff",
        "entry_text": "#2c3e50",
        "yardimci": ("#f0c4c4", "#e0a5a5", "#5a2c2c"),
        "operator": ("#d1d8f0", "#bcc6e0", "#2f2f49"),
        "sayi": ("#f7f1e5", "#e5dcd0", "#3e3e3e"),
        "esit": ("#b8e0d2", "#9fd6c0", "#204d40"),
        "ikon": "🌙"
    },
    {
        "ad": "dark",
        "bg": "#1e1e2e",
        "entry_bg": "#2e2e3e",
        "entry_text": "#ffffff",
        "yardimci": ("#a55c5c", "#8c4646", "#fff"),
        "operator": ("#3b3f5c", "#2e3248", "#ffffff"),
        "sayi": ("#4a4e69", "#3e425c", "#ffffff"),
        "esit": ("#2e8b57", "#256b45", "#ffffff"),
        "ikon": "☀️"
    },
    {
        "ad": "blue",
        "bg": "#cce7ff",
        "entry_bg": "#ffffff",
        "entry_text": "#003366",
        "yardimci": ("#99ccff", "#80bfff", "#002244"),
        "operator": ("#66b2ff", "#3399ff", "#001122"),
        "sayi": ("#b3d9ff", "#99ccff", "#001122"),
        "esit": ("#3399ff", "#007acc", "#ffffff"),
        "ikon": "🧿"
    },
    {
        "ad": "green",
        "bg": "#e0f2f1",
        "entry_bg": "#ffffff",
        "entry_text": "#004d40",
        "yardimci": ("#b2dfdb", "#80cbc4", "#00251a"),
        "operator": ("#a5d6a7", "#81c784", "#003300"),
        "sayi": ("#c8e6c9", "#a5d6a7", "#003300"),
        "esit": ("#4caf50", "#388e3c", "#ffffff"),
        "ikon": "🌿"
    }
]

def tus_sesi_cal():
    if ses_durum:
        try:
            pygame.mixer.Sound("click.wav").play()
        except:
            pass

def tema_degistir():
    global mevcut_tema_index
    tus_sesi_cal()
    mevcut_tema_index = (mevcut_tema_index + 1) % len(temalar)
    secilen = temalar[mevcut_tema_index]
    ctk.set_appearance_mode(secilen["ad"] if secilen["ad"] in ["light", "dark"] else "light")
    tema_buton_text.set(f"{secilen['ikon']} Tema")
    guncelle_tema()

def ses_degistir():
    global ses_durum
    ses_durum = not ses_durum
    tus_sesi_cal()
    ses_buton_text.set("🔇 Ses" if not ses_durum else "🔊 Ses")

def guncelle_tema():
    tema = temalar[mevcut_tema_index]
    app.configure(fg_color=tema["bg"])
    giris.configure(fg_color=tema["entry_bg"], text_color=tema["entry_text"])
    hafiza_label.configure(text_color=tema["entry_text"])
    for btn, tur in buton_referanslari:
        renk = tema[tur]
        btn.configure(fg_color=renk[0], hover_color=renk[1], text_color=renk[2])

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

def geri_sil():
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

def hafizaya_ekle():
    global memory
    tus_sesi_cal()
    try:
        memory = eval(giris.get())
        hafiza_text.set(f"Hafıza: {memory}")
    except:
        memory = None
        hafiza_text.set("")

def hafizayi_getir():
    tus_sesi_cal()
    if memory is not None:
        giris.insert("end", str(memory))

def hafizayi_temizle():
    global memory
    tus_sesi_cal()
    memory = None
    hafiza_text.set("")

def karekok():
    tus_sesi_cal()
    try:
        ifade = giris.get()
        if ifade.strip() == "":
            raise ValueError("Boş giriş")
        deger = eval(ifade)
        if deger < 0:
            raise ValueError("Negatif sayı")
        sonuc = math.sqrt(deger)
        giris.delete(0, "end")
        giris.insert(0, str(sonuc))
    except:
        giris.delete(0, "end")
        giris.insert(0, "HATA")
def pi_ekle():
    tus_sesi_cal()
    giris.insert("end", str(math.pi))

def e_ekle():
    tus_sesi_cal()
    giris.insert("end", str(math.e))

def us_alma():
    tus_sesi_cal()
    giris.insert("end", "**")
def log_al():
    tus_sesi_cal()
    try:
        ifade = giris.get()
        if ifade.strip() == "":
            raise ValueError("Boş giriş")
        deger = eval(ifade)
        if deger <= 0:
            raise ValueError("Negatif veya sıfır")
        sonuc = math.log10(deger)
        giris.delete(0, "end")
        giris.insert(0, str(sonuc))
    except:
        giris.delete(0, "end")
        giris.insert(0, "HATA")

def ln_al():
    tus_sesi_cal()
    try:
        ifade = giris.get()
        if ifade.strip() == "":
            raise ValueError("Boş giriş")
        deger = eval(ifade)
        if deger <= 0:
            raise ValueError("Negatif veya sıfır")
        sonuc = math.log(deger)
        giris.delete(0, "end")
        giris.insert(0, str(sonuc))
    except:
        giris.delete(0, "end")
        giris.insert(0, "HATA")




def faktoriyel():
    tus_sesi_cal()
    try:
        ifade = giris.get()
        if ifade.strip() == "":
            raise ValueError("Boş giriş")
        deger = int(eval(ifade))
        if deger < 0:
            raise ValueError("Negatif sayı")
        sonuc = math.factorial(deger)
        giris.delete(0, "end")
        giris.insert(0, str(sonuc))
    except:
        giris.delete(0, "end")
        giris.insert(0, "HATA")

def bilimsel_mod_degistir():
    global bilimsel_aktif
    tus_sesi_cal()
    bilimsel_aktif = not bilimsel_aktif
    if bilimsel_aktif:
        bilimsel_frame.pack(pady=5)
        bilimsel_buton_text.set("🧮 Kapat")
        app.geometry("350x760")
    else:
        bilimsel_frame.pack_forget()
        bilimsel_buton_text.set("🔬 Bilimsel")
        app.geometry("350x700")

def klavye_girdisi(event):
    tus = event.char
    if tus in "0123456789":
        tikla(tus)
    elif tus == ".":
        tikla(".")
    elif tus in "+-*/":
        tikla(tus)
    elif tus.lower() == "c":
        temizle()
    elif tus.lower() == "n":
        isaret_degistir()
    elif tus.lower() == "m":
        hafizaya_ekle()
    elif tus.lower() == "r":
        hafizayi_getir()
    elif tus.lower() == "x":
        hafizayi_temizle()
    elif tus.lower() == "t":
        tema_degistir()
    elif tus.lower() == "s":
        ses_degistir()

app.bind("<Return>", hesapla)
app.bind("<BackSpace>", lambda e: geri_sil())
app.bind("<Escape>", lambda e: temizle())
app.bind("<Key>", klavye_girdisi)

giris = ctk.CTkEntry(app, font=("Helvetica", 28), justify="right", width=300, height=60, corner_radius=15, border_width=2)
giris.pack(pady=10)

hafiza_label = ctk.CTkLabel(app, textvariable=hafiza_text, font=("Helvetica", 14))
hafiza_label.pack()

ust_frame = ctk.CTkFrame(app, fg_color="transparent")
ust_frame.pack(pady=5)

ctk.CTkButton(ust_frame, textvariable=tema_buton_text, width=100, command=tema_degistir).pack(side="left", padx=3)
ctk.CTkButton(ust_frame, textvariable=ses_buton_text, width=100, command=ses_degistir).pack(side="left", padx=3)
ctk.CTkButton(ust_frame, textvariable=bilimsel_buton_text, width=100, command=bilimsel_mod_degistir).pack(side="left", padx=3)

buton_referanslari = []

def olustur_buton(parent, text, command, tur="sayi", genislik=65):
    renk = temalar[mevcut_tema_index][tur]
    btn = ctk.CTkButton(parent, text=text, font=("Helvetica", 20), width=genislik, height=65,
                        corner_radius=32, fg_color=renk[0], hover_color=renk[1],
                        text_color=renk[2], command=command)

    def on_press(event):
        btn.configure(fg_color=renk[1])
        btn.configure(width=genislik - 5, height=60)

    def on_release(event):
        btn.configure(fg_color=renk[0])
        btn.configure(width=genislik, height=65)

    btn.bind("<ButtonPress-1>", on_press)
    btn.bind("<ButtonRelease-1>", on_release)
    buton_referanslari.append((btn, tur))
    return btn

# Yardımcı Butonlar
yardimci_frame = ctk.CTkFrame(app, fg_color="transparent")
yardimci_frame.pack(pady=5)

olustur_buton(yardimci_frame, "C", temizle, tur="yardimci").pack(side="left", padx=5)
olustur_buton(yardimci_frame, "⌫", geri_sil, tur="yardimci").pack(side="left", padx=5)
olustur_buton(yardimci_frame, "+/-", isaret_degistir, tur="yardimci").pack(side="left", padx=5)
olustur_buton(yardimci_frame, "%", lambda: tikla('%'), tur="yardimci").pack(side="left", padx=5)

hafiza_frame = ctk.CTkFrame(app, fg_color="transparent")
hafiza_frame.pack(pady=5)

olustur_buton(hafiza_frame, "M+", hafizaya_ekle, tur="yardimci").pack(side="left", padx=5)
olustur_buton(hafiza_frame, "MR", hafizayi_getir, tur="yardimci").pack(side="left", padx=5)
olustur_buton(hafiza_frame, "MC", hafizayi_temizle, tur="yardimci").pack(side="left", padx=5)

# Bilimsel Frame (BAŞLANGIÇTA GÖRÜNMEYECEK)
bilimsel_frame = ctk.CTkFrame(app, fg_color="transparent")

# Satır 1
olustur_buton(bilimsel_frame, "√", karekok, tur="operator").grid(row=0, column=0, padx=5, pady=5)
olustur_buton(bilimsel_frame, "n!", faktoriyel, tur="operator").grid(row=0, column=1, padx=5, pady=5)
olustur_buton(bilimsel_frame, "^", us_alma, tur="operator").grid(row=0, column=2, padx=5, pady=5)

# Satır 2
olustur_buton(bilimsel_frame, "π", pi_ekle, tur="operator").grid(row=1, column=0, padx=5, pady=5)
olustur_buton(bilimsel_frame, "e", e_ekle, tur="operator").grid(row=1, column=1, padx=5, pady=5)


# Satır 3 (Yeni log ve ln)
olustur_buton(bilimsel_frame, "log", log_al, tur="operator").grid(row=2, column=0, padx=5, pady=5)
olustur_buton(bilimsel_frame, "ln", ln_al, tur="operator").grid(row=2, column=1, padx=5, pady=5)







# Sayı ve İşlem Tuşları
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
