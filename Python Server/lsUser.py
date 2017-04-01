#
# User Class, can call for help and stores their location
#

import sys
import math
import random

class User:

    def __init__(self):
        self.location = [0,0]
        self.needsHelp = False
    
    def setPos(self, x, y):
        self.location = [x,y]
    
    def wantHelp(self):
        self.needsHelp = True
    
    def isHelped(self):
        self.needsHelp = False
        
    def setRandomPos(self):
        x = random.uniform(-10, 10)
        y = random.uniform(-10, 10)
        self.location = [x,y]