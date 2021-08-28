from tkinter import *


def login_UI(login_frame, fullname,username, password, login):
    Label(login_frame, text='LOGIN', fg='white', padx='15', pady='15', font='Helvetica,25').pack()
    Label(login_frame, text='FULLNAME', fg='white', bg='black', padx='15', pady='15', font='Helvetica,25').pack()
    Entry(login_frame, textvar=fullname, width=60, fg='black', bg='white', borderwidth=6, relief='flat').pack()
    Label(login_frame, text='USERNAME', fg='white', pady='3', bg='black', font='Helvetica').pack()
    Entry(login_frame, textvar=username, width=60, fg='black', bg='white', borderwidth=6, relief='flat').pack()
    Label(login_frame, text='PASSWORD', fg='white', pady=3, bg='black', font='Helvetica').pack()
    Entry(login_frame, textvar=password, show='*', width=60, fg='black', bg='white', borderwidth=6,
          relief='flat').pack()

    Button(text='LOGIN', bg='orange', border=0, font='Helvetica', fg='white', padx=18, pady=10, command= login).pack()