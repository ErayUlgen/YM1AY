import tkinter as tk

# Hesap makinesi işlemlerini yapan fonksiyon
def hesapla():
    try:
        sonuc = eval(giris.get())
        cikti_label.config(text=f"Sonuç: {sonuc}")
    except:
        cikti_label.config(text="Hata! Geçersiz ifade.")

# Temel arayüz oluşturma
pencere = tk.Tk()
pencere.title("Hesap Makinesi")
pencere.geometry("300x200")
pencere.resizable(False, False)

# Giriş alanı
giris = tk.Entry(pencere, font=("Arial", 16), justify="right")
giris.pack(padx=10, pady=10, fill="x")

# Hesapla butonu
hesapla_btn = tk.Button(pencere, text="Hesapla", font=("Arial", 14), command=hesapla)
hesapla_btn.pack(pady=5)

# Sonuç etiketi
cikti_label = tk.Label(pencere, text="Sonuç: ", font=("Arial", 14))
cikti_label.pack(pady=10)

# Ana döngü
pencere.mainloop()
