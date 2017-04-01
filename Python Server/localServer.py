#
# Emulates the desktop/android application functionality that the customer service rep
# or shift manager would have. Allows them to dispatch employees to specific users who
# need help based on the user's location and employees area of expertise. Quite basic 
# in it's current form, documentation exists on future improvements.
# 
# 
#

import socket
import sys
import math
from lsUser import User
from lsBS import Empl


# Track Blue Shirts
#   Get info on each one
# Track User
# Alert when User asks for help
# 



def main():
    
    c1 = User()
    c2 = User()
    e1 = Empl()
    e2 = Empl()
    e3 = Empl()
    
    c2.wantHelp()
    e3.Busy()

    
    
    
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("\nUser keyboard interrupt")