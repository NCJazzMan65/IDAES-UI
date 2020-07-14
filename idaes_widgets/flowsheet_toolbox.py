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
    def __ini__(self, master, name):

        # Call the parent initialize method
        super().__init__(master, text=name, padding=(5))

        # Initialize grid
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=0)
        self.rowconfigure(4, weight=0)
        self.rowconfigure(5, weight=1)

        # Create toolbox items

    # Create pressure changer model tools
    def create_pressure_changers(self):

        self.pressurechangelabel = ttk.Label(self, text='Pressure Changers', padding=(2))
        self.pressurechangelabel.grid(column=0, row=0, sticky=(W))
        self.pressureframe = ttk.Frame(self, padding=(2), relief="sunken")
        self.pressureframe.grid(column=0, row=1, sticky=(N,S,E,W))
        self.pressureframe.columnconfigure(0, weight=1)
        self.pressureframe.rowconfigure(0, weight=1)
        self.pumpcanvas = Canvas(self.pressureframe, width=100)
        self.pumpcanvas.grid(column=0, row=0, sticky=(N,S,E,W))
        self.pumpicon = Pump(name="Pump", height=50, width=100, orient="left")
        self.pumpicon.attach(self.pumpcanvas)

