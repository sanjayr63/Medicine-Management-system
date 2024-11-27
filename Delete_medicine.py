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
HeadingLabel = Label(TopHeadingFrame, text="Medicine Management System - Delete Medicine",
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

def delete_specific():
    conn = sqlite3.connect("medicine.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM medicine WHERE MedicineName = ?", (medicine_name.get(),))
    conn.commit()

    if cursor.rowcount > 0:
        msg.showinfo('DELETE MEDICINE', 'Medicine deleted', icon="info")
    else:
        msg.showinfo('Error', 'Medicine not found', icon='warning')

    conn.close()

def delete_all():
    conn = sqlite3.connect("medicine.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM medicine")
    conn.commit()

    msg.showinfo('DELETE ALL MEDICINE', 'All medicines deleted', icon="info")
    conn.close()

def backup():
    conn = sqlite3.connect("medicine.db")
    cursor = conn.cursor()

    # Create a backup database
    backup_conn = sqlite3.connect("medicine_backup.db")
    backup_cursor = backup_conn.cursor()

    # Create the same table structure in the backup database
    backup_cursor.execute("""
        CREATE TABLE IF NOT EXISTS medicine (
            MedicineName TEXT,
            MedicineID TEXT,
            Brand TEXT,
            ChemicalCompanent TEXT,
            MFG_Date TEXT,
            EXP_Date TEXT,
            price INT
        )
    """)

    # Fetch all data from the original database
    cursor.execute("SELECT * FROM medicine")
    data = cursor.fetchall()

    if data:
        # Insert data into the backup database
        backup_cursor.executemany("INSERT INTO medicine VALUES (?, ?, ?, ?, ?, ?, ?)", data)
        backup_conn.commit()
        msg.showinfo('Backup', 'All data backed up successfully!', icon="info")
    else:
        msg.showinfo('Backup', 'No data to backup!', icon="warning")

    # Close connections
    conn.close()
    backup_conn.close()

def restore():
    conn = sqlite3.connect("medicine.db")
    cursor = conn.cursor()

    # Connect to the backup database
    backup_conn = sqlite3.connect("medicine_backup.db")
    backup_cursor = backup_conn.cursor()

    # Fetch all data from the backup database
    backup_cursor.execute("SELECT * FROM medicine")
    data = backup_cursor.fetchall()

    if data:
        # Clear the current data in the main database
        cursor.execute("DELETE FROM medicine")
        cursor.executemany("INSERT INTO medicine VALUES (?, ?, ?, ?, ?, ?, ?)", data)
        conn.commit()
        msg.showinfo('Restore', 'Data restored from backup successfully!', icon="info")
    else:
        msg.showinfo('Restore', 'No backup data to restore!', icon='warning')

    # Close connections
    conn.close()
    backup_conn.close()

delete_btn = Button(MidFrame, text="Delete", command=delete_specific, font=('helvetica', 12), fg='white', bg='green')
delete_btn.grid(row=8, column=1, padx=10, pady=10)

delete_all_btn = Button(MidFrame, text="Delete All", command=delete_all, font=('helvetica', 12), fg='white', bg='green')
delete_all_btn.grid(row=8, column=2, padx=10, pady=10)

backup_btn = Button(MidFrame, text="Backup", command=backup, font=('helvetica', 12), fg='white', bg='green')
backup_btn.grid(row=8, column=3, padx=10, pady=10)

restore_btn = Button(MidFrame, text="Restore", command=restore, font=('helvetica', 12), fg='white', bg='green')
restore_btn.grid(row=8, column=4, padx=10, pady=10)

window.mainloop()
