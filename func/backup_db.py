import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile, askopenfilename
import json

import func.database as db
from func import *


def imp_json():
    ''' Importing as JSON '''
    print("Imported...")
    file_type = [('Json Files', '*.json')]
    filename = askopenfilename(filetypes = file_type, defaultextension = file_type)
    with open(filename) as f:
        data = json.load(f)
    for k, v in data.items():
        db_insert.add_data1(v[0], v[1], v[2])
    messagebox.showinfo("Backup", "Record Imported Successfully!!!") 

def exp_json():
    ''' Exporting as JSON '''
    data = {}
    results = db_select.data_fetch()
    for r in results:
        data[r[0]] = [r[1], r[2], r[3]]
    data_json = json.dumps(data)
    file_type = [('Json Files', '*.json')]
    filename = asksaveasfile(filetypes = file_type, defaultextension = file_type)
    with open(filename.name, 'w') as f:
        json.dump(data, f, indent = 4, sort_keys=True)
    messagebox.showinfo("Backup", "Record Exported Successfully!!!")        