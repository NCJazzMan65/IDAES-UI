#######################################################################
#                                                                     #
#               IDAES Flowsheet Editor (IDAES-FE)                     #
#                                                                     #
#  This program is a graphical interface for creating, editing, and   #
#  running process model flowsheets based on the DOE IDAES platform.  #
#                                                                     #
#  Author:  Timothy A. Fuller                                         #
#  Date:  4/30/2020                                                   #
#                                                                     #
#  Version:  1.0.0                                                    #
#                                                                     #
#######################################################################


# System module imports
import sys
import os

# Module imports
from tkinter import *
from tkinter import ttk
import IDAESCutomWidgets as Custom


# Define the main window
class MainWindow(Frame):

    # Override initialization method
    def __init__(self, master = None):

        # Set master window
        super().__init__(master)
        self.master = master
        self.master.title('IDAES Flowsheet Editor')
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.master.geometry('640x480+30+30')
        #self.mainwindow = Toplevel(self.master)

        # Create main paned window frame
        self.mainwindowpane = ttk.Panedwindow(self.master, orient=HORIZONTAL)
        self.mainwindowpane.grid(column=0, row=0, sticky=(N,S,E,W))
        self.toolpane = ttk.Labelframe(self.mainwindowpane, width=120, height=240)
        self.sheetpane = ttk.Labelframe(self.mainwindowpane, width=200, height=240)
        self.mainwindowpane.add(self.toolpane)
        self.mainwindowpane.add(self.sheetpane)

        # Create main menu
        self.create_menu()

        # Create library frame
        self.create_libraryframe()

        # Create flowsheet frame
        self.create_flowsheetframe()
        
    # Method to create the main menu
    def create_menu(self):

        # Define main menu bar
        self.mainmenu = Menu(self.master)
        self.master['menu'] = self.mainmenu

        # Define File menu
        self.menu_file = Menu(self.mainmenu)
        self.menu_file.add_command(label='New')
        self.menu_file.add_separator()
        self.menu_file.add_command(label="Open...")
        self.mainmenu.add_cascade(menu=self.menu_file, label='File')

        # Define Edit menu
        self.menu_edit = Menu(self.mainmenu)
        self.mainmenu.add_cascade(menu=self.menu_edit, label='Edit')

    # Create the library frame and contained widgets
    def create_libraryframe(self):

        # Create the frame
        self.libraryframe = ttk.Frame(self.toolpane, borderwidth=2, 
                                      relief="sunken")
        self.libraryframe.grid(column=0, row=0, sticky=(N,S,E,W))
        self.libraryframe.columnconfigure(0, weight=1)
        self.libraryframe.rowconfigure(0, weight=1)

        # Add the unit model list box widget
        self.listboxitems = ('One','Two','Three','Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten')
        #self.boxitems = StringVar(value=self.listboxitems)
        #self.unitmodelslistbox = Listbox(self.libraryframe, listvariable=self.boxitems, height=20)
        self.unitmodelslistbox = Custom.ScrollableListbox(self.libraryframe)
        self.unitmodelslistbox.listitems = StringVar(value=self.listboxitems)
        self.unitmodelslistbox.grid(column=0, row=0, sticky=(N,S,E,W))

    # Create flowsheet frame and contained widgets
    def create_flowsheetframe(self):

        # Create the frame
        self.flowheetframe = ttk.Frame(self.sheetpane)
        self.flowheetframe.grid(column=1,row=0, sticky='nsew')
        self.flowheetframe.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Add the flowsheet notebook widget
        self.fsnotebook = ttk.Notebook(self.flowheetframe)
        self.fsnotebook.grid(column=0, row=0, sticky=(N,S,E,W))
        self.fstab1 = ttk.Frame(self.fsnotebook)
        self.fstab2 = ttk.Frame(self.fsnotebook)
        self.fsnotebook.add(self.fstab1, text="Flowsheet 1")
        self.fsnotebook.add(self.fstab2, text="Flowsheet 2")

# Define main method
def main():

    # Create root window
    rootwindow = Tk()

    # Create an instance of the main window class
    app = MainWindow(rootwindow)

    # Run the application
    app.mainloop()


# Call main function on startup
if __name__ == '__main__':
    main()
