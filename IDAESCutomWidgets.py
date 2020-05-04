#######################################################################
#                                                                     #
#                      IDAES Custom Widgets                           #
#                                                                     #
#  This file contains a number of custom widget classes used in the   #
#  IDAES Flowsheet Editor program                                     #
#                                                                     #
#  Author:  Timothy A. Fuller                                         #
#  Date:  5/4/2020                                                    #
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


# Define the scrollable listbox class
class ScrollableListbox(Frame):

    # Override initialization method
    def __init__(self, master = None):

        # Set the parent window
        self.master = master