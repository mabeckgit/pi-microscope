import pigpio
import os
import time


class PeripheryException(Exception):
    pass


class BigStepper:
    def __init__(self):
        try:
            cmd_return = os.system("sudo pigpiod")

            time.sleep(1)
            self.pi = pigpio.pi()
            if self.pi.connected:
                print("GPIO initialized")
            else:
                raise PeripheryException
        except PeripheryException:
            print("Failed to initialize GPIO")
            raise
        self.directionpin = 18
        self.pi.set_mode(self.directionpin, pigpio.OUTPUT)
        self.direction = True
        self.steppin = 17
        self.pi.set_mode(self.steppin, pigpio.OUTPUT)
        self.pi.write(self.directionpin, 0)
        self.pi.write(self.steppin, 0)
        self.sleeppin = 27
        self.pi.set_mode(self.sleeppin, pigpio.OUTPUT)
        self.pi.write(self.sleeppin, 0)
        
    def toggle_direction(self):
        if self.direction:
            self.pi.write(self.directionpin, 0)
            self.direction = False
        else:
            self.pi.write(self.directionpin, 1)
            self.direction = True
            
    def perform_steps(self, number_steps, delay):
        self.pi.write(self.sleeppin, 1)
        #time.sleep(1)
        for step in range(number_steps*32):
            self.pi.write(self.steppin, 1)
            time.sleep(delay)
            self.pi.write(self.steppin, 0)
            time.sleep(delay)
        self.pi.write(self.sleeppin, 0)
            
