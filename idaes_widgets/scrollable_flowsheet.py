########################################################################
#                                                                      #
#                    IDAES Scrollable Flowsheet                        #
#                                                                      #
#  This file contains a custom scrollable flowsheet widget used in     #
#  the IDAES Flowsheet Editor program.  The flowsheet is built upon    #
#  a tkinter canvas widget.  This custom widget creation and editiing  #
#  of process model flowsheets.                                        #
#                                                                      #
#  Author:  Timothy A. Fuller                                          #
#  Date:  5/7/2020                                                     #
#                                                                      #
#  Version:  1.0.0                                                     #
#                                                                      #
########################################################################


# System module imports
import sys
import os

# Module imports
from tkinter import *
from tkinter import ttk


# Define the scrollable flowsheet class
class ScrollableFlowsheet(Frame):

    # Override initialization method
    def __init__(self, master = None):

        # Initialize variables
        self.canvas_height = 2000
        self.canvas_width = 2000
        self.grid_step = 20

        # Set the parent window
        super().__init__(master)
        self.master = master
        self.master.columnconfigure(0,weight=1)
        self.master.columnconfigure(1, weight=0)
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=0)

        # Create a canvas
        self.flowsheet = Canvas(self.master, scrollregion=(0,0,self.canvas_width,self.canvas_height))
        self.flowsheet['bg'] = 'white'
        self.flowsheet.grid(column=0, row=0, sticky=(N,S,E,W))
        self.flowsheet.dnd_accept = self.dnd_accept

        # Create scrollbars
        self.vert_scroll = ttk.Scrollbar(self.master, orient=VERTICAL, command=self.flowsheet.yview)
        self.vert_scroll.grid(column=1, row=0, sticky=(N,S))
        self.horiz_scroll = ttk.Scrollbar(self.master, orient=HORIZONTAL, command=self.flowsheet.xview)
        self.horiz_scroll.grid(column=0, row=1, sticky=(E,W))
        self.flowsheet['yscrollcommand'] = self.vert_scroll.set
        self.flowsheet['xscrollcommand'] = self.horiz_scroll.set

        # Create an alignment grid
        x_limit = int((self.canvas_width / self.grid_step) - 1)
        y_limit = int((self.canvas_height / self.grid_step) - 1)
        for i in range(1, x_limit):
            for j in range(1, y_limit):
                x = i * self.grid_step
                y = j * self.grid_step
                self.flowsheet.create_rectangle(x, y, x+1, y+1, outline='gray', fill='gray')

    # Define the drag-drop accept method
    def dnd_accept(self, source, event):
        return self

    # Define drag-drop enter method
    def dnd_enter(self, source, event):
        #self.flowsheet.focus_set() # Show highlight border
        x, y = source.where(self.flowsheet, event)
        x1, y1, x2, y2 = source.canvas.bbox(source.id)
        dx, dy = x2-x1, y2-y1
        self.dndid = self.flowsheet.create_rectangle(x, y, x+dx, y+dy)
        self.dnd_motion(source, event)

    # Define drag-drop in motion method
    def dnd_motion(self, source, event):
        x, y = source.where(self.flowsheet, event)
        x1, y1, x2, y2 = self.flowsheet.bbox(self.dndid)
        self.flowsheet.move(self.dndid, x-x1, y-y1)

    # Define drag-drop leave method
    def dnd_leave(self, source, event):
        #self.top.focus_set() # Hide highlight border
        self.flowsheet.delete(self.dndid)
        self.dndid = None

    # Define drag-drop commit method
    def dnd_commit(self, source, event):
        self.dnd_leave(source, event)
        x, y = source.where(self.flowsheet, event)
        source.attach(self.flowsheet, x, y)