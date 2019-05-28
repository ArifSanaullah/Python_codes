# _Tabbed_Control_Widget_(Hindi_)(1080p)

import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("Tabbed_Control_Widget")
nb = ttk.Notebook(root)
page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)
nb.add(page1, text="Page One")
nb.add(page2, text="Page Two")
nb.grid(row=0, column=0)
nb.pack(expand=True, fill="both")

# labels creating
label1 = ttk.Label(page1, text="this is label one")
label1.grid(row=0, column=0)
label2 = ttk.Label(page2, text="this is label two")
label2.grid(row=0, column=0)


# entry boxes
entry1 = ttk.Entry(page1, width=16)
entry1.grid(row=0, column=1)

entry2 = ttk.Entry(page2, width=16)
entry2.grid(row=0, column=1)



root.mainloop()