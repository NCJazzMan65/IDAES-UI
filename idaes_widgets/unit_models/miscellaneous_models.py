##########################################################################
#                                                                        #
#                     IDAES Miscellaneous Unit Models                    #
#                                                                        #
#  This file contains a number of miscellaneous unit models used in the  #
#  IDAES Flowsheet Editor program.                                       #
#                                                                        #
#  The unit models provided include:                                     #
#    - Feed Block                                                        #
#    - Feed Block with Flash                                             #
#    - Product Block                                                     #
#                                                                        #
#  Author:  Timothy A. Fuller                                            #
#  Date:  6/3/2020                                                       #
#                                                                        #
#  Version:  1.0.0                                                       #
#                                                                        #
##########################################################################

"""
Miscellaneous unit operations model widgets for the IDAES Flowsheet Editor
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
class FeedBlock(DraggableWidget):

    # Initialize this instance
    def __init__(self, name):

        # Call parent initialize method
        icon = PhotoImage(file='../graphics/Feed_Block_Icon.png')
        super().__init__(name, icon)


# Define product block class
class ProductBlock(DraggableWidget):

    # Initialize this instance
    def __init__(self, name):

        # Call parent initialize method
        icon = PhotoImage(file='../graphics/Product_Block_Icon.png')
        super().__init__(name, icon)