#
# Emulates the desktop/android application functionality that the customer service rep
# or shift manager would have. Allows them to dispatch employees to specific users who
# need help based on the user's location and employees area of expertise. Quite basic 
# in it's current form, documentation exists on future improvements.
#

import sys
import math
from lsUser import User
from lsBS import Empl
from lsBae import Beacon

c1 = User()
c2 = User()
e1 = Empl()
e2 = Empl()
e3 = Empl()
b1 = Beacon()
b2 = Beacon()
b3 = Beacon()

store = [c1.location,c2.location,e1.location,e2.location,e3.location]
status = [c1.needsHelp,c2.needsHelp,e1.isBusy or e1.isHelping, e2.isBusy or e2.isHelping,e3.isBusy or e3.isHelping]
rssi = [b1.rssi, b2.rssi, b3.rssi]

def getDis(U, E):
    [x,y] = getVec(U, E)
    return math.fabs(math.sqrt(x*x + y*y))
    
def getVec(U, E):
    p1 = U.location
    p2 = E.location
    x = (p1[0] - p2[0])
    y = (p1[1] - p2[1])
    return [x,y]

def updateStore():
    global store 
    store = [c1.location, c2.location, e1.location, e2.location, e3.location]
    
def updateStoreFile(fileName):
    global c1
    global c2
    global e1
    global e2
    global e3
    global b1
    global b2
    global b3
    
    f = open(fileName, 'r')
    for line in f:
        l = line.split(";")
        xy = l[1].split(",")
        
        exec(l[0] + ".setPos(int(xy[0]),int(xy[1]))")
        
        if len(l) == 3: #User
            if int(l[2]):
                exec(l[0] + ".wantHelp()")
            else:
                exec(l[0] + ".isHelped()")
        elif len(l) == 4: #Empl
            if int(l[2]):
                exec(l[0] + ".Helping()")
            else:
                exec(l[0] + ".doneHelping()")
            if int(l[3]):
                exec(l[0] + ".Busy()")
            else:
                exec(l[0] + ".notBusy()")
        else: #beacon
            ar = [int(l[2]),int(l[3]),int(l[4]),int(l[5]),int(l[6])]
            exec(l[0] + ".updateDistPoints(ar)")
        
    updateStore()
    updateStatus()
    updateRssi()
    
def updateStatus():
    global status 
    status = [c1.needsHelp, c2.needsHelp, e1.isBusy or e1.isHelping, e2.isBusy or e2.isHelping, e3.isBusy or e3.isHelping]
    
def updateRssi():
    global rssi
    rssi = [b1.rssi, b2.rssi, b3.rssi]

# Track Blue Shirts
#   Get info on each one
# Track User
# Alert when User asks for help
# 

def main():
    global c1
    global c2
    global e1
    global e2
    global e3
    global b1
    global b2
    global b3
    
    c1.setPos(-5,2)
    c2.setRandomPos()
    e1.setPos(0,2)
    e2.setRandomPos()
    e3.setRandomPos()
    b1.setPos(10,10)
    b2.setPos(-10,-10)
    b1.setRssi(4.912481378, 0)
    b1.setRssi(12.8062, 2)
    b2.setRssi(13, 0)
    b2.setRssi(15.6205, 2)
    
    c1.wantHelp()
    e3.Busy()
    
    updateStore()
    updateStatus()
    
    print ""
    print ""
    print ""
    
    print "Example values of where people can be in the store: ", store
    print "Example array showing if people are busy or not: ", status
    print "Some possible RSSI values: ", rssi
    print "Able to get the distance between the first and third user in the store: ", getDis(c1, e1)
    print "Also able to express this as a directional vector: ", getVec(c1, e1)
    
    updateStoreFile('store')
    
    print ""
    print "Location of people in the store loaded from an external source: ", store
    print "Is a person busy (also loaded externally)? ", status
    print "Reset RSSI values for everyone: ", rssi
    
    print ""
    print ""
    print ""
    print ""
    print ""
    
    b1.setRssi(5,0)
    b1.setRssi(math.sqrt(146),1)
    b1.setRssi(9*math.sqrt(2),2)
    b2.setRssi(5,0)
    b2.setRssi(5*math.sqrt(2),1)
    b2.setRssi(3*math.sqrt(10),2)
    b3.setRssi(5,0)
    b3.setRssi(math.sqrt(34),1)
    b3.setRssi(math.sqrt(10),2)
    b1.setPos(-5,5)
    b2.setPos(1,5)
    b3.setPos(1,-3)
    
    updateRssi()
    
    print "Beacon locations in the store: ", b1.location, b2.location, b3.location
    print "Beacon Signal Strength to a specific user: ", b1.rssi[0], b2.rssi[0], b3.rssi[0]
    print "User's Location: ",b1.triLat(b2,b3, 0)
    print ""
    print "Beacon Signal Strenth to another user: ", b1.rssi[1], b2.rssi[1], b3.rssi[1]
    print "Second User's Location: ", b1.triLat(b2,b3, 1)
    print ""
    print "Beacon Signal Strength to a third user: ", b1.rssi[2], b2.rssi[2], b3.rssi[2]
    print "Third User's Locations: ", b1.triLat(b2,b3, 2)
    
    
    print ""
    print ""
    print ""
    print ""
    print ""
    
    
    
    
    
    
if __name__ == '__main__':
    print ""
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("\nUser keyboard interrupt")