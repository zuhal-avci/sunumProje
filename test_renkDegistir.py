import tkinter as tk

def test_rengi_degistir():
    # Tkinter penceresi oluştur
    pencere = tk.Tk()
    pencere.configure(bg="Blue")

    # Arka plan rengini değiştir
    pencere.configure(bg="Red")

    # Test: Arka plan rengi değişti mi?
    assert pencere["bg"] == "Red"
