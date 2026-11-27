# Simple paint app with tkinter (needs Pillow: pip install pillow)
# Saving the image as PNG also needs Ghostscript to be installed.

import tkinter as tk
from tkinter.colorchooser import askcolor
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk

def get_color():
    c = askcolor()
    myColor.set(c[1])

def active(event):
    global last_x,last_y
    x=event.x
    y=event.y
    last_x=x
    last_y=y

def paint(event):
    global last_x,last_y
    x=event.x
    y=event.y
    s = sc.get()
    color=myColor.get()
    cw.create_line(x,y,last_x,last_y,width=s,fill=color,capstyle="round",joinstyle="round")
    last_x=x
    last_y=y

def save_cmd():
    ext = [ ("PNG files","*.png") , ("All files","*.*") ]
    path = asksaveasfilename(filetypes=ext,defaultextension=".png")
    if not path:
        return
    cw.postscript(file="temp.eps")
    img = Image.open("temp.eps")
    img.save(path)
    showinfo("SAVE", "Saved!")

def open_cmd():
    ext = [ ("Image files","*.png;*.jpg;*.jpeg") , ("All files","*.*") ]
    path = askopenfilename(filetypes=ext,defaultextension=".png")
    if not path:
        return
    img = Image.open(path)
    img = img.resize((580,500))
    photo = ImageTk.PhotoImage(img)
    cw.image = photo
    cw.create_image(0,0,anchor="nw",image=photo)


window = tk.Tk()
window.title("PAINT")
window.geometry("600x600")
window.resizable(False, False)

cw = tk.Canvas(window,bg="white",bd=5,relief="solid")
cw.place(x=10,y=10,width=580,height=500)

last_x,last_y = 0,0

cw.bind("<1>",active)
cw.bind("<B1-Motion>",paint)

myColor=tk.StringVar()
myColor.set("black")
sc = tk.Scale(window,from_=1,to=20,orient="horizontal")
sc.place(x=10,y=530)

btn_color = tk.Button(window,text="COLOR",command=get_color)
btn_color.place(x=150,y=550)

btn_open = tk.Button(window, text="OPEN", command=open_cmd)
btn_open.place(x=250, y=550)

btn_save = tk.Button(window, text="SAVE", command=save_cmd)
btn_save.place(x=350, y=550)

window.mainloop()