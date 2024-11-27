from tkinter import *
import sqlite3
import tkinter.messagebox as msg

# Initialize the main window
window = Tk()
window.geometry("900x600")
window.title("Medicine Management System")

# Load background image
try:
    reg_image = PhotoImage(file='Register.png')  # Corrected filename
    bg_label = Label(window, image=reg_image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
except Exception as e:
    print(f"Error loading image: {e}")

# Create and configure database
conn = sqlite3.connect("medicine.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS userdata (
                    Name TEXT, 
                    ID TEXT, 
                    UserName TEXT, 
                    Password TEXT, 
                    Mobile TEXT, 
                    Email TEXT)""")
conn.commit()

# Define StringVars for inputs
name = StringVar()
id_var = StringVar()
username = StringVar()
password = StringVar()
mobile = StringVar()
email = StringVar()

# Heading Frame
TopHeadingFrame = Frame(window, width=700, bd=1)
TopHeadingFrame.pack(side=TOP)
HeadingLabel = Label(TopHeadingFrame, text="Medicine Management System - Register",
                     font=('Helvetica', 16), fg='green', bg='white')
HeadingLabel.grid(row=0, column=0, padx=40, pady=40)

# Middle Frame
MidFrame = Frame(window, width=500, bd=1)
MidFrame.pack(side=TOP)

# Create labels and entry fields
labels = ["Name", "ID", "User Name", "Password", "Mobile", "Email ID"]
variables = [name, id_var, username, password, mobile, email]

for i, label in enumerate(labels):
    Label(MidFrame, text=label, font=('Helvetica', 12), fg='blue', bg='white').grid(row=i, column=0, padx=10, pady=10)
    Entry(MidFrame, font=('Helvetica', 12), textvariable=variables[i]).grid(row=i, column=1, padx=10, pady=10)

def register():
    user_data = {
        "name": name.get(),
        "id": id_var.get(),
        "username": username.get(),
        "password": password.get(),
        "mobile": mobile.get(),
        "email": email.get()
    }

    for key, value in user_data.items():
        if not value.strip():
            msg.showerror('Input Error', f'{key.capitalize()} cannot be empty!')
            return

    try:
        cursor.execute(
            """INSERT INTO userdata (Name, ID, UserName, Password, Mobile, Email) VALUES (?, ?, ?, ?, ?, ?)""",
            (user_data["name"], user_data["id"], user_data["username"], user_data["password"], user_data["mobile"], user_data["email"])
        )
        conn.commit()

        if cursor.rowcount > 0:
            msg.showinfo('Confirmation', 'New user added', icon="info")
        else:
            msg.showinfo('Error', 'New user not added', icon='warning')
    except sqlite3.Error as e:
        msg.showerror('Database Error', str(e))

def login():
    window.destroy()
    import login  # Make sure login.py exists

submit_btn = Button(MidFrame, text='SUBMIT', command=register, font=('Helvetica', 12), fg='white', bg='green')
submit_btn.grid(row=len(labels), column=0, padx=5, pady=5)

Login_btn = Button(MidFrame, text="Login", command=login, font=('Helvetica', 12), fg='white', bg='green')
Login_btn.grid(row=len(labels), column=1, padx=10, pady=10)

window.mainloop()

# Close the database connection on exit
conn.close()
