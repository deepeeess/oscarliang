#!/usr/bin/env python
import smbus
import time
import signal
import sys
import redis
import traceback

bus = smbus.SMBus(1)

address = 0x04

while True: #event loop
  try: 
    #this should work without any errors
    #try turning this on in /boot/config.txt to eliminate errors
    #dtparam=i2c_arm=on,i2c_arm_baudrate=38400
    message = bus.read_i2c_block_data(address,0)
    print("message " + str(message))
  except KeyboardInterrupt:
    print "Killed."
    sys.exit()
  except:
    print("could not read from device");
    time.sleep(1)
