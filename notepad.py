from tkinter import *
import sqlite3
import bcrypt
from tkinter.messagebox import *

root = Tk()
fullname = StringVar()
username = StringVar()
password = StringVar()

root.geometry('500x500+200+200')

def login():
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



Label(root,text='SIGNUP',fg='white',padx='15',pady='15',font='Helvetica,25').pack()
Label(root,text='FULLNAME',fg='white',bg='black',padx='15',pady='15',font='Helvetica,25').pack()
Entry(root,textvar=fullname,width=60,fg='black',bg='white',borderwidth=6,relief='flat').pack()
Label(root,text='USERNAME',fg='white',pady='3',bg='black',font='Helvetica').pack()
Entry(root,textvar=username,width=60,fg='black',bg='white',borderwidth=6,relief='flat').pack()
Label(root,text='PASSWORD',fg='white',pady=3,bg='black',font='Helvetica').pack()
Entry(root,textvar=password,show='*',width=60,fg='black',bg='white',borderwidth=6,relief='flat').pack()

Button(text='LOGIN',bg='blue',border=0,font='Helvetica',fg='white',padx=18,pady=10,command=login).pack()












































root.mainloop()