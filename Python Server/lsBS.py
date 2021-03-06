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
        self.distances = [0,0,0,0,0]
    
    def setPos(self, x, y):
        self.location = [x,y]
        
    def getPos(self):
        return self.location
    
    def Helping(self):
        self.isHelping = True
    
    def doneHelping(self):
        self.isHelping = False
        
    def Busy(self):
        self.isBusy = True
        
    def notBusy(self):
        self.isBusy = False
        
    def setRandomPos(self):
        x = round(random.uniform(-10, 10))
        y = round(random.uniform(-10, 10))
        self.location = [x,y]