import tkinter as tk
from tkinter import ttk
from tkcalendar import *
from collections import OrderedDict
from tkinter import messagebox
from datetime import *
import time

root = tk.Tk()
canvas_width = 1200
canvas_height = 500
root.geometry(f"{canvas_width}x{canvas_height}")

frame = ttk.Label(root)
frame.grid(row=1, column=0, sticky=tk.W)

label_frame = ttk.LabelFrame(root)
label_frame.grid()
frame1 = ttk.Label(frame)
frame1.grid()


def cal_func():

    def posted_cal_value():
        messagebox.showinfo("your date is", cal.get_date())
    top = tk.Toplevel(root)
    cal = Calendar(top, font="arial 14", selectmode="day")
    cal.grid()
    btn3Var = cal.get_date()
    btn3 = ttk.Button(top, text="From Date", command=btn3Var)
    btn3.grid()


    def unposted_cal_value():
        top = tk.Toplevel(root)
        cal = Calendar(top, font="arial 14" , selectmode="day" , year=2019 , month=1 , day=1)
        cal.grid()
        messagebox.showinfo("To Date", cal.get_date())
        return cal.get_date()
    return btn3Var

# cal_func()

txt = tk.Text(root, width=14, height=1, wrap="char")
txt.grid(row=1, column=9)
txt.insert(0.0, cal_func().get_date)


if __name__ == '__main__':
    root.mainloop()