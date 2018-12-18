import pyautogui
import time
import logging
import sys, os

if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the pyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app
    # path into variable _MEIPASS'.
    application_path = sys._MEIPASS
    sys.release = True

else:
    application_path = os.path.dirname(os.path.abspath(__file__))
    sys.release = False

logging.getLogger()
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

if sys.release:
    logging.debug( "Failsafe disabled" )
    pyautogui.FAILSAFE = False
    pyautogui.PAUSE = 0

elif not sys.release:
    logging.info( "Failsafes enabled" )
    logging.info( "Move mouse to upper-left corner to abort" )

if sys.modules['__main__'].__file__ != __file__:
    sys.exit(0)
    # Leaves if this is being called from another file
    # Test that our own sys.release variable works in other files
    # This way we can distinguish test code from release code

run = True
print( "Enter 'q' to quit")
print( "Ex. Enter x and y coords: 10 -10" )
x = 0
y = 0
while run:
    coords = input( "Enter x and y coords:" )
    if coords == 'q':
        run = False
        continue
    coords = coords.split(" ")
    try:
        x = int(coords[0])
        y = int(coords[1])
    except:
        continue

    pyautogui.moveRel(x, y, 0.5)
