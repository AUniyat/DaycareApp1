__author__ = 'ALEX'
import sqlite3

class Family:
    def __init__(self, id, firstName, lastName, phone, email):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.phone = phone
        self.email = email

    def __str__(self):
       return str(self.id) + ": " + str(self.firstName) + " " + str(self.lastName) + " " + \
              str(self.phone) + " " + str(self.email)

class payments:
    def __init__(self, january, february, march, april, may, june, july, august, september,
                 october, november, december, trackFamily):
        self.january = january
        self.february = february
        self.march = march
        self.april = april
        self.may = may
        self.june = june
        self.july = july
        self.august = august
        self.september = september
        self.october = october
        self.november = november
        self.december = december
        self.trackFamily = trackFamily

    def __str__(self):
        return (format(self.january) + " " + format(self.february) + " " + format(self.march) +
                " " + format(self.april) + " " + format(self.may) + " " + format(self.june) + " " +
                format(self.july) + " " + format(self.august) + " " + format(self.september) + " " +
                format(self.october) + " " + format(self.november) + " " + format(self.december))

class Database:

    dbName = "DaycareFamilies.db"

    def __init__(self):
        self.conn = sqlite3.connect(self.dbName, timeout=10)
        self.conn.execute("PRAGMA foreign_keys = OFF")
        self.cursor = self.conn.cursor()

    def setupDB(self):
        #self.dropTables()
        self.createFamilyTable()
        #self.createPaymentsTable()

    def createFamilyTable(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Families
                               (familyID INTEGER PRIMARY KEY AUTOINCREMENT ,
                                firstName text,
                                lastName text,
                                phone text,
                                email text)''')
        self.conn.commit()

    def createPaymentsTable(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Payments
                               (january real,
                                february real,
                                march real,
                                april real,
                                may real,
                                june real,
                                july real,
                                august real,
                                september real,
                                october real,
                                november real,
                                december real,
                                trackFamily integer,
                                FOREIGN KEY(trackFamily) REFERENCES Families(familyID) ON DELETE CASCADE)''')
        self.conn.commit()


    def insertFamily(self, firstName, lastName, phone, email):
        self.cursor.execute('INSERT INTO Families (firstName, lastName, phone, email) VALUES (?, ?, ?, ?)',
                            [firstName, lastName, phone, email])
        self.conn.commit()

    def insertpayments(self, january, february, march, april, may, june, july, august, september,
                 october, november, december, trackFamily):
        self.cursor.execute('INSERT INTO Payments'
                            '(january, february, march, april, may, june, july, august, september,october, november,'
                            'december, trackFamily) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)',[january, february, march, april, may, june, july, august, september,
                 october, november, december, trackFamily])
        self.conn.commit()

    def getAllFamilies(self):
        self.cursor.execute('SELECT * FROM Families')
        self.conn.commit()
        return self.cursor.fetchall()

    def getAllPayments(self):
        self.cursor.execute('SELECT * FROM Payments')
        self.conn.commit()
        return self.cursor.fetchall()

    def dropTables(self):
        self.cursor.execute('''DROP TABLE IF EXISTS Families''')
        self.cursor.execute('''DROP TABLE IF EXISTS Payments''')
        self.conn.commit()

    def deleteFamily(self, familyID):
        self.cursor.execute('DELETE FROM Families WHERE familyID = ? ', [familyID])
        self.conn.commit()

    def getSpecificPayment(self, trackFamily):
        self.cursor.execute('SELECT ROWID FROM Payments WHERE trackFamily = ?'), [trackFamily]
        self.conn.commit()
