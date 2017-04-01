#
# Employee Class, can respond to help and be busy
#

import sys
import math
import random

class Empl:

    def __init__(self):
        self.location = [0,0]
        self.isHelping = False
        self.isBusy = False
    
    def setPos(self, x, y):
        self.location = [x,y]
    
    def isHelping(self):
        self.needsHelp = True
    
    def doneHelping(self):
        self.needsHelp = False
        
    def Busy(self):
        self.isBusy = True
        
    def notBusy(self):
        self.isBusy = False
        
    def setRandomPos(self):
        x = random.uniform(-10, 10)
        y = random.uniform(-10, 10)
        self.location = [x,y]