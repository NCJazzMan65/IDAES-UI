#######################################################################
#                                                                     #
#                    IDAES Scrollable Listbox                         #
#                                                                     #
#  This file contains a custom scrollable listbox widget used in the  #
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

        # Initialize class variables
        self.listitems = StringVar()

        # Set the parent window
        super().__init__(master)
        self.master = master
        self.master.columnconfigure(0,weight=1)
        self.master.columnconfigure(1, weight=1)
        self.master.rowconfigure(0, weight=1)

        # Create the listbox
        self.listbox = Listbox(self.master, listvariable=self.listitems)
        self.listbox.grid(column=0, row=0, sticky=(N,S,E,W))

        # Create the scrollbar and tie it to listbox
        self.listscroll = ttk.Scrollbar(self.master, orient=VERTICAL, command=self.listbox.yview)
        self.listscroll.grid(column=1, row=0, sticky=(N,S))
        self.listbox['yscrollcommand'] = self.listscroll.set