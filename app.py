import functions as func
from tkinter import *
from PIL import ImageTk, Image

# Description
root = Tk()
root.title("Pass-Genenerator")
root.iconbitmap(r'.\images\favicon.ico')
root.resizable(width=False, height=False)
root.geometry("248x232")

# App logo
img = ImageTk.PhotoImage(Image.open(".\images\Logo.png"))
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
                    command=lambda: func.button_click(var, result))
btn_submit.grid(row=3, column=1, columnspan=3)

# Display Password
result = Entry(root, width=30, borderwidth=2)
result.grid(row=4, column=1, columnspan=4, pady=5)

# Status bar
status = Label(root, text="Developed By Pratik, V1.1", bd=2, relief=SUNKEN, anchor=E)
status.grid(row=5, column=0, columnspan=4, sticky=W+E)

root.mainloop()