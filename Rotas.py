from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from Drive_Train import andar, rotate, turn,md,claw
from bip import bipar

hub = PrimeHub()

def close():
    claw.run_angle(1000,300)

def openn():
    claw.run_target(1000,60)

def rotaI():
    bipar(500,100)
    andar(18)
    rotate(90)
    wait(500)
    andar(8)
    close()
    wait(500)
    andar(-15)
    wait(500)
    rotate(-90)
    
def rotaII():
    bipar(500,100)
    andar(14)
    rotate(90)
    andar(4)
    openn()
    


