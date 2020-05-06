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

# Add parent directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))

# Import IDAES-FE modules
from idaes_widgets.scrollable_listbox import ScrollableListbox


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
        self.mastercontent = ttk.Frame(self.master, padding=(3,10,3,3))
        self.mastercontent.grid(column=0, row=0, sticky=(N,S,E,W))
        self.mastercontent.columnconfigure(0, weight=1)
        self.mastercontent.rowconfigure(0, weight=1)

        # Create main paned window frame
        self.mainwindowpane = ttk.Panedwindow(self.mastercontent, orient=HORIZONTAL)
        self.mainwindowpane.grid(column=0, row=0, sticky=(N,S,E,W))
        self.toolpane = ttk.Labelframe(self.mainwindowpane, text="Model Library", width=240, height=480)
        self.toolpane.columnconfigure(0, weight=1)
        self.toolpane.rowconfigure(0, weight=1)
        self.sheetpane = ttk.Labelframe(self.mainwindowpane, width=400, height=480)
        self.sheetpane.columnconfigure(0, weight=1)
        self.sheetpane.rowconfigure(0, weight=1)
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
        self.libraryframe = ttk.Frame(self.toolpane, padding=(5))
        self.libraryframe.grid(column=0, row=0, sticky=(N,S,E,W))
        self.libraryframe.columnconfigure(0, weight=1)
        self.libraryframe.rowconfigure(0, weight=0)
        self.libraryframe.rowconfigure(1, weight=0)
        self.libraryframe.rowconfigure(2, weight=1)

        # Add the pressure changer models section
        self.pressurechangelabel = ttk.Label(self.libraryframe, text='Pressure Changers')
        self.pressurechangelabel.grid(column=0, row=0, sticky=(W))
        self.pressureframe = ttk.Frame(self.libraryframe, padding=(2), relief="sunken")
        self.pressureframe.grid(column=0, row=1, sticky=(N,S,E,W))
        self.pumplabel = ttk.Label(self.pressureframe, text="Pump")
        self.pumplabel.grid(column=0, row=1, sticky=(W))
        self.pump_image = PhotoImage(file='graphics/Pump_Icon_Small.png')
        self.pumplabel['image'] = self.pump_image
        self.pumplabel['compound'] = "left"

    # Create flowsheet frame and contained widgets
    def create_flowsheetframe(self):

        # Create the frame
        self.flowheetframe = ttk.Frame(self.sheetpane)
        self.flowheetframe.grid(column=0,row=0, sticky='nsew')
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
