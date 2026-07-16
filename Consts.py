from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from Drive_Train import claw

hub = PrimeHub()

def close():
    claw.run_angle(1000,300)

def openn():
    claw.run_target(1000,60)

def high():
    claw.run_angle(1000,800)

    
