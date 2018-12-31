#!/usr/bin/env python3
# This will be the main module that links up the GUI and https server

import time
import logging
import sys, os
from queue import Queue
from threading import Thread

import pyautogui
from patches.monkeyPatches import mouseMoveDragPatch

pyautogui._mouseMoveDrag = mouseMoveDragPatch

loggingLevel = logging.INFO
if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the pyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app
    # path into variable _MEIPASS'.
    application_path = sys._MEIPASS
    sys.release = True

else:
    loggingLevel = logging.DEBUG
    application_path = os.path.dirname(os.path.abspath(__file__))
    sys.release = False

logging.getLogger()
logging.basicConfig(format='%(levelname)s: %(message)s', level=loggingLevel)

if sys.release:
    logging.debug( "Failsafe disabled" )
    pyautogui.FAILSAFE = False
    pyautogui.PAUSE = 0

elif not sys.release:
    logging.info( "Failsafes enabled" )
    logging.info( "Move mouse to upper-left corner to abort" )

class LControl():
    def __init__( self ):
        self.q = Queue()
        self.run = True

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
            logging.error( str( __name__ ) + " Received: " + str( move ) )
            return False

        return True

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

    def serve_forever( self ):
        t = Thread(target=self._serve_forever)
        t.start()

def main():
    lcontrol = LControl()
    try:
        lcontrol.serve_forever()
        lcontrol.q.put((100, 0))
        lcontrol.q.put((1000, 0))
        lcontrol.q.put(("-1000", "0"))
        while True:
            time.sleep(1000000)
    except:
        lcontrol.run = False
        lcontrol.q.put("quit")

if __name__ == '__main__':
    main()

