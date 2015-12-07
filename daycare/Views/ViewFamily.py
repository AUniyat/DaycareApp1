__author__ = 'ALEX'
from tkinter import *
from daycare.Views.StartMenu import *
from daycare.Database.DatabaseSqlite3 import *

class viewFamilyFrame(Frame):
    db = None
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.db = Database()
        self.grid()
        self.master.title("Current Families")
        #Back Button
        self.btnBack = Button(self)
        self.btnBack["text"] = "Back"
        self.btnBack["command"] = self.clickBack
        self.btnBack.grid(row=6, column=0, sticky=W+S)
        #Delete Button
        self.btnDelete = Button(self)
        self.btnDelete["text"]= "Delete Family"
        self.btnDelete.grid(row=5,column=0, sticky=W+S)
        self.btnDelete["command"] = self.clickDelete
        #Add Widgets
        self.widgetsViewFamilies()

    def clickBack(self):
        States.selection = States.STARTMENU
        self.quit()

    def clickDelete(self):
        selectedFamily = self.lstbxFamilies.get(self.lstbxFamilies.curselection())
        name1 = str(selectedFamily).split()[0]
        name2 = str(selectedFamily).split()[1]
        self.db.deleteFamily(name1, name2)

    def widgetsViewFamilies(self):
        self.lblfrmViewfamily = LabelFrame(self, text="Current Families")
        self.lblfrmViewfamily.grid(row=0, column=0, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)
        #Add a list box
        self.lstbxFamilies = Listbox(self.lblfrmViewfamily, width=50, height=5, exportselection=0)
        self.lstbxFamilies.grid(row=0, column=0, columnspan=2)
        #Add a scroll bar to the list box
        self.scrollBar = Scrollbar(self.lblfrmViewfamily, orient=VERTICAL)
        self.scrollBar.grid(row=0, column=2, sticky=N+S)
        self.lstbxFamilies.config(yscrollcommand=self.scrollBar.set)
        self.scrollBar.config(command=self.lstbxFamilies.yview)
        #populate list box
        self.updateListBox(self.lstbxFamilies)

    def updateListBox(self, listBox):
        #listBox.delete(0, END)
        families = self.db.getAllFamilies()
        allFamilies = []
        for tuple in families:
            family = Family(tuple[0], tuple[1], tuple[2], tuple[3])
            allFamilies.append(family)
        for x in allFamilies:
            listBox.insert(END, x)

