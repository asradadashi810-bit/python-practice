# Digital clock with tkinter

import tkinter as tk
from datetime import datetime

window = tk.Tk()
window.title("ASRA")
window.geometry("500x500")
window.resizable(False, False)
window.config(bg="black")


top_rect = tk.Frame(window, bg="white", height=280)
top_rect.pack(side=tk.TOP, fill="both", expand=True)


bottom_rect = tk.Frame(window, bg="#530f97", height=220)
bottom_rect.pack(side=tk.BOTTOM, fill="both")

datetime_lbl = tk.Label(bottom_rect, font=("arial", 20, "bold"),
                         fg="#00EAFF", bg="#530f97")
datetime_lbl.pack(expand=True)


def update_clock():
    now = datetime.now()
    datetime_lbl.config(text=now.strftime("%Y/%m/%d   %H:%M:%S"))
    window.after(1000, update_clock)


update_clock()
window.mainloop()