__author__ = 'ALEX'
import sqlite3

class Family:
    def __init__(self, firstName, lastName, phone, email):
        self.firstName = firstName
        self.lastName = lastName
        self.phone = phone
        self.email = email

    def __str__(self):
       return str(self.firstName) + " " + str(self.lastName) + " " + str(self.phone) + " " + str(self.email)

class Database:

    dbName = "DaycareFamilies.db"

    def __init__(self):
        self.conn = sqlite3.connect(self.dbName, timeout=10)
        self.conn.execute("PRAGMA foreign_keys = OFF")
        self.cursor = self.conn.cursor()

    def setupDB(self):
        #self.dropTables()
        self.createFamilyTable()

    def createFamilyTable(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Families
                               (firstName text,
                                lastName text,
                                phone text,
                                email text)''')
        self.conn.commit()


    def insertFamily(self, firstName, lastName, phone, email):
        self.cursor.execute('INSERT INTO Families (firstName, lastName, phone, email) VALUES (?, ?, ?, ?)',
                            [firstName, lastName, phone, email])
        self.conn.commit()

    def getAllFamilies(self):
        self.cursor.execute('SELECT * FROM Families')
        self.conn.commit()
        return self.cursor.fetchall()

    def dropTables(self):
        self.cursor.execute('''DROP TABLE IF EXISTS Families''')
        self.conn.commit()

    def deleteFamily(self, firstName, lastName):
        self.cursor.execute('DELETE FROM Families WHERE firstName = ? AND lastname = ? ', (firstName, lastName))
        self.conn.commit()

