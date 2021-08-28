from tkinter import *
import sqlite3
import bcrypt
from UI.sign_up import signup_ui
from UI.login import login_UI
from tkinter.messagebox import *

root = Tk()
fullname = StringVar()
username = StringVar()
password = StringVar()

signup_frame = Frame(root)
signup_frame.pack()

login_frame= Frame(root)
login_frame.pack()


root.geometry('500x500+200+200')

def signup():
    db = sqlite3.connect('app.db')
    cor = db.cursor()
    # cor.execute('''CREATE TABLE users(id INTEGER PRIMARY KEY AUTOINCREMENT , fullname text NOT NULL,
    # username text NOT NULL , password text NOT NULL)''')
    hashed_password = bcrypt.hashpw(password.get().encode('utf-8'), bcrypt.gensalt())

    cor.execute('''INSERT INTO users(fullname, username, password) values(?,?,?)''',
                (fullname.get(), username.get(), hashed_password))
    db.commit()

    print(fullname.get())
    print(username.get())
    print(hashed_password)



signup_ui(signup_frame, fullname,username, password, signup )
login_UI(login_frame, fullname,username, password, signup)

root.mainloop()