import sqlite3
from tkinter import messagebox

import func.database as db

def data_fetch():
    ''' Reading Data from DB '''
    conn = db.db_connect()
    c = conn.cursor()
    sql = 'SELECT * FROM user'
    result = c.execute(sql)
    result2 = result.fetchall()    
    db.db_close(conn)
    return result2


def data_fetch_where(selected):
    ''' Reading Data from DB '''
    conn = db.db_connect()
    c = conn.cursor()
    sql = 'SELECT * FROM user WHERE userid=?'
    result = c.execute(sql, (selected,))
    result2 = result.fetchall()    
    db.db_close(conn)
    return result2