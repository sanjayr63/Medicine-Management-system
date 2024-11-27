from tkinter import *
import sqlite3
import tkinter as tk
import tkinter.messagebox as msg


# from tkinter import messagebox

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
HeadingLabel = Label(TopHeadingFrame,text="Medicine Management System - Register",
                     font=('Helvetica',16),fg='green',bg='white')
HeadingLabel.grid(row=0,column=0,padx=10,pady=10)

"""MIDDILE FRAME"""
'''NAME'''

MidFrame = Frame(window,width=500,bd=1)
MidFrame.pack(side=TOP)


conn = sqlite3.connect("medicine.db")
cursor = conn.cursor()
cursor.execute("""create table if not exists 'userdata'(Name text, ID text,UserName text, Password text,Mobile text,Email text)""")
conn.commit()


name = StringVar()
name.set("")

nameLabel = Label(MidFrame,text="Name",font=('helvetica',12),fg='blue',bg='white')
nameLabel.grid(row=0,column=0,padx=5,pady=5)

nameTextBox = Entry(MidFrame,font=('Helvitica',13),textvariable=name)
nameTextBox.grid(row=0,column=1,padx=10,pady=10)

'''ID'''



id = StringVar()
id.set("")

idLabel = Label(MidFrame,text="Id",font=("hellvetica",12),fg='blue',bg='white')
idLabel.grid(row=1,column=0,padx=10,pady=10)

idTextBox = Entry(MidFrame,font=("helvitica",12),textvariable=id)
idTextBox.grid(row=1,column=1,padx=10,pady=10)

'''userName'''

username = StringVar()
username.set("")

usernameLabel = Label(MidFrame,text="User Name",font=("hellvetica",12),fg='blue',bg='white')
usernameLabel.grid(row=2,column=0,padx=10,pady=10)

usernameTextBox = Entry(MidFrame,font=("helvitica",12),textvariable=username)
usernameTextBox.grid(row=2,column=1,padx=10,pady=10)

'''PASSWORD'''

password = StringVar()
password .set("")

passwordLabel = Label(MidFrame,text="Password ",font=("hellvetica",12),fg='blue',bg='white')
passwordLabel.grid(row=3,column=0,padx=10,pady=10)

passwordTextBox = Entry(MidFrame,font=("helvitica",12),textvariable=password )
passwordTextBox.grid(row=3,column=1,padx=10,pady=10)
'''MOBILE NO'''

mobile = StringVar()
mobile .set("")

mobileLabel = Label(MidFrame,text="Mobile ",font=("hellvetica",12),fg='blue',bg='white')
mobileLabel.grid(row=4,column=0,padx=10,pady=10)

mobileTextBox = Entry(MidFrame,font=("helvitica",12),textvariable=mobile )
mobileTextBox.grid(row=4,column=1,padx=10,pady=10)

'''EMIL ID'''

email = StringVar()
email.set('')

emailLabel = Label(MidFrame,text='Email ID',font=('helltetica',12),fg='blue',bg='white')
emailLabel.grid(row=5,column=0,padx=10,pady=10)

emailTextBox = Entry(MidFrame,font=('helltetica',12),textvariable=email)
emailTextBox.grid(row=5,column=1,padx=10,pady=10)




def register():
    # Collecting values from entry fields
    user_data = {
        "name": name.get(),
        "id": id.get(),
        "username": username.get(),
        "password": password.get(),
        "mobile": mobile.get(),
        "email": email.get()
    }

    # Validation: Check for empty fields
    for key, value in user_data.items():
        if not value.strip():  # Check if the field is empty or contains only whitespace
            msg.showerror('Input Error', f'{key.capitalize()} cannot be empty!')
            return  # Exit the function if any field is empty

    # If all fields are filled, proceed to insert into the database
    conn = sqlite3.connect("medicine.db")
    cursor = conn.cursor()
    cursor.execute(
        """insert into 'userdata' (Name, Id, UserName, Password, Mobile, Email) values (?, ?, ?, ?, ?, ?)""",
        (user_data["name"], user_data["id"], user_data["username"], user_data["password"], user_data["mobile"], user_data["email"])
    )

    conn.commit()



    if cursor.rowcount > 0:
        msg.showinfo('Confirmation', 'New user added', icon="info")
    else:
        msg.showinfo('Error', 'New user not added', icon='warning')







def login():
    window.destroy()
    import login




submit_btn =tk.Button(MidFrame,text='SUBMIT', command=register, font=('helltetica',12),fg='white',bg='green')
submit_btn.grid(row=6,column=0,padx=5,pady=5)



Login_btn = Button(MidFrame,text="Login", command=login, font=('helltetica',12),fg='white',bg='green')
Login_btn.grid(row=6,column=1,padx=10,pady=10)

window.mainloop()
