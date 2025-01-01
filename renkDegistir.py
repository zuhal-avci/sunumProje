import tkinter as tk

# Pencere oluştur
pencere = tk.Tk()
pencere.title("Arka Plan Rengi")
pencere.geometry("300x200")

# Arka plan rengini değiştiren fonksiyon
def rengi_degistir():
    pencere.configure(bg="Red")

# Tek bir buton oluştur
buton = tk.Button(pencere, text="Rengi Değiştir", command=rengi_degistir)
buton.pack(pady=20)

# Pencereyi çalıştır
pencere.mainloop()
