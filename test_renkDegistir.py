from unittest.mock import MagicMock
import tkinter as tk

tk.Tk = MagicMock()

def test_rengi_degistir():
    pencere = tk.Tk()
    pencere.configure(bg="Blue")
    pencere.configure(bg="Red")
    assert pencere.configure.call_args[1]["bg"] == "Red"
