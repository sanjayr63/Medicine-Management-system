from tkinter import *
import sqlite3
import tkinter.messagebox as msg
from tkinter import ttk   #themed tkinter

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
HeadingLabel = Label(TopHeadingFrame,text="Medicine Management System - View Medicine",
                     font=('Helvetica',16),fg='green',bg='white')
HeadingLabel.grid(row=0,column=0,padx=5,pady=5)

MidFrame = Frame(window,width = 700,bd=1)
MidFrame.pack(side=TOP)

view_frame = Frame(window,bd=1)
view_frame.pack(side=TOP,fill=X)

tv = ttk. Treeview(view_frame,columns=('MedicineName','MedicineID','Brand','ChemicalComponent','MFG_Date','EXP_Date','Price'))

tv.heading('#1',text='Medicine Name')
tv.heading('#2',text='Medicine Id')
tv.heading('#3',text='Brand')
tv.heading('#4',text='ChemicalComponent')
tv.heading('#5',text='MFG_DATE')
tv.heading('#6',text='EXP_DATE')
tv.heading('#7',text='Price')

tv.column('#0', width=0,stretch=NO)
tv.column('#1', width=50)
tv.column('#2', width=50)
tv.column('#3', width=50)
tv.column('#4', width=50)
tv.column('#5', width=50)
tv.column('#6', width=50)
tv.column('#7', width=50)

tv.pack(fill=X)

conn = sqlite3.connect('medicine.db')
cursor = conn.cursor()
cursor.execute("select * from 'medicine' ")
data = cursor.fetchall()

for i in data:
    tv.insert("", "end", values=i)




window.mainloop()