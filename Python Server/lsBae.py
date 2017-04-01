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
        
    def triLat(self, b2, b3, index):
        b1L = self.location
        b2L = b2.location
        b3L = b3.location
        r1 = int(self.rssi[index])
        r2 = int(b2.rssi[index])
        r3 = int(b3.rssi[index])
        x1 = int(b1L[0])
        x2 = int(b2L[0])
        x3 = int(b3L[0])
        y1 = int(b1L[1])
        y2 = int(b2L[1])
        y3 = int(b3L[1])
        
        yP1 = (x2-x3)*((x2*x2-x1*x1)+(y2*y2-y1*y1)+(r1*r1-r2*r2))
        yP2 = (x1-x2)*((x3*x3-x2*x2)+(y3*y3-y2*y2)+(r2*r2-r3*r3))
        yP3 = 2*((y1-y2)*(x2-x3)-(y2-y3)*(x1-x2))
        
        xP1 = (y2-y3)*((y2*y2-y1*y1)+(x2*x2-x1*x1)+(r1*r1-r2*r2))
        xP2 = (y1-y2)*((y3*y3-y2*y2)+(x3*x3-x2*x2)+(r2*r2-r3*r3))
        xP3 = 2*((x1-x2)*(y2-y3)-(x2-x3)*(y1-y2))
        
        y = (-yP1+yP2)/yP3
        x = (-xP1+xP2)/xP3
        return [x,y]
        