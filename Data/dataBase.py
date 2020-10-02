import sqlite3 as sql
from tkinter import StringVar


class DataBase:

    def __init__(self):
        pass

    def connect(self):
        db = sql.connect("phone_book.db")
        return db

    def createTable(self):
        create_table_query = "CREATE TABLE IF NOT EXISTS Contacts (contact_id INTEGER PRIMARY KEY AUTOINCREMENT, " \
                             "first_name, text, last_name text, email text, phone_number text) "
        cursor = self.cursor()
        cursor.execute(create_table_query)

    def cursor(self):
        db = self.connect()
        cursor = db.cursor()
        return cursor

    def commit(self):
        db = self.connect()
        return db.commit()

    def selectQuery(self):
        select_query = "SELECT * FROM Contacts"
        return select_query

    def insertContact(self, t1, t2, t3, t4):
        
        insert_query = "INSERT INTO Contacts(first_name, last_name, email, phone_number) VALUES(?,?,?,?) "
        cursor = self.cursor()
        cursor.execute(insert_query, (t1, t2, t3, t4))
        self.commit()

    def updateContact(self):
        update_query = "UPDATE Contact SET(first_name = ?, last_name = ?, email = ?, phone_number = ?)"
        cursor = self.cursor()
        cursor.execute(update_query)
        self.commit()

    def deleteContact(self, id):
        delete_query = "DELETE * FROM Contact where contact_id =" + id
        cursor = self.cursor()
        cursor.execute(delete_query)
        self.commit()

    def search(self, q: str):
        search_query = "SELECT * FROM Contacts WHERE first_name LIKE '%" + q + "%' or last_name LIKE '%" + q + "%'"
        cursor = self.cursor()
        cursor.execute(search_query)
        rows = cursor.fetchall()
        print(rows)
        return rows
