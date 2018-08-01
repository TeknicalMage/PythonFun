import sys

try:
    import launchpad_py as launchpad
except ImportError:
    try:
        import launchpad
    except ImportError:
        sys.exit("error loading launchpad.py")

import random
from pygame import time

def loop1():
    main2()
    loop2()
    
def loop2():
    loop1()
 
def main():

    mode = ("Mk1")

    # create an instance
    lp = launchpad.Launchpad();

    # check what we have here and override lp if necessary
    lp.Open( name = "Launchpad Mini", number = 0)
    print("Launchpad Mk1/S/Mini")
    mode = "Mk1"
            
    if mode is None:
        print("Did not find any Launchpads, meh...")
        return

    if mode == "Mk1":
        lp.LedCtrlString( "TEK TEK TEK TEK TEK TEK TEK TEK TEK TEK TEK TEK TEK TEK TEK TEK TEK TEK", 8, 0, -1 )
                
    lp.Reset() # turn all LEDs off
    lp.Close() # close the Launchpad (will quit with an error due to a PyGame bug)

    
def main2():
    mode = "Mk1"
    lp = launchpad.Launchpad();
    lp.Open( name = "Launchpad Mini", number = 0)
    if mode == "Mk1":
        lp.LedCtrlString( "TEK TEK TEK TEK TEK TEK TEK TEK TEK TEK TEK TEK TEK TEK TEK TEK TEK TEK ", 8, 0, -1 )    



if __name__ == '__main__':
    main()
    main2()
    loop1()
    
