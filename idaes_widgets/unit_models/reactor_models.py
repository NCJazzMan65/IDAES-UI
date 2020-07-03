#############################################################################
#                                                                           #
#                       IDAES Reactor Unit Models                           #
#                                                                           #
#  This file contains several different reactor unit model widgets used in  #
#  the IDAES Flowsheet Editor program. These reactor model widgets contain  #
#  methods for specifying the configuration of the specific reactor and     #
#  reactor and methods for supporting drag-drop operations on the           #
#  flowsheet.                                                               #
#                                                                           #
#  Unit model widgets included in this file are:                            #
#    - Continuous Stirred Tank Reactor                                      #
#    - Equilibrium Reactor                                                  #
#    - Gibbs Reactor                                                        #
#    - Plug Flow Reactor                                                    #
#    - Stoichionetric (Yield) Reactor                                       #
#                                                                           #
#  Author:  Timothy A. Fuller                                               #
#  Date:  6/3/2020                                                          #
#                                                                           #
#  Version:  1.0.0                                                          #
#                                                                           #
#############################################################################

"""
Equilibrium Reactor unit operations model widget for the IDAES Flowsheet Editor
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


# Define feed block class
class EquilReactor(DraggableWidget):

    # Initialize this instance
    def __init__(self, name, height=50, width=50, orient="top"):

        # Call parent initialize method
        icon = PhotoImage(file='../graphics/Equil_Reactor_Icon.png')
        super().__init__(name, icon, height, width, orient)