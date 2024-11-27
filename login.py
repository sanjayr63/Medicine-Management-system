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
HeadingLabel = Label(TopHeadingFrame,text="Medicine Management System - Login",
                     font=('Helvetica',16),fg='green',bg='white')
HeadingLabel.grid(row=0,column=0,padx=5,pady=5)

"""MID FRAME"""

MidFrame = Frame(window,width = 600,bd=1)

MidFrame.pack(side=TOP)

username = StringVar()
username.set('')

usernameLabel = Label(MidFrame,text="Username",font=("hellvetica",12),fg='blue',bg='white')
usernameLabel.grid(row=0,column=0,padx=10,pady=10)

usernameTextBox = Entry(MidFrame,font=('Helvetica',12),textvariable=username)
usernameTextBox.grid(row=0,column=1,padx=10,pady=10)

password = StringVar()
password.set("")

passwordLabel = Label(MidFrame,text="Password ",font=("hellvetica",12),fg='blue',bg='white')
passwordLabel.grid(row=1,column=0,padx=10,pady=10)

passwordTextBox = Entry(MidFrame,font=('Helvetica',12),textvariable=password)
passwordTextBox.grid(row=1,column=1,padx=10,pady=10)

def register():
    window.destroy()
    import  register

def login():

    user_data = {
        "username": username.get(),
        "password": password.get(),
    }
    for key, value in user_data.items():
        if not value.strip():  # Check if the field is empty or contains only whitespace
            msg.showerror('Input Error', f'{key.capitalize()} cannot be empty!')
            return  # Exit the function if any field is empty


    conn = sqlite3.connect('medicine.db')
    cursor = conn.cursor()
    cursor.execute("""select * from 'userdata' where UserName = ? and Password = ?  """,(username.get(),password.get()))


    if len(list(cursor.fetchall())) >0:
        msg.showinfo('Login confirmation', 'login successful',icon='info')

        window.destroy()
        import Home

    else:
        msg.showinfo('login error','user not defined',icon='warning')

submit_btn = Button(MidFrame,text='Register', command=register, font=('helltetica',12),fg='white',bg='green')
submit_btn.grid(row=3,column=1,padx=5,pady=5)

NotUserLabel = Label(MidFrame,text='Already a  user?',font=('helltetica',12),fg='white',bg='red')
NotUserLabel.grid(row=3,column=0,padx=10,pady=10)

Login_btn = Button(MidFrame,text="Login", command=login, font=('helltetica',12),fg='white',bg='green')
Login_btn.grid(row=2,column=1,padx=10,pady=10)


window.mainloop()