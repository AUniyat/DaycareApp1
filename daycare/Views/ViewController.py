__author__ = 'ALEX'
from tkinter import *
from daycare.Views.BeanStates import States
from daycare.Views.StartMenu import StartMenu
from daycare.Views.AddFamily import addFamilyView
from daycare.Views.ViewFamily import viewFamilyFrame
from daycare.Views.generateExcel import *

class ViewController:
    root = Tk()
    result = None
    def startProject(self):
        while True:
            if States.selection == States.STARTMENU:
                app = StartMenu(master=self.root)
                app.mainloop()
            elif States.selection == States.ADDFAMILY:
                app = addFamilyView(master=self.root)
                app.mainloop()
            elif States.selection == States.VIEWFAMILY:
                app = viewFamilyFrame(master=self.root)
                app.mainloop()
            elif States.selection == States.EXCEL:
                openExcel()
                app = StartMenu(master=self.root)
                app.mainloop()
            if States.selection == States.QUIT:
                break
            app.destroy()
        self.root.destroy()

