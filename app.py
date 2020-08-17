from tkinter import *
from PIL import ImageTk, Image


# import func.genpass as gp
from func import genpass as gp, about, clear

# Description
root = Tk()
root.title("Pass-Genenerator")
root.iconbitmap(r'.\images\favicon.ico')
root.resizable(width=False, height=False)
root.geometry("248x253")


# Menu Bar
menubar = Menu(root) 
# option1
file = Menu(menubar, tearoff=0)   
file.add_command(label="Open")  
file.add_command(label="Save") 
file.add_command(label="Clear", command=lambda: clear.clear_radio_pass(result, var))    
file.add_separator()  
file.add_command(label="Close", command=root.quit)  
menubar.add_cascade(label="File", menu=file) 
# option2
backup = Menu(menubar, tearoff=0)
# sub-option2.1
import1 = Menu(backup)
import1.add_command(label="Database")  
import1.add_command(label="SQL")  
import1.add_command(label="Text") 
backup.add_cascade(label="Import as...", menu=import1, underline=0) 
# sub-option2.2
export = Menu(backup)
export.add_command(label="Database")  
export.add_command(label="SQL")  
export.add_command(label="Text")  
backup.add_cascade(label="Export as...", menu=export, underline=0)
menubar.add_cascade(label="Backup", menu=backup)
# option3
menubar.add_cascade(label="About", command=about.about_app)
root.config(menu=menubar)
# Menu Bar End

# App logo
img = ImageTk.PhotoImage(Image.open(".\images\logo.png"))
logo_panel = Label(root, image = img)
logo_panel.grid(row=0, column=0, columnspan=4, sticky=W+E)

# App Label
applabel = Label(root, text = "Pass-Generator", font = 24)
applabel.grid(row=1, column=0, columnspan=4, sticky=W+E)

# Defining Radio
var = IntVar()
btn_poor = Radiobutton(root, text = "Poor", variable = var, value = 1, anchor=W)
btn_avg = Radiobutton(root, text = "Average", variable = var, value = 2, anchor=W)
btn_strong = Radiobutton(root, text = "Strong", variable = var, value = 3, anchor=W)

# Display Radio
btn_poor.grid(row=2, column=1, padx=10)
btn_avg.grid(row=2, column=2, padx=10)
btn_strong.grid(row=2, column=3, padx=10)

# Submit Button
btn_submit = Button(root, text="Generate", font="Helvetica 10 bold", padx=15, 
                    command=lambda: gp.gen_pass_btn(var, result))
btn_submit.grid(row=3, column=1, columnspan=3)

# Display Password
result = Entry(root, width=30, borderwidth=2)
result.grid(row=4, column=1, columnspan=4, pady=5)

# Status bar
status = Label(root, text="Version 1.0.3", bd=2, relief=SUNKEN, anchor=E)
status.grid(row=5, column=0, columnspan=4, sticky=W+E)

root.mainloop()