# from tkinter import *
# import sqlite3
# import tkinter.messagebox as msg
#
# window = Tk()
# window.geometry("900x600")
# reg_image = PhotoImage(file='registerbg.png')
# bg_label = Label(window,image=reg_image)
# bg_label.place(x=0,y=0, relwidth=1, relheight=1)
# window.title("Medicine Management System")
# window.config()
#
# """HEADING FRAME"""
#
# TopHeadingFrame = Frame(window, width=700, bd=1)
# TopHeadingFrame.pack(side=TOP)
# HeadingLabel = Label(TopHeadingFrame,text="Medicine Management System - Search Medicine",
#                      font=('Helvetica',16),fg='green',bg='white')
# HeadingLabel.grid(row=0,column=0,padx=5,pady=5)
#
# MidFrame = Frame(window, width=500, bd=1)
# MidFrame.pack(side=TOP)
#
# medicine_name = StringVar()
# medicine_name.set("")
#
# medicine_nameLabel = Label(MidFrame, text="Medicine Name", font=('helvetica', 12), fg='blue', bg='white')
# medicine_nameLabel.grid(row=0, column=0, padx=5, pady=5)
#
# medicine_nameTextBox = Entry(MidFrame, font=('Helvitica', 13), textvariable=medicine_name)
# medicine_nameTextBox.grid(row=0, column=1, padx=10, pady=10)
#
#
# def search():
#     conn = sqlite3.connect("medicine.db")
#     cursor = conn.cursor()
#     cursor.execute("select * from 'medicine' where MedicineName = ?", ([medicine_name.get()]))
#     conn.commit()
#     tv = cursor.fetchall()
#
#     # for i in tv.get_children():
#     #     tv.delete(i)
#
#     if cursor.rowcount > 0:
#         msg.showinfo('SEARCH MEDICINE', ' Medicine search', icon="info")
#     else:
#         msg.showinfo('Error', ' Medicine not found', icon='warning')
#
#
# search_btn = Button(MidFrame, text="Search", command=search, font=('helltetica', 12), fg='white', bg='green')
# search_btn.grid(row=8, column=1, padx=10, pady=10)
#
# window.mainloop()

from tkinter import *
import sqlite3
import tkinter.messagebox as msg

window = Tk()
window.geometry("900x600")
reg_image = PhotoImage(file='Resgister.png')
bg_label = Label(window, image=reg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
window.title("Medicine Management System")
window.config()

"""HEADING FRAME"""

TopHeadingFrame = Frame(window, width=700, bd=1)
TopHeadingFrame.pack(side=TOP)
HeadingLabel = Label(TopHeadingFrame, text="Medicine Management System - Search Medicine",
                     font=('Helvetica', 16), fg='green', bg='white')
HeadingLabel.grid(row=0, column=0, padx=5, pady=5)

MidFrame = Frame(window, width=500, bd=1)
MidFrame.pack(side=TOP)

medicine_name = StringVar()
medicine_name.set("")

medicine_nameLabel = Label(MidFrame, text="Medicine Name", font=('helvetica', 12), fg='blue', bg='white')
medicine_nameLabel.grid(row=0, column=0, padx=5, pady=5)

medicine_nameTextBox = Entry(MidFrame, font=('Helvetica', 13), textvariable=medicine_name)
medicine_nameTextBox.grid(row=0, column=1, padx=10, pady=10)


def search():
    conn = sqlite3.connect("medicine.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM medicine WHERE MedicineName = ?", (medicine_name.get(),))
    results = cursor.fetchall()

    if results:
        msg.showinfo('SEARCH MEDICINE', f'Medicine found:\n{results}', icon="info")
    else:
        msg.showinfo('Error', 'Medicine not found', icon='warning')

    conn.close()  # Close the database connection


search_btn = Button(MidFrame, text="Search", command=search, font=('helvetica', 12), fg='white', bg='green')
search_btn.grid(row=8, column=1, padx=10, pady=10)

window.mainloop()
