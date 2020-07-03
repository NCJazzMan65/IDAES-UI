#############################################################################
#                                                                           #
#                       IDAES Draggable Widget                              #
#                                                                           #
#  This file contains a draggable widget class which is used as a base      #
#  class for all unit model widgets in the IDAES Flowsheet Editor program.  #
#                                                                           #
#  Author:  Timothy A. Fuller                                               #
#  Date:  6/11/2020                                                         #
#                                                                           #
#  Version:  1.0.0                                                          #
#                                                                           #
#############################################################################

"""
Draggable widget base class for all IDAES Flowsheet Editor unit model widgets
"""


# System imports
import sys
import os

# Module imports
import tkinter
from tkinter import ttk

# Add parent directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))

# IDAES FE module imports
from idaes_helpers.drag_drop import DndHandler

# Declare exported methods
__all__ = ["dnd_start", "DndHandler"]


# Factory method for drag-drop handler
def dnd_start(source, event):
    h = DndHandler(source, event)
    if h.root:
        return h
    else:
        return None


# Define the draggable widget class
class DraggableWidget:

    # Initialize this instance
    def __init__(self, name, icon, height=50, width=50, orient="top"):

        # Create instance variables
        self.name = name
        self.icon = icon
        self.height = height
        self.width = width
        self.orient = orient
        self.canvas = None
        self.label = None
        self.id = None
    
    # Method to drop widget in new location
    def attach(self, canvas, x=10, y=10):
        if canvas is self.canvas:
            self.canvas.coords(self.id, x, y)
            return
        if self.canvas:
            self.detach()
        if not canvas:
            return
        label = tkinter.Label(canvas, text=self.name, image=self.icon, compound=self.orient,
                              borderwidth=2, relief="raised", 
                              height=self.height, width=self.width)
        id = canvas.create_window(x, y, window=label, anchor="nw")
        self.canvas = canvas
        self.label = label
        self.id = id
        label.bind("<ButtonPress>", self.press)

    # Method to remove widget from original location at drag start
    def detach(self):
        canvas = self.canvas
        if not canvas:
            return
        id = self.id
        label = self.label
        self.canvas = self.label = self.id = None
        canvas.delete(id)
        label.destroy()

    # Method to handle mouse button press at drag start 
    def press(self, event):
        if dnd_start(self, event):
            # where the pointer is relative to the label widget:
            self.x_off = event.x
            self.y_off = event.y
            # where the widget is relative to the canvas:
            self.x_orig, self.y_orig = self.canvas.coords(self.id)

    # Method to handle dragging the widget
    def move(self, event):
        x, y = self.where(self.canvas, event)
        self.canvas.coords(self.id, x, y)

    # Method to put the widget back to its original position
    def putback(self):
        self.canvas.coords(self.id, self.x_orig, self.y_orig)

    # Method to determine where dragged widget is
    def where(self, canvas, event):
        # where the corner of the canvas is relative to the screen:
        x_org = canvas.winfo_rootx()
        y_org = canvas.winfo_rooty()
        # where the pointer is relative to the canvas widget:
        x = event.x_root - x_org
        y = event.y_root - y_org
        # compensate for initial pointer offset
        return x - self.x_off, y - self.y_off

    # Method to end drag-drop
    def dnd_end(self, target, event):
        pass

