__author__ = 'ALEX'
from tkinter import *
from daycare.Views.BeanStates import States

class StartMenu(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.master.title("DayCare")
        #Add widgets
        self.widgetStartMenu()


    def widgetStartMenu(self):
        self.lblfrmStartMenu = LabelFrame(self, text="Menu")
        self.lblfrmStartMenu.grid(row=0, column=0, sticky='WE', padx=5, pady=5, ipadx=5, ipady=5)
        #The add family button
        self.btnAddFamily = Button(self.lblfrmStartMenu)
        self.btnAddFamily["text"] = "Add Family"
        self.btnAddFamily["command"] = self.clickbtnAddFamily
        self.btnAddFamily.grid(row=0, column=0, sticky=W+E)
        #Exit Button
        self.btnExit = Button(self.lblfrmStartMenu)
        self.btnExit["text"] = "Exit"
        self.btnExit["command"] = self.clickbtnExit
        self.btnExit.grid(row=2, column=0, sticky=W+E)
        #View current families button
        self.btnViewFamily = Button(self.lblfrmStartMenu)
        self.btnViewFamily["text"] = "View Current Families"
        self.btnViewFamily.grid(row=1, column=0)
        self.btnViewFamily["command"] = self.clickbtnViewFamily
        #Generate Excel button
        self.btnExcel = Button(self.lblfrmStartMenu)
        self.btnExcel["text"] = "Generate Excel Report"
        self.btnExcel.grid(row=1, column=1)
        self.btnExcel["command"] = self.clickbtnExcel

    #actions  for click events
    def clickbtnExit(self):
        States.selection = States.QUIT
        self.quit()

    def clickbtnAddFamily(self):
        States.selection = States.ADDFAMILY
        self.quit()

    def clickbtnViewFamily(self):
        States.selection = States.VIEWFAMILY
        self.quit()

    def clickbtnExcel(self):
        States.selection = States.EXCEL
        self.quit()

