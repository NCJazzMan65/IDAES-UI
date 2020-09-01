#######################################################################################
#                                                                                     #
#                             IDAES Flowsheet Toolbox                                 #
#                                                                                     #
#  This file contains the graphical toolbox which holds draggable icons representing  #
#  the unit models, stream connectors, annotations, etc which can be placed on an     #
#  IDAES flowsheet.                                                                   #
#                                                                                     #
#  Author:  Timothy A. Fuller                                                         #
#  Date:  6/3/2020                                                                    #
#                                                                                     #
#  Version:  1.0.0                                                                    #
#                                                                                     #
#######################################################################################

"""
IDAES flowsheet editor toolbox
"""


# System imports
import sys
import os

# Module imports
from tkinter import *
from tkinter import ttk

# Add parent directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))

# Import IDAES-FE modules
from idaes_widgets.unit_models.pressure_change_models import Pump
from idaes_widgets.unit_models.reactor_models import EquilReactor
from idaes_widgets.unit_models.miscellaneous_models import FeedBlock, ProductBlock

# Define toolbox class
class Toolbox(ttk.LabelFrame):

    # Initialize this instance
    def __init__(self, master):

        # Call the parent initialize method
        super().__init__(master, text='Model Library', padding=(3,5,3,3))

        # Initialize grid
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=0)
        self.rowconfigure(4, weight=1)

        # Define display styles
        self.framestyle = ttk.Style()
        self.framestyle.configure('toolboxstyle.TFrame', 
                                    background='white', 
                                    relief='sunken')
        self.labelstyle = ttk.Style()
        self.labelstyle.configure('toolboxitemstyle.TLabel', 
                                   background='white', 
                                   padding=(2))

        # Create toolbox items
        self.create_pressure_changers()
        self.create_reactor()

    # Create pressure changer model tools
    def create_pressure_changers(self):

        # Create the pump label and frame
        self.pressurechangelabel = ttk.Label(self, 
                                             text='Pressure Changers', 
                                             padding=(3))
        self.pressurechangelabel.grid(column=0, row=0, sticky=(W))
        self.pressureframe = ttk.Frame(self, 
                                       style='toolboxstyle.TFrame', 
                                       padding=(2))
        self.pressureframe.grid(column=0, row=1, sticky=(N,S,E,W))
        self.pressureframe.columnconfigure(0, weight=1)
        self.pressureframe.rowconfigure(0, weight=0)
        self.pressureframe.rowconfigure(1, weight=1)

        # Add the pump
        self.pumpiconfile='../graphics/Pump_Icon_30x30.png'
        self.pumpicon = PhotoImage(file=self.pumpiconfile)
        self.pumptoolboxitem = ttk.Label(self.pressureframe, 
                                         text='Pump', 
                                         image=self.pumpicon, 
                                         compound='left', 
                                         style='toolboxitemstyle.TLabel')
        self.pumptoolboxitem.grid(column=0, row=0, sticky=(W))
    
    # Create reactor model tools
    def create_reactor(self):

        # Create reactor label and frame
        self.reactorlabel = ttk.Label(self, 
                                      text='Reactors', 
                                      padding=(3))
        self.reactorlabel.grid(column=0, row=2, sticky=(W))
        self.reactorframe = ttk.Frame(self, 
                                      style='toolboxstyle.TFrame', 
                                      padding=(2))
        self.reactorframe.grid(column=0, row=3, sticky=(N,S,E,W))
        self.reactorframe.columnconfigure(0, weight=1)
        self.reactorframe.rowconfigure(0, weight=0)
        self.reactorframe.rowconfigure(1, weight=0)
        self.reactorframe.rowconfigure(2, weight=0)
        self.reactorframe.rowconfigure(3, weight=1)

        # Add the equilibrium reactor
        self.equiliconfile = '../graphics/Equil_Icon_30x40.png'
        self.equilicon = PhotoImage(file=self.equiliconfile)
        self.equiltoolboxitem = ttk.Label(self.reactorframe, 
                                          text='Equilibrium', 
                                          image=self.equilicon, 
                                          compound='left', 
                                          style='toolboxitemstyle.TLabel')
        self.equiltoolboxitem.grid(column=0, row=0, sticky=(W))

        # Add the yield reactor
        self.yieldiconfile = '../graphics/Yield_Icon_30x40.png'
        self.yieldicon = PhotoImage(file=self.yieldiconfile)
        self.yieldtoolboxitem = ttk.Label(self.reactorframe,
                                          text='Yield',
                                          image=self.yieldicon,
                                          compound='left',
                                          style='toolboxitemstyle.TLabel')
        self.yieldtoolboxitem.grid(column=0, row=1, sticky=(W))

        # Add the gibbs reactor
        self.gibbsiconfile = '../graphics/Gibbs_Icon_30x40.png'
        self.gibbsicon = PhotoImage(file=self.gibbsiconfile)
        self.gibbstoolboxitem = ttk.Label(self.reactorframe,
                                          text='Gibbs',
                                          image=self.gibbsicon,
                                          compound='left',
                                          style='toolboxitemstyle.TLabel')
        self.gibbstoolboxitem.grid(column=0, row=2, sticky=(W))


