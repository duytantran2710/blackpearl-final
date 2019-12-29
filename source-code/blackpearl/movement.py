#!/usr/bin/env python
#
# filename: movement.py
# author:   DTT,Lan Le , Phuc
# date:     19-Nov-2015
# purpose:  Controll the main motors
# hardware: MOTOR_B & MOTOR_C
#
from BrickPi import *
import time

class Movement:
    power = 255
    def __init__(self):
        BrickPiSetup()
        # initialize front motors
        BrickPi.MotorEnable[PORT_B] = 1    # enable motor B
        BrickPi.MotorEnable[PORT_C] = 1    # enable motor C
        BrickPiSetupSensors()
        
    def moveForward(self):
        BrickPi.MotorSpeed[PORT_B] = self.power
        BrickPi.MotorSpeed[PORT_C] = self.power
        BrickPiUpdateValues()
    
    def moveBackward(self):
        BrickPi.MotorSpeed[PORT_B] = -self.power
        BrickPi.MotorSpeed[PORT_C] = -self.power
        BrickPiUpdateValues()    
    
    def turnLeft(self):
        BrickPi.MotorSpeed[PORT_B] = self.power
        BrickPi.MotorSpeed[PORT_C] = -self.power
        BrickPiUpdateValues()
        
    def turnRight(self):
        BrickPi.MotorSpeed[PORT_B] = -self.power
        BrickPi.MotorSpeed[PORT_C] = self.power
        BrickPiUpdateValues()
    
    def handleAction(self, action):
        if action == 'forward':
            self.moveForward()
        if action == 'backward':
            self.moveBackward()  
        if action == 'left':
            self.turnLeft()
        if action == 'right':
            self.turnRight()
