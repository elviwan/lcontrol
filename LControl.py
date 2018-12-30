# This will be the main module that links up the GUI and https server

import time
import logging
import sys, os
from queue import Queue
from threading import Thread

loggingLevel = logging.INFO
if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the pyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app
    # path into variable _MEIPASS'.
    application_path = sys._MEIPASS
    sys.release = True

else:
    # We do not need to do this when it is an exe
    # This is because our exe should have the right package
    # Add lib directory to module search path
    parent_dir = os.path.abspath(os.path.dirname(__file__))
    lib_dir = os.path.join(parent_dir, 'packages')
    # We insert our own libraries with our own modifications first
    # This way, the interpreter uses our libraries instead of the
    # ones that may exist on our machine
    sys.path.insert(0,lib_dir)

    loggingLevel = logging.DEBUG
    application_path = os.path.dirname(os.path.abspath(__file__))
    sys.release = False

# We import our custom packages last
import pyautogui

# We also import our local packages
import netifaces

# GLOBAL CONSTANTS
ADDR = 'addr'


logging.getLogger()
logging.basicConfig(format='%(levelname)s: %(message)s', level=loggingLevel)

if sys.release:
    logging.debug( "Failsafe disabled" )
    pyautogui.FAILSAFE = False
    pyautogui.PAUSE = 0

elif not sys.release:
    logging.info( "Failsafes enabled" )
    logging.info( "Move mouse to upper-left corner to abort" )

def getInterfaceAddr():
    ''' Used to get interface addresses (both IPv4 and IPv6)
        Input: None
        Output: List of dictionaries with list of addresses
        Output is a list -> dict -> list
        Reason: Some interfaces may have multiple addresses
                (Point to point)

        Example (Access first interface's list of IPv4 address)
        inf[0][netifaces.AF_INET]
        Example (Access last interface's list of IPv6 address)
        inf[-1][netifaces.AF_INET6]
    '''
    inf = []
    for i in netifaces.interfaces():
        interface = netifaces.ifaddresses(i)
        d = {}
        if netifaces.AF_INET in interface:
            for a in interface[netifaces.AF_INET]:
                if ADDR in a:
                    if netifaces.AF_INET not in d:
                        d[netifaces.AF_INET] = []
                    d[netifaces.AF_INET].append(a[ADDR])

        if netifaces.AF_INET6 in interface:
            for a in interface[netifaces.AF_INET6]:
                if ADDR in a:
                    if netifaces.AF_INET6 not in d:
                        d[netifaces.AF_INET6] = []
                    d[netifaces.AF_INET6].append(a[ADDR])
        inf.append(d)
    return inf

class LControl():
    def __init__( self ):
        self.q = Queue()
        self.run = False
        self.started = False

    def moveDrag( self, x, y, move="move", duration=0.5 ):
        # Line 821/822 are commented out in __init__.py for pyAutoGui
        # This allows us to move between monitors
        try:
            x = int( x )
            y = int( y )
        except:
            logging.warning( str( __name__ ) + " Received: " + str( x ) + " " + str( y ) )
            return False

        if move == "move":
            logging.debug( "Moving to coordinates: " + str( x ) + " " + str( y ) )
            pyautogui.moveRel( x, y, 0.5 )
        elif move == "drag":
            logging.debug( "Dragging to coordinates: " + str( x ) + " " + str( y ) )
            pyautogui.dragRel( x, y, 0.5 )
        else:
            logging.error( "moveDrag - Received: " + str( move ) )
            return False

        return True

    # We should rename this (maybe)
    def _serve_forever( self ):
        while self.run:
            args = [ None, None, "move", 0.5 ]
            item = self.q.get( block=True )
            if type( item ) != tuple:
                continue
            if len( item ) < 2 and len( item ) > 4:
                continue
            for i, itm in enumerate( item ):
                args[i] = itm
            self.moveDrag( args[0], args[1], args[2], args[3] )
        # Signals that we have finally stopped
        self.started = False

    def addRequest( self, item ):
        if not self.started:
            logging.error( "LControl not started. Please start first" )
            return False
        self.q.put( item )
        logging.debug( "addRequest - Added to queue: " + str(item) )
        return True

    def start( self ):
        if self.started:
            return False
        # Signals to not start another one
        self.started = True
        # Signals we are running
        self.run = True
        t = Thread( target=self._serve_forever )
        t.start()
        return True

    def stop( self ):
        # Signals to stop running
        self.run = False
        # We add an item to stop the blocking call "get"
        self.addRequest( "quit" )

def main():
    interfaces = getInterfaceAddr()
    # Example of accessing interfaces
    for i in interfaces:
        if netifaces.AF_INET in i:
            print ( i[netifaces.AF_INET][0] )
        if netifaces.AF_INET6 in i:
            print ( i[netifaces.AF_INET6][0] )
    # Another example: equivalent to the above
    # for i in interfaces:
    #     for val in i:
    #         print (i[val][0])
    lcontrol = LControl()
    try:
        lcontrol.start()
        lcontrol.q.put((100, 0))
        lcontrol.q.put((1000, 0))
        lcontrol.q.put(("-1000", "0"))
        while True:
            time.sleep(1000000)
    except:
        lcontrol.stop()

if __name__ == '__main__':
    main()

