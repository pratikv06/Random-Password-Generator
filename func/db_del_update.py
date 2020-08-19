import sqlite3
from tkinter import *
from tkinter import messagebox

import func.database as db
from func import *

options = []

def get_options(top):
    results = db_select.data_fetch()
    # Dropdwon options
    global options
    options = []
    for res in results:
        options.append(str(res[0]) +". "+ res[1])
    if len(options) == 0:
        res = messagebox.showinfo("Open", "No Record Found!")
        if res:
            top.destroy()
            return
    return options

def view_details(selected, userid, password, update_btn, delete_btn):
    ''' fetching data to display '''
    if selected.get() == '':
        messagebox.showwarning("Warning", "Select a option!")
        return
    # print(selected.get(), results, userid.get(), password.get(), update_btn, delete_btn)
    selected = int(selected.get().split(".")[0])
    results = db_select.data_fetch_where(selected)
    for res in results:
        if res[0] == selected:
            userid.delete(0, END)
            password.delete(0, END)
            userid['state'] = NORMAL
            password['state'] = NORMAL
            userid.insert(0, res[2])
            password.insert(0, res[3])
            update_btn['state'] = NORMAL
            delete_btn['state'] = NORMAL
            return

def data_update(selected, userid, password):
    selected = int(selected.get().split(".")[0])
    userid = userid.get()
    password = password.get()

    if len(userid) == 0 or len(password) == 0:
        title = "Warning:"
        msg = "Feild:\n"
        if len(userid) == 0:
            msg += "- Userid\n"
        if len(password) == 0:
            msg += "- Password\n"
        msg += "cannot be leaved blank"
        messagebox.showwarning(title, msg)
    else:
        conn = db.db_connect()
        c = conn.cursor()
        sql = "UPDATE user SET username=?, pwd=? WHERE userid=?"
        c.execute(sql, (userid, password, selected,))
        db.db_close(conn)
        title= "Updated"
        msg = "Updated Sucessfully"
        result = messagebox.showinfo(title, msg)


def data_delete(top, selected, drop, userid, password, update_btn, delete_btn):
    ''' Deleting record from database '''
    del1 = int(selected.get().split(".")[0])
    conn = db.db_connect()
    c = conn.cursor()
    sql = "DELETE FROM user WHERE userid=?"
    c.execute(sql, (del1,))
    db.db_close(conn)
    title= "Deleted"
    msg = "Deleted Sucessfully"
    result = messagebox.showinfo(title, msg)

    # Changing state of widgets
    userid.delete(0, END)
    password.delete(0, END)
    userid['state'] = DISABLED
    password['state'] = DISABLED
    update_btn['state'] = DISABLED
    delete_btn['state'] = DISABLED

    options = []
    if options == '':
        return
    options = get_options(top)
    drop = OptionMenu(top, selected, *options)
    drop.config(width=30)
    drop.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky=W)
    selected.set('')
    
