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
from idaes_widgets.scrollable_flowsheet import ScrollableFlowsheet
from idaes_widgets.unit_models.miscellaneous_models import FeedBlock, ProductBlock
from idaes_widgets.unit_models.pressure_change_models import Pump
from idaes_widgets.unit_models.reactor_models import EquilReactor
from idaes_helpers.drag_drop import DndHandler
from idaes_widgets.flowsheet_toolbox import Toolbox


# Define the main window
class MainWindow(ttk.Frame):

    # Override initialization method
    def __init__(self, master = None):

        # Set master window
        super().__init__(master)
        self.master = master
        self.master.title('IDAES Flowsheet Editor')
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.master.geometry('640x480+30+30')
        self.master.option_add('*tearOff',FALSE)
        self.mastercontent = ttk.PanedWindow(self.master, orient=HORIZONTAL)
        self.mastercontent.grid(column=0, row=0, sticky=(N,S,E,W))

        # Create main menu
        self.create_menu()

        # Create main display areas
        self.create_main_areas()

        # Create flowsheet editing notebook
        self.create_flowsheet_notebook()
        
    # Method to create the main menu
    def create_menu(self):
       
        # Define main menu bar
        self.mainmenu = Menu(self.master)
        self.master['menu'] = self.mainmenu

        # Define File menu
        self.menu_file = Menu(self.mainmenu)
        self.menu_file.add_command(label='New', command=self.create_new_flowsheet)
        self.menu_file.add_separator()
        self.menu_file.add_command(label="Open...")
        self.mainmenu.add_cascade(menu=self.menu_file, label='File')

        # Define Edit menu
        self.menu_edit = Menu(self.mainmenu)
        self.mainmenu.add_cascade(menu=self.menu_edit, label='Edit')

    # Create the library frame and contained widgets
    def create_main_areas(self):

        # Create the model library
        self.librarybox = Toolbox(master=self.mastercontent)
        self.mastercontent.add(self.librarybox, weight=1)

        # Create the flowsheet editor frame
        self.flowsheetframe = ttk.Frame(self.mastercontent, padding=(5))
        self.mastercontent.add(self.flowsheetframe, weight=3)
        self.flowsheetframe.columnconfigure(0, weight=1)
        self.flowsheetframe.rowconfigure(0, weight=1)
        
    # Create flowsheet tabs
    def create_flowsheet_notebook(self):

        # Add the flowsheet notebook widget
        self.fsnotebook = ttk.Notebook(self.flowsheetframe)
        self.fsnotebook.grid(column=0, row=0, sticky=(N,S,E,W))
        self.fsnotebook.columnconfigure(0, weight=1)
        self.fsnotebook.rowconfigure(0, weight=1)

    # Create new flowsheet
    def create_new_flowsheet(self):

        # Create a new frame and add to notebook
        self.newtab = ttk.Frame(self.fsnotebook, padding=(5))
        self.newtab.grid(column=0, row=0, sticky=(N,S,E,W))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.fsnotebook.add(self.newtab, text="Flowsheet 1")

        # Add a new flowsheet canvas to notebook frame
        self.flowsheet = ScrollableFlowsheet(self.newtab)
        self.flowsheet.grid(column=0, row=0, sticky=(N,S,E,W))

        # Add test widget to flowsheet canvas
        #self.pump101 = Pump(name="Pump101", height=100, width=100)
        #self.pump101.attach(self.flowsheet.flowsheet)

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
