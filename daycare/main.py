__author__ = 'ALEX'
from daycare.Views.ViewController import *
from daycare.Database.DatabaseSqlite3 import *

#Set up the database
dbm = Database()
dbm.setupDB()

#Start the app with tkinter
vc = ViewController()
vc.startProject()

