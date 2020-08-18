import sqlite3
from tkinter import messagebox

import func.database as db

def data_add(top, website, userid, password):
    ''' Adding data to DB '''
    if len(website) == 0 or len(userid) == 0 or len(password) == 0:
        title = "Warning:"
        msg = "Feild:\n"
        if len(website) == 0:
            msg += "- Website\n"
        if len(userid) == 0:
            msg += "- Userid\n"
        if len(password) == 0:
            msg += "- Password\n"
        msg += "cannot be leaved blank"
        messagebox.showwarning(title, msg)
    else:
        conn = db.db_connect()
        c = conn.cursor()
        sql = "INSERT INTO user (website, username, pwd) VALUES (?, ?, ?)"
        c.execute(sql, (website, userid, password,))
        db.db_close(conn)
        title= "Saved"
        msg = "Saved Sucessfully"
        result = messagebox.showinfo(title, msg)
        if result:
            top.destroy()