#!/usr/bin/env python
#
# filename: camera.py
# author:   DTT
# date:     18-Nov-2015
# purpose:  Controlling the camera of the robot
# hardware: MOTOR_C
#
from BrickPi_fixed import *
from datetime import datetime

class Camera:
    def __init__(self):
        self.rpi = BrickPi()
        self.motor = self.rpi.motors[PORT_C]
        
    def getCurrentPosition(self):
        return [self.motor.get_position_in_degrees(), self.motor.position]
    
    def rotateLeft(self):
        self.motor.rotate(100, -10)
        self.rpi.update_values()
        self.motor.update_position()

    def rotateRight(self):
        currentDeg = self.motor.get_position_in_degrees()
        self.motor.rotate(100, 10)
        self.rpi.update_values()
        self.motor.update_position()
    
    def handleAction(self, action):
        if action == 'left':
            self.rotateLeft()
        else:
            self.rotateRight()
        return "[%s]: Rotate the camera to the %s at position %s." % (self.getCurrentTime(), action, str(self.getCurrentPosition()))
    
    def getCurrentTime(self):
        return datetime.now().strftime('%H:%m:%S')
