import tkinter as tk

def test_button():
    # Tkinter penceresi oluştur
    pencere = tk.Tk()
    pencere.geometry("300x200")
    
    # Buton oluştur
    def rengi_degistir():
        pencere.configure(bg="Red")
    
    buton = tk.Button(pencere, text="Rengi Değiştir", command=rengi_degistir)
    buton.pack()

    # Test: Butonun metni doğru mu?
    assert buton.cget("text") == "Rengi Değiştir"

    # Pencereyi yok et
    pencere.destroy()

# Testi çalıştır
if __name__ == "__main__":
    test_button()
    print("Test başarılı!")
