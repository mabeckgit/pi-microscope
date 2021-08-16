# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
from adafruit_motor import stepper
from adafruit_motorkit import MotorKit
import time

kit = MotorKit(i2c=board.I2C())
kit2 = MotorKit(i2c=board.I2C(), address=0x061)

kit.stepper1.release()
kit.stepper2.release()
"""
kit2.motor3.throttle = 0.25
time.sleep(1.0)
kit2.motor3.throttle = 0.5
time.sleep(1.0)
kit2.motor3.throttle = 0.75
time.sleep(1.0)

time.sleep(1.0)
"""
#kit2.motor3.throttle = 1.0

kit.stepper2.release()
timing3 = 0*16
timing2 = 4*16
left = 0
down = 0
print("Microsteps")

if left == 1:
    for i in range(timing2):
        kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.MICROSTEP)
    time.sleep(0.2)
else: 
    for i in range(timing2):
        kit.stepper2.onestep(direction=stepper.FORWARD, style=stepper.MICROSTEP)
    time.sleep(0.2)
print("Interleaved coil steps")
if down == 1:
    for i in range(timing3):
        kit2.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.MICROSTEP)
else:
    for i in range(timing3):
        kit2.stepper1.onestep(direction=stepper.FORWARD, style=stepper.MICROSTEP)
kit.stepper2.release()
kit2.stepper1.release()