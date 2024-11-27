import sqlite3
from tkinter import *
import tkinter.messagebox as msg

window = Tk()
window.geometry("900x600")
reg_image = PhotoImage(file='Resgister.png')
bg_label = Label(window,image=reg_image)
bg_label.place(x=0,y=0, relwidth=1, relheight=1)
window.title("Medicine Management System")
window.config()

"""HEADING FRAME"""

TopHeadingFrame = Frame(window, width=700, bd=1)
TopHeadingFrame.pack(side=TOP)
HeadingLabel = Label(TopHeadingFrame,text="Medicine Management System - HOME",
                     font=('Helvetica',16),fg='green',bg='white')
HeadingLabel.grid(row=0,column=0,padx=5,pady=5)

"""MID FRAME"""

MidFrame = Frame(window,width = 600,bd=1)

MidFrame.pack(side=TOP)


def add():
    window.destroy()
    import add_medicine

add_btn = Button(MidFrame,text="Add Medicine", command=add,font=('Helvetica',18),fg='green',bg='skyblue')
add_btn.grid(row=0,column=1,padx=10,pady=10)

def view():
    window.destroy()
    import view_medicine

view_btn = Button(MidFrame,text="view Medicine", command=view,font=('Helvetica',18),fg='green',bg='skyblue')
view_btn.grid(row=1,column=1,padx=10,pady=10)

def search():
    window.destroy()
    import search_medicine


search_btn = Button(MidFrame,text="search Medicine", command=search,font=('Helvetica',18),fg='green',bg='skyblue')
search_btn.grid(row=2,column=1,padx=10,pady=10)

def Delete():
    window.destroy()
    import Delete_medicine

Delete_btn = Button(MidFrame,text="delete Medicine", command=Delete,font=('Helvetica',18),fg='green',bg='skyblue')
Delete_btn.grid(row=3,column=1,padx=10,pady=10)

def logout():
    window.destroy()
    import login

login_btn = Button(MidFrame,text="Logout ", command=logout,font=('Helvetica',18),fg='white',bg='green')
login_btn.grid(row=4,column=1,padx=10,pady=10)







window.mainloop()