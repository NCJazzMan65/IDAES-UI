###################################################################
#                                                                 #
#                   IDAES Feed Block Unit Model                   #
#                                                                 #
#  This file contains a feed block unit model widget used in the  #
#  IDAES Flowsheet Editor program.  The feed block model widget   #
#  contains methods for specifying the configuration of the feed  #
#  block and methods for supporting drag-drop operations on the   #
#  flowsheet.                                                     #
#                                                                 #
#  Author:  Timothy A. Fuller                                     #
#  Date:  5/29/2020                                               #
#                                                                 #
#  Version:  1.0.0                                                #
#                                                                 #
###################################################################

"""
Feed Block unit operations model widget for the IDAES Flowsheet Editor
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

