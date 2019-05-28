import tkinter as tk
from tkinter import ttk
from collections import OrderedDict
from tkinter import messagebox
from datetime import *
import time
import calendar

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

clock = tk.Label(root, font="times 16 bold",bg="White")
clock.grid(row=0, column=0, pady=5, sticky=tk.W)

# clock function


def tick():
    time_str1 = time.strftime("%H:%M:%S")
    clock.config(text=time_str1)
    clock.after(200, tick)


# value of date to display
date_str = datetime.now().strftime("%d/%m/%y")
# displaying date and time
tk.Label(frame1, text=f"{date_str}", font="gothic 12 bold").grid(row=1, column=0, sticky=tk.W)
# displaying title label
tk.Label(frame1, text="MAIN MENU", fg="black", font="gothic 12 bold").grid(row=2, column=0)

# don't uncomment it was just a practice code snippet
# can_widget = Canvas(root, width=canvas_width, height=canvas_height)
# can_widget.grid()
# can_widget.create_line(0, 200, 800, 200)
# can_widget.create_line(400, 0, 400, 400)


root.title("Pharmacy Name")
frame = ttk.Label(root)
frame.grid(row=3, column=0, sticky=tk.W)

label_frame = ttk.LabelFrame(root)
label_frame.grid(row=3, column=0)

# create FrameLabels



# creating menus


class FileZap(tk.Frame):
    def __init__(self, win):
        tk.Frame.__init__(self, root)
        self.menu = tk.Menu(win)
        self.add_acc_menu = tk.Menu(self.menu, tearoff=0)
        self.inventry_menu = tk.Menu(self.menu, tearoff=0)
        self.party_menu = tk.Menu(self.menu, tearoff=0)
        self.sale_rprt_menu = tk.Menu(self.menu, tearoff=0)
        self.open_recent_menu = tk.Menu(self.menu, tearoff=0)
        self.exit_menu = tk.Menu(self.menu, tearoff=0)

        root.configure(menu=self.menu)

        self.menu_items = OrderedDict([
            ("Add Account", self.add_acc_menu),
            ("Inventry", self.inventry_menu),
            ("Party", self.party_menu),
            ("Sale Report", self.sale_rprt_menu),
            ("Exit", self.exit_menu)
        ])

        # adding cascades to main menu
        for k, v in self.menu_items.items():
            self.menu.add_cascade(label=k, menu=v)

        # adding nested menu (sub menu) to File Menu

        self.add_acc_menu.add_cascade(label="Open Recent", menu=self.open_recent_menu)

        open_recet_lbls = ["file 1", "file 2", "file 3"]

        for index in range(len(open_recet_lbls)):
            self.open_recent_menu.add_command(label=open_recet_lbls[index])

        # adding commands to main menu casecades

        add_acc_lbls = ["Add Account", "Add Company", "Add OPD"]
        for index in range(len(add_acc_lbls)):
            self.add_acc_menu.add_command(label=add_acc_lbls[index], accelerator="Ctrl+F")

        inventry_lbls = ["Sale Invoice", "Sale Return", "Purchase Invoice"]
        for index in range(len(inventry_lbls)):
            self.inventry_menu.add_command(label=inventry_lbls[index])

        party_lbls = ["Accounts", "Party Ledger", "Item Report"]
        for index in range(len(party_lbls)):
            self.party_menu.add_command(label=party_lbls[index])

        sale_rprt_lbls = ["sale report 1", "sale report 2", "sale report 3"]
        for index in range(len(sale_rprt_lbls)):
            self.sale_rprt_menu.add_command(label=sale_rprt_lbls[index])

        self.exit_menu.add_command(label="Exit", command=exit_btn)

# creating labels


