#
# Beacon Class, each one keeps track of users and the distances from it to the user along with it's coordintates
#


import sys
import math
import random

class Beacon:
    
    def __init__(self):
        self.location = [0,0]
        self.rssi = [0,0,0,0,0]
        
    def setPos(self, x, y):
        self.location = [x,y]
        
    def setRandomPos(self):
        x = random.uniform(-10, 10)
        y = random.uniform(-10, 10)
        self.location = [x,y]
        
    def getDist(self, U):
        p1 = U.location
        x = (p1[0] - self.location[0])
        y = (p1[1] - self.location[1])
        return math.fabs(math.sqrt(x*x + y*y))
        
    def getDistI(self, i):
        return self.rssi[i]
    
    def popDistPoint(self, x, y, index):
        [a,b] = self.location
        j = x - a
        k = y - b
        dis = math.fabs(math.sqrt(j*j + k*k))
        self.rssi[index] = dist
    
    def popDistPerson(self, U, index):
        popDistPoint(U.location[0], U.location[1], index)
        
    def updateRssi(self, userLoctions):
        index = 0
        for user in userLocations:
            popDistPerson(user, index)
            index += 1
        
    def updateDistPoints(self, users):
        index = 0
        for val in users:
            self.rssi[index] = val
            index += 1
        
    def setRssi(self, r, index):
        self.rssi[index] = r