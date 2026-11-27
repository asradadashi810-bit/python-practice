# GUI calculator with tkinter

import tkinter as tk

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error"
    return a / b

first_num = 0
operator = ""

def press_number(num):
    screen.insert(tk.END, str(num))

def press_operator(op):
    global first_num, operator
    try:
        first_num = float(screen.get())
    except ValueError:
        return
    operator = op
    screen.delete(0, tk.END)

def press_equal():
    try:
        second_num = float(screen.get())
    except ValueError:
        return

    if operator == "+":
        result = add(first_num, second_num)
    elif operator == "-":
        result = subtract(first_num, second_num)
    elif operator == "*":
        result = multiply(first_num, second_num)
    elif operator == "/":
        result = divide(first_num, second_num)
    else:
        result = second_num

    screen.delete(0, tk.END)
    screen.insert(tk.END, str(result))



def press_backspace():
    current = screen.get()
    screen.delete(0, tk.END)
    screen.insert(tk.END, current[:-1])


window = tk.Tk()
window.title("C A L C U L A T O R")
window.geometry("500x600")
window.resizable(False, False)
window.config(bg="black")

FONT = ("arial", 16)

screen= tk.Entry(window, font=("arial", 24), justify="right", bd=5)
screen.place(x=20, y=20, width=460, height=100)

btn_1 = tk.Button(window, text="1", font=FONT, command=lambda: press_number(1))
btn_1.place(x=20, y=140, width=100, height=70)

btn_2 = tk.Button(window, text="2", font=FONT, command=lambda: press_number(2))
btn_2.place(x=130, y=140, width=100, height=70)

btn_3 = tk.Button(window, text="3", font=FONT, command=lambda: press_number(3))
btn_3.place(x=240, y=140, width=100, height=70)

btn_plus = tk.Button(window, text="+", font=FONT, command=lambda: press_operator("+"))
btn_plus.place(x=350, y=140, width=100, height=70)

btn_4 = tk.Button(window, text="4", font=FONT, command=lambda: press_number(4))
btn_4.place(x=20, y=220, width=100, height=70)

btn_5 = tk.Button(window, text="5", font=FONT, command=lambda: press_number(5))
btn_5.place(x=130, y=220, width=100, height=70)

btn_6 = tk.Button(window, text="6", font=FONT, command=lambda: press_number(6))
btn_6.place(x=240, y=220, width=100, height=70)

btn_minus = tk.Button(window, text="-", font=FONT, command=lambda: press_operator("-"))
btn_minus.place(x=350, y=220, width=100, height=70)

btn_7 = tk.Button(window, text="7", font=FONT, command=lambda: press_number(7))
btn_7.place(x=20, y=300, width=100, height=70)

btn_8 = tk.Button(window, text="8", font=FONT, command=lambda: press_number(8))
btn_8.place(x=130, y=300, width=100, height=70)

btn_9 = tk.Button(window, text="9", font=FONT, command=lambda: press_number(9))
btn_9.place(x=240, y=300, width=100, height=70)

btn_multiply = tk.Button(window, text="*", font=FONT, command=lambda: press_operator("*"))
btn_multiply.place(x=350, y=300, width=100, height=70)


btn_dot = tk.Button(window, text=".", font=FONT, command=lambda: press_number("."))
btn_dot.place(x=20, y=380, width=100, height=70)

btn_backspace = tk.Button(window, text="<-", font=FONT, command=press_backspace)
btn_backspace.place(x=20, y=460, width=100, height=70)

btn_0 = tk.Button(window, text="0", font=FONT, command=lambda: press_number(0))
btn_0.place(x=130, y=380, width=100, height=70)

btn_equal = tk.Button(window, text="=", font=FONT, command=press_equal)
btn_equal.place(x=240, y=380, width=100, height=70)

btn_divide = tk.Button(window, text="/", font=FONT, command=lambda: press_operator("/"))
btn_divide.place(x=350, y=380, width=100, height=70)

window.mainloop()