room_label = ttk.Label(text="Room [f7]")
room_label.grid(row=0, column=1, sticky=tk.W)
reg_no_label = ttk.Label(text="Reg. No.")
reg_no_label.grid(row=0, column=3, sticky=tk.W)
opd_label = ttk.Label(text="OPD No.")
opd_label.grid(row=0, column=5, sticky=tk.W)
from_date_label = ttk.Label(text="From Date")
from_date_label.grid(row=1, column=8, sticky=tk.E)
to_date_label = ttk.Label(text="To Date")
to_date_label.grid(row=2, column=8, sticky=tk.E)
party_label = ttk.Label(text="Party [f2]")
party_label.grid(row=1, column=1, sticky=tk.W)
panel_label = ttk.Label(text="Panel Name")
panel_label.grid(row=1, column=3, sticky=tk.W)
doctor_label = ttk.Label(text="Doctor")
doctor_label.grid(row=2, column=1, sticky=tk.W)
detail_label = ttk.Label(text="Details")
detail_label.grid(row=3, column=1, sticky=tk.W)
mobile_label = ttk.Label(text="Mobile No. ")
mobile_label.grid(row=2, column=3, sticky=tk.W)
rem_label = ttk.Label(text="Name [f6]")
rem_label.grid(row=3, column=3, sticky=tk.W)
stock_label = ttk.Label(text="Stock")
stock_label.grid(row=5, column=1, sticky=tk.W)
last_s_label = ttk.Label(text="Last Sale Value")
last_s_label.grid(row=5, column=2, sticky=tk.W)
exp_label = ttk.Label(text="Expiry")
exp_label.grid(row=5, column=3, sticky=tk.W)
packing_label = ttk.Label(text="Packing")
packing_label.grid(row=5, column=4, sticky=tk.W)
sel_prod_label = ttk.Label(text="Select Product [f1] ")
sel_prod_label.grid(row=7, column=1, sticky=tk.W)
batch_label = ttk.Label(text="Batch No. ")
batch_label.grid(row=7, column=2, sticky=tk.W)
qty_label = ttk.Label(text="Quantity ")
qty_label.grid(row=7, column=3, sticky=tk.W)
rate_label = ttk.Label(text="Unit Rate")
rate_label.grid(row=7, column=4, sticky=tk.W)
qty_rate_label = ttk.Label(text="Selected Qty Rate")
qty_rate_label.grid(row=7, column=5, sticky=tk.W)


# create entry box


room_var = tk.StringVar()
room_entry_ox = ttk.Entry(root, width=16, textvariable=room_var)
room_entry_ox.grid(row=0, column=2)
reg_No_var = tk.StringVar()
reg_No_entry_box = ttk.Entry(root, width=16, textvariable=reg_No_var)
reg_No_entry_box.grid(row=0, column=4)
OPD_No_var = tk.StringVar()
OPD_No_entry_box = ttk.Entry(root, width=16, textvariable=OPD_No_var)
OPD_No_entry_box.grid(row=0, column=8)
party_var = tk.StringVar()
party_entry_box = ttk.Entry(root, width=16, textvariable=party_var)
party_entry_box.grid(row=1, column=2)
panel_var = tk.StringVar()
panel_entry_box = ttk.Entry(root, width=16, textvariable=panel_var)
panel_entry_box.grid(row=1, column=4)
from_date_var = tk.StringVar()
from_date_entry_box = ttk.Entry(root, width=16, textvariable=from_date_var)
from_date_entry_box.grid(row=1, column=9)
to_date_var = tk.StringVar()
to_date_entry_box = ttk.Entry(root, width=16, textvariable=to_date_var)
to_date_entry_box.grid(row=2, column=9)
doctor_var = tk.StringVar()
doctor_entry_box = ttk.Entry(root, width=16, textvariable=doctor_var)
doctor_entry_box.grid(row=2, column=2)
detail_var = tk.StringVar()
detail_entry_box = ttk.Entry(root, width=16, textvariable=detail_var)
detail_entry_box.grid(row=3, column=2)
mobile_var = tk.StringVar()
mobile_entry_box = ttk.Entry(root, width=16, textvariable=mobile_var)
mobile_entry_box.grid(row=2, column=4)
remarks_var = tk.StringVar()
remarks_entry_box = ttk.Entry(root, width=16, textvariable=remarks_var)
remarks_entry_box.grid(row=3, column=4)
stock_var = tk.StringVar()
stock_entry_box = ttk.Entry(root, width=16, textvariable=stock_var)
stock_entry_box.grid(row=6, column=1)
last_S_var = tk.StringVar()
last_S_entry_box = ttk.Entry(root, width=16, textvariable=last_S_var)
last_S_entry_box.grid(row=6, column=2)
exp_var = tk.StringVar()
exp_entry_box = ttk.Entry(root, width=16, textvariable=exp_var)
exp_entry_box.grid(row=6, column=3)
pack_var = tk.StringVar()
pack_entry_box = ttk.Entry(root, width=16, textvariable=pack_var)
pack_entry_box.grid(row=6, column=4)
sel_prod_var = tk.StringVar()
sel_entry_box = ttk.Entry(root, width=16, textvariable=sel_prod_var)
sel_entry_box.grid(row=8, column=1, padx=3)
sel_entry_box.focus()   # to bring the cursor to the desired point when a root is opened focus() method is used
batch_var = tk.StringVar()
batch_entry_box = ttk.Entry(root, width=16, textvariable=batch_var)
batch_entry_box.grid(row=8, column=2, padx=3)
qty__var = tk.StringVar()
qty_entry_box = ttk.Entry(root, width=16, textvariable=qty__var)
qty_entry_box.grid(row=8, column=3, padx=3)
rate_var = tk.StringVar()
rate_entry_box = ttk.Entry(root, width=16, textvariable=rate_var)
rate_entry_box.grid(row=8, column=4, padx=3)
qty_rate_var = tk.StringVar()
qty_rate_entry_box = ttk.Entry(root, width=16, textvariable=qty_rate_var)
qty_rate_entry_box.grid(row=8, column=5, padx=3)


