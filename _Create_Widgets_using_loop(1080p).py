# _Create_Menubar_(Hindi)(1080p)

import tkinter as tk
from tkinter import  ttk
win = tk.Tk()
win.title("Menu Bars Lecture")

menubar = tk.Menu(win)


def func():
    print("function called")
# ****************simple menu bar*****************

# menubar.add_command(label="Save", command=func)
# menubar.add_command(label="Save As", command=func)
# menubar.add_command(label="Copy", command=func)
# menubar.add_command(label="Paste", command=func)

# *************drop down menu bar*****************


main_menu = tk.Menu(win)
file_menu = tk.Menu(main_menu, tearoff=0)
file_menu.add_command(label="New File", command=func)
file_menu.add_separator()
file_menu.add_command(label="New Window", command=func)
file_menu.add_separator()
file_menu.add_command(label="Save File", command=func)

# edit menu
edit_menu = tk.Menu(main_menu, tearoff=0)
file_menu.add_separator()
edit_menu.add_command(label="Undo", command=func)
file_menu.add_separator()
edit_menu.add_command(label="Redo", command=func)

# view menu
view_menu = tk.Menu(main_menu, tearoff=0)
file_menu.add_separator()
view_menu.add_command(label="Tool Windows", command=func)
file_menu.add_separator()
view_menu.add_command(label="Recent Files", command=func)
file_menu.add_separator()
view_menu.add_command(label="Tool Bar", command=func)

# Navigaetg menu

navig_menu = tk.Menu(main_menu, tearoff=0)
file_menu.add_separator()
navig_menu.add_command(label="Last Edit Location", command=func)
file_menu.add_separator()
navig_menu.add_command(label="Class", command=func)
file_menu.add_separator()
navig_menu.add_command(label="File Structure", command=func)

# code menu

code_menu = tk.Menu(main_menu, tearoff=0)
file_menu.add_separator()
code_menu.add_command(label="Compile", command=func)
file_menu.add_separator()
code_menu.add_command(label="Reformate", command=func)
file_menu.add_separator()
code_menu.add_command(label="Insert", command=func)

# refactor menu
refactor_menu = tk.Menu(main_menu, tearoff=0)
file_menu.add_separator()
refactor_menu.add_command(label="Rename", command=func)
file_menu.add_separator()
refactor_menu.add_command(label="Safe Delete", command=func)
file_menu.add_separator()
refactor_menu.add_command(label="Extract", command=func)

# run menu
run_menu = tk.Menu(main_menu, tearoff=0)
file_menu.add_separator()
run_menu.add_command(label="Run", command=func)
file_menu.add_separator()
run_menu.add_command(label="Debug", command=func)
file_menu.add_separator()
run_menu.add_command(label="Compile", command=func)

# Tools menu

tools_menu = tk.Menu(main_menu, tearoff=0)
tools_menu.add_command(label="Task", command=func)
tools_menu.add_command(label="Template", command=func)
tools_menu.add_command(label="Console", command=func)

# VSC menu

vcs_menu = tk.Menu(main_menu, tearoff=0)
vcs_menu.add_command(label="History", command=func)
vcs_menu.add_command(label="Apply Patch", command=func)
vcs_menu.add_command(label="Sync Settings", command=func)

# Widnows menu

wind_menu = tk.Menu(main_menu, tearoff=0)
wind_menu.add_command(label="Windows Layout", command=func)
wind_menu.add_command(label="Tab Windows", command=func)
wind_menu.add_command(label="Project", command=func)

# help menu

help_menu = tk.Menu(main_menu, tearoff=0)
help_menu.add_command(label="Find Action", command=func)
help_menu.add_command(label="Help", command=func)
help_menu.add_command(label="Tip Of The Day", command=func)


# main menu

main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Edit", menu=edit_menu)
main_menu.add_cascade(label="View", menu=view_menu)
main_menu.add_cascade(label="Navigate", menu=navig_menu)
main_menu.add_cascade(label="Code", menu=code_menu)
main_menu.add_cascade(label="Refactor", menu=refactor_menu)
main_menu.add_cascade(label="Run", menu=run_menu)
main_menu.add_cascade(label="Tools", menu=tools_menu)
main_menu.add_cascade(label="VCS", menu=vcs_menu)
main_menu.add_cascade(label="Window", menu=wind_menu)
main_menu.add_cascade(label="Help", menu=help_menu)


win.configure(menu=main_menu)

win.mainloop()