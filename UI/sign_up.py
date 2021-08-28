from tkinter import *


def signup_ui(signup_frame, fullname,username, password, command):
    Label(signup_frame, text='SIGNUP', fg='white', padx='15', pady='15', font='Helvetica,25').pack()
    Label(signup_frame, text='FULLNAME', fg='white', bg='black', padx='15', pady='15', font='Helvetica,25').pack()
    Entry(signup_frame, textvar=fullname, width=60, fg='black', bg='white', borderwidth=6, relief='flat').pack()
    Label(signup_frame, text='USERNAME', fg='white', pady='3', bg='black', font='Helvetica').pack()
    Entry(signup_frame, textvar=username, width=60, fg='black', bg='white', borderwidth=6, relief='flat').pack()
    Label(signup_frame, text='PASSWORD', fg='white', pady=3, bg='black', font='Helvetica').pack()
    Entry(signup_frame, textvar=password, show='*', width=60, fg='black', bg='white', borderwidth=6,
          relief='flat').pack()

    Button(text='SIGNUP', bg='blue', border=0, font='Helvetica', fg='white', padx=18, pady=10, command=command).pack()