def action():
    print("function called")


add_acc_btn = ttk.Button(root, text="Add Account", command=action)
add_acc_btn.grid(row=5, column=0, sticky=tk.W)

cash_pmnt_btn = ttk.Button(root, text="Cash Payment", command=action)
cash_pmnt_btn.grid(row=6, column=0, sticky=tk.W)

cash_rcpt_btn = ttk.Button(root, text="Cash Receipt", command=action)
cash_rcpt_btn.grid(row=7, column=0, sticky=tk.W)

product_btn = ttk.Button(root, text="Product History", command=action)
product_btn.grid(row=8, column=0, sticky=tk.W)

sale_inv_btn = ttk.Button(root, text="Sale Invoice", command=action)
sale_inv_btn.grid(row=9, column=0, sticky=tk.W)

sale_ret_btn = ttk.Button(root, text="Sale Return", command=action)
sale_ret_btn.grid(row=10, column=0, sticky=tk.W)

purch_inv_btn = ttk.Button(root, text="Purchase Invoice", command=action)
purch_inv_btn.grid(row=11, column=0, sticky=tk.W)

purch_ret_btn = ttk.Button(root, text="Purchase Return", command=action)
purch_ret_btn.grid(row=12, column=0, sticky=tk.W)


def pstd_btn_func(event=""):
    if messagebox.showinfo("Open Posted", "Open Posted.?"):
        print("Posted Opened")


root.bind("<Alt-p>", pstd_btn_func)
posted_btn = ttk.Button(root, text="Posted", command=pstd_btn_func)
posted_btn.grid(row=1, column=10, sticky=tk.W)


def unpstd_btn_func(event=""):
    if messagebox.showinfo("Open Unposted", "Open Unposted.?"):
        print("Unposted Opened")


root.bind("<Alt-u>", unpstd_btn_func)
unposted_btn = ttk.Button(root, text="UnPosted", command=unpstd_btn_func)
unposted_btn.grid(row=2, column=10, sticky=tk.E)

# command line buttons


def add_btn_func(event=""):
    if messagebox.askyesno("Add New Invoice" , "Do You Want to Add New Invoice"):
        print("new invoice added")


root.bind("<Alt-a>", add_btn_func)
add_btn = ttk.Button(root, text="Add", command=add_btn_func)
add_btn.grid(row=20, column=1)


def save_btn_func(event=""):
    if messagebox.askyesno("Save File" , "Do You Want to Save the File ?"):
        print("File is Saved")


root.bind('<Alt-s>', save_btn_func)
save_btn = ttk.Button(root , text="Save" , command=save_btn_func)
save_btn.grid(row=20, column=2)


def cancel_btn_func(event=""):
    print("cancelled")


root.bind("<Alt-c>", cancel_btn_func)
cancel_btn = ttk.Button(root, text="Cancel", command=cancel_btn_func)
cancel_btn.grid(row=20, column=3)


def exit_gui(event=""):
    if messagebox.askyesno("Close the Programme?" , "Do Want to Close the Application"):
        return exit()


root.bind('<Alt-x>', exit_gui)
exit_btn = ttk.Button(root, text="Exit", command=exit_gui)
exit_btn.grid(row=20, column=4)


file_zap = FileZap(root)
tick()
if __name__ == '__main__':
    root.mainloop()