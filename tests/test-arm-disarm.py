#!/usr/bin/env python

"""test-send.py: Test script to send RC commands to a MultiWii Board."""

__author__ = "Aldo Vargas"
__copyright__ = "Copyright 2016 Altax.net"

__license__ = "GPL"
__version__ = "1"
__maintainer__ = "Aldo Vargas"
__email__ = "alduxvm@gmail.com"
__status__ = "Development"

__modified_by__ = "Curtis Wang, ycwang@u.northwestern.edu, for Python 3.5+"

from pymultiwii import MultiWii
import time

if __name__ == "__main__":

    #board = MultiWii("/dev/tty.usbserial-AM016WP4")
    board = MultiWii("/dev/tty.SLAB_USBtoUART")
    try:
        board.arm()
        print("Board is armed now!")
        print("In 3 seconds it will disarm...")
        time.sleep(3)
        board.disarm()
        print("Disarmed.")
        time.sleep(3)

    except Exception as error:
        print("Error on Main: "+str(error))

"""
# data = [roll, pitch, yaw, throttle, aux1-4]
data = [1500,1500,1500,1200,1000,1000,1000,1000]
            
board.sendCMDreceiveATT(16,MultiWii.SET_RAW_RC,data)
            
print(board.attitude)
"""