__author__ = 'ALEX'
from tkinter import *
from daycare.Views.StartMenu import *
from daycare.Database.DatabaseSqlite3 import *
from tkinter import messagebox

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
        self.btnBack.grid(row=2, column=0, sticky=N+W+E)
        #Delete Button
        self.btnDelete = Button(self)
        self.btnDelete["text"]= "Delete Family"
        self.btnDelete.grid(row=1, column=0, sticky=N+W+E)
        self.btnDelete["command"] = self.clickDelete
        #Add Widgets
        self.widgetsViewFamilies()
        self.widgetAddPayments()

    def clickBack(self):
        States.selection = States.STARTMENU
        self.quit()

    def clickDelete(self):
        #If the user has not selecter a family send a warning
        if not self.lstbxFamilies.curselection():
            messagebox.showwarning("Error", "Please select a family")
            return
        #Ask the user if they are sure of deletion
        if messagebox.askyesno("Confirm","Are you sure you want to delete this family?"):
            selectedFamily = self.lstbxFamilies.get(self.lstbxFamilies.curselection())
            familyID = int(str(selectedFamily).split(':')[0])
            self.db.deleteFamily(familyID)
            self.deleteSucess()
            self.updateListBox(self.lstbxFamilies)

    def widgetsViewFamilies(self):
        self.lblfrmViewfamily = LabelFrame(self, text="First Name, Last Name, Phone #, E-mail")
        self.lblfrmViewfamily.grid(row=0, column=0, sticky='WENS', padx=5, pady=5, ipadx=5, ipady=30)
        #Add a list box
        self.lstbxFamilies = Listbox(self.lblfrmViewfamily, width=50, height=20, exportselection=0)
        self.lstbxFamilies.grid(row=0, column=0, columnspan=2)
        #Add a scroll bar to the list box
        self.scrollBar = Scrollbar(self.lblfrmViewfamily, orient=VERTICAL)
        self.scrollBar.grid(row=0, column=2, sticky=N+S)
        self.lstbxFamilies.config(yscrollcommand=self.scrollBar.set)
        self.scrollBar.config(command=self.lstbxFamilies.yview)
        #populate list box
        self.updateListBox(self.lstbxFamilies)

    def widgetAddPayments(self):
        self.lblfrmAddpayment = LabelFrame(self, text="Add Monthly Payments")
        self.lblfrmAddpayment.grid(row=0, column=1, sticky='N', padx=5, pady=5, ipadx=5, ipady=5)
        #add January label and entry text box
        self.lblJanuary = Label(self.lblfrmAddpayment, text="January: ")
        self.lblJanuary.grid(row=0, column=0)
        self.txtAddJanuary = Entry(self.lblfrmAddpayment, bg="pale turquoise", width=20)
        self.txtAddJanuary.grid(row=0, column=1)
        #add February label and entry text box
        self.lblFebruary = Label(self.lblfrmAddpayment, text="February: ")
        self.lblFebruary.grid(row=1, column=0)
        self.txtAddFebruary = Entry(self.lblfrmAddpayment, bg="pale turquoise", width=20)
        self.txtAddFebruary.grid(row=1, column=1)
        #add March label and entry text box
        self.lblMarch = Label(self.lblfrmAddpayment, text="March: ")
        self.lblMarch.grid(row=2, column=0)
        self.txtAddMarch = Entry(self.lblfrmAddpayment, bg="pale turquoise", width=20)
        self.txtAddMarch.grid(row=2, column=1)
        #add April label and entry text box
        self.lblApril = Label(self.lblfrmAddpayment, text="April: ")
        self.lblApril.grid(row=3, column=0)
        self.txtAddApril = Entry(self.lblfrmAddpayment, bg="pale turquoise", width=20)
        self.txtAddApril.grid(row=3, column=1)
        #add May label and entry text box
        self.lblMay = Label(self.lblfrmAddpayment, text="May: ")
        self.lblMay.grid(row=4, column=0)
        self.txtAddMay = Entry(self.lblfrmAddpayment, bg="pale turquoise", width=20)
        self.txtAddMay.grid(row=4, column=1)
        #add June label and entry text box
        self.lblJune = Label(self.lblfrmAddpayment, text="June: ")
        self.lblJune.grid(row=5, column=0)
        self.txtAddJune = Entry(self.lblfrmAddpayment, bg="pale turquoise", width=20)
        self.txtAddJune.grid(row=5, column=1)
        #add July label and entry text box
        self.lblJuly = Label(self.lblfrmAddpayment, text="July: ")
        self.lblJuly.grid(row=6, column=0)
        self.txtAddJuly = Entry(self.lblfrmAddpayment, bg="pale turquoise", width=20)
        self.txtAddJuly.grid(row=6, column=1)
        #add August label and entry text box
        self.lblAugust = Label(self.lblfrmAddpayment, text="August: ")
        self.lblAugust.grid(row=7, column=0)
        self.txtAddAugust = Entry(self.lblfrmAddpayment, bg="pale turquoise", width=20)
        self.txtAddAugust.grid(row=7, column=1)
        #add September label and entry text box
        self.lblSeptember = Label(self.lblfrmAddpayment, text="September: ")
        self.lblSeptember.grid(row=8, column=0)
        self.txtAddSeptember = Entry(self.lblfrmAddpayment, bg="pale turquoise", width=20)
        self.txtAddSeptember.grid(row=8, column=1)
        #add October label and entry text box
        self.lblOctober = Label(self.lblfrmAddpayment, text="October: ")
        self.lblOctober.grid(row=9, column=0)
        self.txtAddOctober = Entry(self.lblfrmAddpayment, bg="pale turquoise", width=20)
        self.txtAddOctober.grid(row=9, column=1)
        #add November label and entry text box
        self.lblNovember = Label(self.lblfrmAddpayment, text="November: ")
        self.lblNovember.grid(row=10, column=0)
        self.txtAddNovember = Entry(self.lblfrmAddpayment, bg="pale turquoise", width=20)
        self.txtAddNovember.grid(row=10, column=1)
        #add December label and entry text box
        self.lblDecember = Label(self.lblfrmAddpayment, text="December: ")
        self.lblDecember.grid(row=11, column=0)
        self.txtAddDecember = Entry(self.lblfrmAddpayment, bg="pale turquoise", width=20)
        self.txtAddDecember.grid(row=11, column=1)
        #Save Button
        self.btnSave = Button(self.lblfrmAddpayment)
        self.btnSave["text"] = "Save"
        self.btnSave["command"] = self.clickSave
        self.btnSave.grid(row=12, column=0, columnspan=2, sticky=E+W)
        self.btnSave['state'] = 'disabled'

    def updateListBox(self, listBox):
        listBox.delete(0, END)
        #Pull all the data from the families table and populate the list box
        families = self.db.getAllFamilies()
        allFamilies = []
        for tuple in families:
            family = Family(tuple[0], tuple[1], tuple[2], tuple[3], tuple[4])
            allFamilies.append(family)
        for x in allFamilies:
            listBox.insert(END, x)

    def deleteSucess(self):
        messagebox.showinfo("Message","Delete successful!")

    def clickSave(self):
        if not self.lstbxFamilies.curselection():
            messagebox.showwarning("Error", "Please select a family")
            return
        january = self.txtAddJanuary.get()
        february = self.txtAddFebruary.get()
        march = self.txtAddMarch.get()
        april = self.txtAddApril.get()
        may = self.txtAddMay.get()
        june = self.txtAddJune.get()
        july = self.txtAddJuly.get()
        august = self.txtAddAugust.get()
        september = self.txtAddSeptember.get()
        october = self.txtAddOctober.get()
        november = self.txtAddNovember.get()
        december = self.txtAddDecember.get()
        selectedFamily = self.lstbxFamilies.get(self.lstbxFamilies.curselection())
        trackFamily = int(str(selectedFamily).split(':')[0])
        self.db.insertpayments(january, february, march, april, may, june, july, august,
                               september, october, november, december, trackFamily)
        #allPayments = self.db.getAllPayments()
        paymentsList = []
        # for tuple in allPayments:
        #     payment = payments(tuple[0], tuple[1], tuple[2], tuple[3], tuple[4], tuple[5], tuple[6],
        #                        tuple[7],tuple[8], tuple[9], tuple[10], tuple[11])
        #     paymentsList.append(payment)
        # for x in paymentsList:
        #     print(x)





