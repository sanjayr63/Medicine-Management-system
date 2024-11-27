from tkinter import *
import sqlite3
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
HeadingLabel = Label(TopHeadingFrame,text="Medicine Management System - Add Medicine",
                     font=('Helvetica',16),fg='green',bg='white')
HeadingLabel.grid(row=0,column=0,padx=5,pady=5)

MidFrame = Frame(window,width=500,bd=1)
MidFrame.pack(side=TOP)


conn = sqlite3.connect("medicine.db")
cursor = conn.cursor()
cursor.execute("""create table if not exists 'medicine'(MedicineName text, MedicineID text,Brand text, ChemicalCompanent text,MFG_Date text,EXP_Date text,price int)""")
conn.commit()


medicine_name = StringVar()
medicine_name.set("")

medicine_nameLabel = Label(MidFrame,text="Medicine Name",font=('helvetica',12),fg='blue',bg='white')
medicine_nameLabel.grid(row=0,column=0,padx=5,pady=5)

medicine_nameTextBox = Entry(MidFrame,font=('Helvitica',13),textvariable=medicine_name)
medicine_nameTextBox.grid(row=0,column=1,padx=10,pady=10)

'''ID'''



medicine_id = StringVar()
medicine_id.set("")

medicine_idLabel = Label(MidFrame,text="Medicine Id",font=("hellvetica",12),fg='blue',bg='white')
medicine_idLabel.grid(row=1,column=0,padx=10,pady=10)

medicine_idTextBox = Entry(MidFrame,font=("helvitica",12),textvariable=medicine_id)
medicine_idTextBox.grid(row=1,column=1,padx=10,pady=10)

'''userName'''

brand = StringVar()
brand.set("")

brandLabel = Label(MidFrame,text="Brand",font=("hellvetica",12),fg='blue',bg='white')
brandLabel.grid(row=2,column=0,padx=10,pady=10)

brandTextBox = Entry(MidFrame,font=("helvitica",12),textvariable=brand)
brandTextBox.grid(row=2,column=1,padx=10,pady=10)

'''PASSWORD'''

ChemicalCompanent = StringVar()
ChemicalCompanent .set("")

ChemicalCompanentLabel = Label(MidFrame,text="Chemical Companent ",font=("hellvetica",12),fg='blue',bg='white')
ChemicalCompanentLabel.grid(row=3,column=0,padx=10,pady=10)

ChemicalCompanentTextBox = Entry(MidFrame,font=("helvitica",12),textvariable=ChemicalCompanent )
ChemicalCompanentTextBox.grid(row=3,column=1,padx=10,pady=10)
'''MOBILE NO'''

mfg = StringVar()
mfg  .set("")

mfgLabel = Label(MidFrame,text="MFG_Date ",font=("hellvetica",12),fg='blue',bg='white')
mfgLabel.grid(row=4,column=0,padx=10,pady=10)

mfgTextBox = Entry(MidFrame,font=("helvitica",12),textvariable=mfg  )
mfgTextBox.grid(row=4,column=1,padx=10,pady=10)

'''EMIL ID'''

exp = StringVar()
exp.set('')

expLabel = Label(MidFrame,text='EXP_Date',font=('helltetica',12),fg='blue',bg='white')
expLabel.grid(row=5,column=0,padx=10,pady=10)

expTextBox = Entry(MidFrame,font=('helltetica',12),textvariable=exp)
expTextBox.grid(row=5,column=1,padx=10,pady=10)

price = StringVar()
price .set('')

priceLabel = Label(MidFrame,text='Price',font=('helltetica',12),fg='blue',bg='white')
priceLabel.grid(row=6,column=0,padx=10,pady=10)

priceTextBox = Entry(MidFrame,font=('helltetica',12),textvariable=price)
priceTextBox.grid(row=6,column=1,padx=10,pady=10)


def add():
    user_data = {
        "medicine_name": medicine_name.get(),
        "MedicineID": medicine_id.get(),
        "Brand": brand.get(),
        "ChemicalCompanent": ChemicalCompanent.get(),
        "MFG_Date": mfg.get(),
        "EXP_Date": exp.get(),
        "price": price.get(),
    }

    # Validation: Check for empty fields
    for key, value in user_data.items():
        if not value.strip():  # Check if the field is empty or contains only whitespace
            msg.showerror('Input Error', f'{key} cannot be empty!')
            return  # Exit the function if any field is empty

    # Ensure price is a valid integer
    if not user_data["price"].isdigit():
        msg.showerror('Input Error', 'Price must be a valid number!')
        return

    # Check for duplicates in the database
    conn = sqlite3.connect("medicine.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM medicine WHERE MedicineID = ? OR MedicineName = ?",
                   (user_data["MedicineID"], user_data["medicine_name"]))

    if cursor.fetchone():
        msg.showerror('Input Error', 'Medicine ID   already exists!')
        return  # Exit if a duplicate is found

    # Insert new record if all validations pass
    cursor.execute(
        """INSERT INTO medicine (MedicineName, MedicineID, Brand, ChemicalCompanent, MFG_Date, EXP_Date, price) 
        VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (user_data["medicine_name"], user_data["MedicineID"], user_data["Brand"],
         user_data["ChemicalCompanent"], user_data["MFG_Date"], user_data["EXP_Date"], int(user_data["price"]))
    )

    conn.commit()

    if cursor.rowcount > 0:
        msg.showinfo('ADD MEDICINE', 'New Medicine added', icon="info")
    else:
        msg.showinfo('Error', 'New Medicine not added', icon='warning')


def back():
    window.destroy()
    import Home


'''BuTTON'''

add_btn = Button(MidFrame,text='ADD', command=add, font=('helltetica',12),fg='white',bg='green')
add_btn.grid(row=7,column=0,padx=5,pady=5)


back_btn = Button(MidFrame,text="Back", command=back, font=('helltetica',12),fg='white',bg='green')
back_btn.grid(row=8,column=1,padx=10,pady=10)






window.mainloop()