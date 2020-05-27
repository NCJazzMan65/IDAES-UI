########################################################################
#                                                                      #
#                       IDAES Pump Unit Model                          #
#                                                                      #
#  This file contains a pump unit model widget used in the IDAES       #
#  Flowsheet Editor program.  The pump model widget contains methods   #
#  for specifying the configuration of the pump and methods for        #
#  supporting drag-drop operations on the flowsheet.                   #
#                                                                      #
#  Author:  Timothy A. Fuller                                          #
#  Date:  5/21/2020                                                     #
#                                                                      #
#  Version:  1.0.0                                                     #
#                                                                      #
########################################################################

"""
Pump unit operations model widget for theIDAES Flowsheet Editor
"""


# System imports
import sys


# Define the pump class
class Pump:

    # Initialize this instance
    def __init__(self, name):
        self.name = name
        self.canvas = None
        self.button = None
        self.id = None