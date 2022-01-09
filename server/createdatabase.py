import sqlite3

#Create DataBase

def create_table():

    conn = sqlite3.connect('dataforms.db')
    c = conn.cursor()
    c.execute(""" CREATE TABLE users (
        name TEXT,
        email PRIMARY KEY,
        sex TEXT,
        time_tiktok INTEGER,
        time_whatsapp INTEGER,
        time_twitter INTEGER,
        time_Instagram INTEGER,
        time_facebook INTEGER
        )""")
    
    conn.commit()

    conn.close()

if __name__ == '__main__':

    create_table()