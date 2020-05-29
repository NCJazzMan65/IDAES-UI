######################################################################
#                                                                    #
#                   IDAES Feed Block Unit Model                      #
#                                                                    #
#  This file contains a product block unit model widget used in the  #
#  IDAES Flowsheet Editor program.  The product block model widget   #
#  contains methods for specifying the configuration of the product  #
#  block and methods for supporting drag-drop operations on the      #
#  flowsheet.                                                        #
#                                                                    #
#  Author:  Timothy A. Fuller                                        #
#  Date:  5/29/2020                                                  #
#                                                                    #
#  Version:  1.0.0                                                   #
#                                                                    #
######################################################################

"""
Product Block unit operations model widget for the IDAES Flowsheet Editor
"""


# System imports
import sys

# Module imports
from tkinter import *
from tkinter import ttk


# Define feed block class
class ProductBlock:

    # Initialize this instance
    def __init__(self, name):

        # Create instance variables
        self.name = name
        self.canvas = None
        self.button = None
        self.id = None
        self.icon = PhotoImage(file='../graphics/Product_Block_Icon.png')