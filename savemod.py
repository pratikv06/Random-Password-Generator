from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox 

from func import *

def check_for_save(root, result, var):
    print(result.get(), var.get())
    if result.get() == '' or var.get() == 0 or var.get() == 99999:
        messagebox.showwarning("Warning", "Generate Password First")
    else:
        save_toplevel(root, result.get())

def save_toplevel(root, result):
    top = Toplevel(root)
    top.attributes('-topmost', 'true')
    top.grab_set()
    top.title("Save")
    top.iconbitmap(r'.\images\favicon.ico')
    root.resizable(width=False, height=False)
    
    # App logo
    img = ImageTk.PhotoImage(Image.open(".\images\logo.png"))
    logo_panel = Label(top, image = img)
    logo_panel.grid(row=0, column=0, columnspan=4, sticky=W+E)
    
    # Module Label
    modlabel = Label(top, text = "Provide Details", font = 24)
    modlabel.grid(row=1, column=0, columnspan=4, sticky=W+E)
    
    # Label
    websitelabel = Label(top, text = "Website", anchor=W)
    useridlabel = Label(top, text = "UserID", anchor=W)
    passwordlabel = Label(top, text = "Password", anchor=W)

    # label display
    websitelabel.grid(row=2, column=0, sticky=W+E)
    useridlabel.grid(row=3, column=0, sticky=W+E)
    passwordlabel.grid(row=4, column=0, sticky=W+E)

    # Entry variable
    website_entry = Entry(top, width=30, borderwidth=2)
    userid_entry = Entry(top, width=30, borderwidth=2)
    result_entry = Entry(top, width=30, borderwidth=2)

    # Entry Display
    website_entry.grid(row=2, column=1, columnspan=2, pady=5, padx=10)
    userid_entry.grid(row=3, column=1, columnspan=2, pady=5, padx=10)
    result_entry.grid(row=4, column=1, columnspan=2, pady=5, padx=10)
    result_entry.insert(0, result)

    # Submit Button
    btn_submit = Button(top, text="Save", font="Helvetica 10 bold", padx=15,
                    command=lambda: db_insert.data_add(top, website_entry.get(), userid_entry.get(), result_entry.get()))
    btn_submit.grid(row=5, column=1, columnspan=2, padx=10, pady=(1,10), sticky=W)

    # Submit Button
    btn_submit = Button(top, text="Cancel", font="Helvetica 10 bold", padx=15, command=top.destroy)
    btn_submit.grid(row=5, column=1, columnspan=2, padx=10, pady=(1,10), sticky=E)

    top.mainloop()  