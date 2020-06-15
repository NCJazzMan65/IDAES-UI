#########################################################################
#                                                                       #
#                IDAES Pressure Change Unit M                           #
#                                                                       #
#  This file contains several pressure change unit model widgets used   #
#  in the IDAES Flowsheet Editor program.  Theses widgets contain       #
#  methods for specifying the configuration of the specific unit model  #
#  and methods for supporting drag-drop operations on the flowsheet.    #
#                                                                       #
#  Unit model widgets included in this file are:                        #
#    - Compressor                                                       #
#    - Pressure Changer                                                 #
#    - Pump                                                             #
#    - Turbine                                                          #
#                                                                       #
#  Author:  Timothy A. Fuller                                           #
#  Date:  6/3/2020                                                      #
#                                                                       #
#  Version:  1.0.0                                                      #
#                                                                       #
#########################################################################

"""
Pressure change unit operation model widgets for the IDAES Flowsheet Editor
"""


# System imports
import sys
import os

# Module imports
from tkinter import *
from tkinter import ttk

# Add parent directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))

# IDAES FE module imports
from idaes_widgets.draggable_widget import DraggableWidget


# Define the pump class
class Pump(DraggableWidget):

    # Initialize this instance
    def __init__(self, name):
        
        # Call parent initialize method
        icon = PhotoImage(file='../graphics/Pump_Icon.png')
        super().__init__(name, icon)