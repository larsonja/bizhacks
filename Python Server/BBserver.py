#
# Quick code to emulate the Best Buy server which would send data to their application.
# Responds to a request from the Android Application for the user's current store's BLE
# beacon locations. Would be implemented in a better way in the future to allow multiple
# connections as well as repeated request from the application in case the app fails a 
# connection and needs to do another request before the server restarts. Additionally the
# current beaconData file should be an SQL database and not a regular file.
#

import socket
import sys

host = "128.189.86.89"
port = 32694

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Socket made"

    try:
        s.bind((host, port))
    except socket.error as msg:
        print 'Bind failed. Error Code: ' + str(msg[0]) + ' Message was: ' + msg[1]
        sys.exit(0)
        
    print "Bind successful " + str(host) + ' ' + str(port)

    s.listen(5)
    print "Now Listening"
    conn, addr = s.accept()
    print "Connected by: ", addr

    while True:
        data = conn.recv(1024)
        if len(msg) != 0:
            print "Recieved: " + msg
            if msg != "1":
                break
            else:
                conn.send("2")
                location = conn.recv()
                
                f = open('beaconData', 'r')
                for line in f:
                    if line.startswith("<" + location + ">"):
                        response = line.split(">")
                        
                        if response:
                            resp = ""
                            c = 0
                            while resp != len(response[1]):#should respond the number of characters it recieves
                                conn.send(response[1])
                                resp = self.recv()
                                c += 1
                                if c == 5: #try 5 times
                                    conn.send("-1")
                                    conn.close()
                    conn.send("-2")
                    conn.close()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("\nUser keyboard interrupt")