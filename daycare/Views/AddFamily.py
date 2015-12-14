__author__ = 'ALEX'
from tkinter import *
from daycare.Views.StartMenu import *
from daycare.Database.DatabaseSqlite3 import *
from tkinter import messagebox


class addFamilyView(Frame):

    db = None
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.db = Database()
        self.grid()
        self.master.title("Add family")
        #Back Button
        self.btnBack = Button(self)
        self.btnBack["text"] = "Back"
        self.btnBack["command"] = self.clickBack
        self.btnBack.grid(row=9, column=0, sticky=W+E)
        self.widgetsAddFamily()

    def clickBack(self):
        States.selection = States.STARTMENU
        self.quit()
    def widgetsAddFamily(self):
        #setting the label frame
        self.lblfrmAddfamily = LabelFrame(self, text="Add Family Information")
        self.lblfrmAddfamily.grid(row=0, column=0, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)
        #adding a label for the first name
        self.lblAddFamilyFirstName = Label(self.lblfrmAddfamily, text="First Name: ")
        self.lblAddFamilyFirstName.grid(row=0, column=0)
        #adding a text box for the first name
        self.txtAddFirstName = Entry(self.lblfrmAddfamily, bg="pale turquoise", width=20)
        self.txtAddFirstName.grid(row=0, column=1)
        #adding a label for the last name
        self.lblAddFamilyLastName = Label(self.lblfrmAddfamily, text="Last Name: ")
        self.lblAddFamilyLastName.grid(row=1, column=0)
        #adding a text box for the last name
        self.txtAddLastName = Entry(self.lblfrmAddfamily, bg="pale turquoise", width=20)
        self.txtAddLastName.grid(row=1, column=1)
        #adding a label for a phone number
        self.lblAddPhoneNumber = Label(self.lblfrmAddfamily, text="Phone #: ")
        self.lblAddPhoneNumber.grid(row=2, column=0)
        #Adding a text box for a phone number
        self.txtAddPhone = Entry(self.lblfrmAddfamily, bg="pale turquoise", width=20)
        self.txtAddPhone.grid(row=2, column=1)
        #adding a label for e-mail
        self.lblAddEmail = Label(self.lblfrmAddfamily, text="E-mail: ")
        self.lblAddEmail.grid(row=3, column=0)
        #Adding a text box for adding e-mail
        self.txtAddEmail = Entry(self.lblfrmAddfamily, bg="pale turquoise", width=20)
        self.txtAddEmail.grid(row=3, column=1)
        #adding a button for saving the added family
        self.btnAddFamily = Button(self.lblfrmAddfamily, text="Add Family")
        self.btnAddFamily.grid(row=1, column=3)
        self.btnAddFamily["command"] = self.clickAddfamily

    def clickAddfamily(self):
        #getting the entered values
        firstName = self.txtAddFirstName.get()
        lastName = self.txtAddLastName.get()
        phoneNumber = self.txtAddPhone.get()
        email = self.txtAddEmail.get()
        #If the user does not fill out a field a warning occurs
        if len(firstName) == 0 or len(lastName) == 0 or len(phoneNumber) == 0 or len(email) == 0:
            self.warning()
            return
        if not firstName.isalnum() or not lastName.isalnum() or not phoneNumber.isalnum():
            messagebox.showwarning("Error", "Please use only letters or numbers for input")
            return
        else:
            messagebox.showinfo("Message", "Family Added")
            self.clearTextBoxes()
        #insert into databse
        self.db.insertFamily(firstName, lastName, phoneNumber, email)

    #A message box to warn the user of unfilled fields
    def warning(self):
        messagebox.showwarning("Error", "Please fill out the whole form")
        return

    def clearTextBoxes(self):
        self.txtAddFirstName.delete(0, END)
        self.txtAddLastName.delete(0, END)
        self.txtAddPhone.delete(0, END)
        self.txtAddEmail.delete(0, END)
