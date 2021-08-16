# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 20:56:24 2020

@author: M
"""

import pigpio
import os
import time
import board
from adafruit_motor import stepper
from adafruit_motorkit import MotorKit


class PeripheryException(Exception):
    pass


class Controller:
    def __init__(self):
        try:
            os.system("sudo pigpiod")

            time.sleep(1)
            self.pi = pigpio.pi()
            if self.pi.connected:
                print("GPIO initialized")
            else:
                raise PeripheryException
        except PeripheryException:
            print("Failed to initialize GPIO. Probably already running")
            raise
        # Initialize HAT-controlled steppers and light
        self.kit = MotorKit(i2c=board.I2C())
        self.kit2 = MotorKit(i2c=board.I2C(), address=0x061)

        self.kit.stepper1.release() # not connected
        self.kit.stepper2.release() # X-axis stepper
        self.kit2.stepper1.release() # Z-axis stepper
        self.kit2.motor3.throttle = 0.0 # Lights

        # Initialize Y-stepper
        self.direction_pin = 18
        self.pi.set_mode(self.direction_pin, pigpio.OUTPUT)
        self.step_pin = 17
        self.pi.set_mode(self.step_pin, pigpio.OUTPUT)
        self.pi.write(self.direction_pin, 0)
        self.pi.write(self.step_pin, 0)
        self.sleep_pin = 27
        self.pi.set_mode(self.sleep_pin, pigpio.OUTPUT)
        self.pi.write(self.sleep_pin, 0)

        self.speed = 4

    def readCommand(self, cmd):
        if cmd == "up":
            self.moveY(down=False)
        elif cmd == "down":
            self.moveY(down=True)
        elif cmd == "left":
            self.moveX(left=True)
        elif cmd == "right":
            self.moveX(left=False)
        elif cmd == "plus":
            self.moveZ(down=False)
        elif cmd == "minus":
            self.moveZ(down=True)
        elif cmd == "brighten":
            self.increaseLight()
        elif cmd == "dim":
            self.decreaseLight()
        elif cmd == "fasten":
            self.increaseSpeed()
        elif cmd == "slow":
            self.decreaseLight()

    def moveX(self, left: bool):
        if left:
            for i in range(16*self.speed):
                self.kit.stepper2.onestep(direction=stepper.BACKWARD,
                                          style=stepper.MICROSTEP)
        else:
            for i in range(16*self.speed):
                self.kit.stepper2.onestep(direction=stepper.FORWARD,
                                          style=stepper.MICROSTEP)
        self.kit.stepper2.release()

    def moveY(self, down: bool):
        if down:
            for i in range(self.speed*16):
                self.kit2.stepper1.onestep(direction=stepper.BACKWARD,
                                           style=stepper.MICROSTEP)
        else:
            for i in range(self.speed*16):
                self.kit2.stepper1.onestep(direction=stepper.FORWARD,
                                           style=stepper.MICROSTEP)
        self.kit2.stepper1.release()

    def moveZ(self, down: bool):
        self.pi.write(self.sleep_pin, 1)
        for step in range(self.speed*32):
            self.pi.write(self.step_pin, 1)
            time.sleep(0.001)
            self.pi.write(self.step_pin, 0)
            time.sleep(0.001)
        self.pi.write(self.sleep_pin, 0)

    def increaseLight(self):
        self.kit2.motor3.throttle = min(1.0, self.kit2.motor3.throttle + 0.25)

    def decreaseLight(self):
        self.kit2.motor3.throttle = max(0.0, self.kit2.motor3.throttle - 0.25)

    def increaseSpeed(self):
        self.speed = min(15, self.speed+1)

    def decreaseSpeed(self):
        self.speed = max(1, self.speed-1)
