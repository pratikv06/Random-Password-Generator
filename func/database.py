import sqlite3

def db_connect():
    ''' Connecting to DB '''
    conn = sqlite3.connect('database.db')
    conn.isolation_level = None
    try:
        c = conn.cursor()
        sql = "CREATE TABLE user (userid INTEGER PRIMARY KEY AUTOINCREMENT, website TEXT NOT NULL, username TEXT NOT NULL, pwd TEXT NOT NULL)"
        c.execute(sql)
    except:
        pass
    return conn

def db_close(conn):
    ''' Closing the connection '''
    conn.close()