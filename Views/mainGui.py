from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from tkinter.ttk import Treeview
from Data.dataBase import DataBase
from Views.addContact import AddContactWindow
from Views.aboutUs import AboutUsWindow
import sqlite3 as sql


def updateTreeview(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert("", 'end', values=i)


def search():
    q2 = q.get()
    search_query = "SELECT * FROM Contacts WHERE first_name LIKE '%" + q2 + "%' or last_name LIKE '%" + q2 + "%'"
    cursor.execute(search_query)
    rows = cursor.fetchall()
    updateTreeview(rows)


db = sql.connect("phone_book.db")
cursor = db.cursor()
create_table_query = "CREATE TABLE IF NOT EXISTS Contacts (contact_id INTEGER PRIMARY KEY AUTOINCREMENT, first_name " \
                     "text, last_name text, " \
                     "email text, phone_number text) "


# testing the table and insert into her
# # insert_query = "INSERT INTO Contacts(first_name, last_name, email, phone_number) VALUES(?,?,?,?)"
# cursor.execute(create_table_query)
# cursor.execute(insert_query, ("Jose", "Martinez", "Mjose@gmail.com", "809-325-2626"))

def clear():
    clear_query = "SELECT * FROM Contacts"
    cursor.execute(clear_query)
    rows = cursor.fetchall()
    updateTreeview(rows)


def clear_text():
    search_entry.delete(0, 'end')
    id_entry.delete(0, 'end')
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    entry3.delete(0, 'end')
    entry4.delete(0, 'end')
    search()


def getRow(event):
    row_id = trv.identify_row(event.y)
    item = trv.item(trv.focus())
    t_id.set(item['values'][0])
    t1.set(item['values'][1])
    t2.set(item['values'][2])
    t3.set(item['values'][3])
    t4.set(item['values'][4])


# instantiating the class Tkinter
root = Tk()

# instantiating the add contact window and pass the root like parameter into the instance


root.title("PhoneBook App")
root.geometry("800x700")
root.resizable(False, False)

# instantiating menu
menubar = Menu(root)


def addContactWindow():
    add_contact_window = AddContactWindow(root)
    return add_contact_window


root.configure(menu=menubar)

file_menu = Menu(menubar, tearoff=1)
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)

q = StringVar()
t_id = StringVar()
t1 = StringVar()
t2 = StringVar()
t3 = StringVar()
t4 = StringVar()


def aboutUsWindow():
    about_us_window = AboutUsWindow(root)
    return about_us_window


# menu option about us
about_menu = Menu(menubar, tearoff=1)
about_menu.add_command(label="About us", command=aboutUsWindow)
menubar.add_cascade(label="Help", menu=about_menu)

# defining 3 sections into the window
wrapper1 = LabelFrame(root, text="Contact List")
wrapper2 = LabelFrame(root, text="Search")
wrapper3 = LabelFrame(root, text="Contact Data")

wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)
wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)
# List section
trv = Treeview(wrapper1, columns=(1, 2, 3, 4, 5), show="headings", height=6)

trv.pack(side=LEFT)
trv.place(x=0, y=0)
trv.heading("#0", text="")
trv.heading("#1", text="Contact ID")
trv.heading("#2", text="First Name")
trv.heading("#3", text="Last Name")
trv.heading("#4", text="Email")
trv.heading("#5", text="Phone No.")

trv.column('#0', width=50, minwidth=100)
trv.column('#1', width=150, minwidth=200)
trv.column('#2', width=150, minwidth=200)
trv.column('#3', width=150, minwidth=200)
trv.column('#4', width=150, minwidth=200)
trv.column('#5', width=150, minwidth=200)
trv.bind('<Double 1>', getRow)
# vertical scrollbar
yscrollbar = ttk.Scrollbar(wrapper1, orient='vertical', command=trv.yview)
yscrollbar.pack(side=RIGHT, fill="y")
# horizontal scrollbar
xscrollbar = ttk.Scrollbar(wrapper1, orient='horizontal', command=trv.xview)
xscrollbar.pack(side=BOTTOM, fill='x')
trv.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)

query = "SELECT contact_id, first_name, last_name, email, phone_number FROM Contacts"
cursor.execute(query)
rows = cursor.fetchall()
updateTreeview(rows)

# Search Section
label = Label(wrapper2, text="Search")
label.pack(side=tk.LEFT, padx=10)

# label, entry and button  search and clear
search_entry = Entry(wrapper2, textvariable=q)
search_entry.pack(side=tk.LEFT, padx=6)
search_button = Button(wrapper2, text="Search", command=search)
search_button.pack(side=tk.LEFT, padx=6)
clear_button = Button(wrapper2, text="Clear", command=lambda: [search, clear_text()])
clear_button.pack(side=tk.LEFT, padx=6)

# labels and entries that belongs to wraper 3
id_label = Label(wrapper3, text="Contact ID:")
id_label.grid(column=1, row=0, padx=5, pady=3)
id_entry = Entry(wrapper3, textvariable=t_id)
id_entry.grid(column=2, row=0, padx=5, pady=3)

label1 = Label(wrapper3, text="First Name:")
label1.grid(column=1, row=1, padx=5, pady=3)
entry1 = Entry(wrapper3, textvariable=t1)
entry1.grid(column=2, row=1, padx=5, pady=3)

label2 = Label(wrapper3, text="Last Name:")
label2.grid(column=1, row=2, padx=5, pady=3)
entry2 = Entry(wrapper3, textvariable=t2)
entry2.grid(column=2, row=2, padx=5, pady=3)

label3 = Label(wrapper3, text="Email:")
label3.grid(column=1, row=3, padx=5, pady=3)
entry3 = Entry(wrapper3, textvariable=t3)
entry3.grid(column=2, row=3, padx=5, pady=3)

label4 = Label(wrapper3, text="Phone #:")
label4.grid(column=1, row=4, padx=5, pady=3)
entry4 = Entry(wrapper3, textvariable=t4)
entry4.grid(column=2, row=4, padx=5, pady=3)


def updateContact():
    firts = t1.get()
    last = t2.get()
    email = t3.get()
    phone = t4.get()
    id = t_id.get()
    print(id)
    update_query = "UPDATE Contacts SET First_name = ?, Last_Name=?, email=?, phone_number=? WHERE contact_id = ?"
    if messagebox.askyesno("Confirm", "Are you sure you want to update the record"):
        cursor.execute(update_query, (firts, last, email, phone, id))
        db.commit()
        clear()
        clear_text()
    else:
        return True


# button action update contact
update_button = Button(wrapper3, text="Update", command=updateContact)
update_button.grid(column=3, row=4, padx=5, pady=3)


def addContact():
    firts = t1.get()
    last = t2.get()
    email = t3.get()
    phone = t4.get()
    insert_query = "INSERT INTO Contacts(first_name, last_name, email, phone_number) VALUES(?,?,?,?)"
    cursor.execute(insert_query, (firts, last, email, phone))
    clear()
    clear_text()


# button action add or insert a new contact
add_button = Button(wrapper3, text="Add", command=addContact)
add_button.grid(column=4, row=4, padx=5, pady=3)


def deleteContact():
    delete_query = "DELETE FROM Contacts WHERE contact_id = " + t_id.get()
    print(delete_query)
    if messagebox.askyesno("Confirm delete", "Are you sure you want to delete this record?"):
        cursor.execute(delete_query)
        clear()
        clear_text()
        db.commit()
    else:
        return True


# button action delete
delete_button = Button(wrapper3, text="Delete", command=deleteContact)
delete_button.grid(column=5, row=4, padx=5, pady=3)

root.mainloop()
