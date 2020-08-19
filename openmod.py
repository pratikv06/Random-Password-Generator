from tkinter import *

from func import *


def open_details(root):
    top = Toplevel(root)
    top.attributes('-topmost', 'true')
    top.grab_set()
    top.title("Open")
    top.iconbitmap(r'.\images\favicon.ico')
    # top.resizable(width=False, height=False)

    # Dropdown Options
    options = db_del_update.get_options(top)
    if options == '':
        return
    selected = StringVar()
    drop = OptionMenu(top, selected, *options)
    drop.config(width=30)
    drop.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky=W)
    # Search Button
    search_btn = Button(top, text="Search", width=12, 
        command= lambda: db_del_update.view_details(selected, userid, password, update_btn, delete_btn))
    search_btn.grid(row=0, column=3, padx=(1,5), pady=5)
    
    # labels
    userid_lbl = Label(top, text="User ID")
    password_lbl = Label(top, text="Password")
    labelfont = ('times', 11, 'bold')
    userid_lbl.config(font=labelfont) 
    password_lbl.config(font=labelfont) 
    userid_lbl.grid(row=1, column=0, padx=15, pady=4, sticky=W)
    password_lbl.grid(row=2, column=0, padx=15, pady=4, sticky=W)

    # Entry (disabled)
    userid = Entry(top, width=30)
    password = Entry(top, width=30)
    labelfont = ('times', 11)
    userid.config(font=labelfont, state=DISABLED) 
    password.config(font=labelfont, state=DISABLED) 
    userid.grid(row=1, column=1, columnspan=3, padx=15, pady=4, sticky=W)
    password.grid(row=2, column=1, columnspan=3, padx=15, pady=4, sticky=W)

    # Buttons
    update_btn = Button(top, text="Update", width=12, state=DISABLED,
        command=lambda: db_del_update.data_update(selected, userid, password))
    delete_btn = Button(top, text="Delete", width=12, state=DISABLED,
        command=lambda: db_del_update.data_delete(top, selected, drop, userid, password, update_btn, delete_btn))
    update_btn.grid(row=3, column=1, columnspan=3, padx=15, pady=4, sticky=W)
    delete_btn.grid(row=3, column=1, columnspan=3, padx=15, pady=4, sticky=E)






# Below functions are not in use
# Display all the deatils in scrollable
# frame of canvas in frame format

# Problem:
# update and delete button funtion
def open_toplevel(root):
    '''scrollable frame'''
    top = Toplevel(root)
    top.attributes('-topmost', 'true')
    top.grab_set()
    top.title("Open")
    top.iconbitmap(r'.\images\favicon.ico')
    # top.resizable(width=False, height=False)

    # Creating canvas for scrollable frame
    global canvas
    canvas = Canvas(top, width=400, height=500)
    canvas.pack(side=LEFT)
    # canvas.grid(row=0, column=0, sticky=W)
    scrollbar = Scrollbar(top, command=canvas.yview)
    scrollbar.pack(side=LEFT, fill='y')
    # scrollbar.grid(row=0, column=0, sticky=N+S)
    canvas.configure(yscrollcommand = scrollbar.set)
    canvas.bind('<Configure>', on_configure)
    frame = Frame(canvas)
    canvas.create_window((0,0), window=frame, anchor='nw')

    # call to database
    results = db_select.data_fetch()

    display_frame(frame, results)
    top.mainloop()  

def display_frame(frame, results):
    '''adding details in frame as frame'''
    for result in results:
        print(result[0]-1)
        # Define Frame
        msg = str(result[0]) +". "+ result[1]
        frame1 = LabelFrame(frame, text=msg, padx=20, pady=10)
        frame1.grid(row=result[0]-1)
        msg = "Userid: "+ result[2]
        Label(frame1, text=msg).grid(row=0, sticky=W)
        msg = "Password: "+ result[3]
        Label(frame1, text=msg).grid(row=1, sticky=W)
        Button(frame1, text="Update").grid(padx=15, row=0, column=1, rowspan=2)
        Button(frame1, text="Delete").grid(padx=5, row=0, column=2, rowspan=2)
        
def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox('all'))