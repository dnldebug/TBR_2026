from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Axis

hub = PrimeHub(top_side=Axis.X, front_side=Axis.Z)
me = Motor(Port.A, Direction.COUNTERCLOCKWISE)
md = Motor(Port.B)
claw = Motor(Port.F)
drive_base = DriveBase(me, md, 54, 90)

drive_base.use_gyro(True)

def andar(dist):
    hub = PrimeHub(top_side=Axis.X, front_side=Axis.Z)
    drive_base.use_gyro(True)
    drive_base.settings(350, 400, 220, 220)
    drive_base.straight(dist*10)
    drive_base.reset()
    

def turn(radius, angle):
    drive_base.settings(200, 200, 200, 200)
    drive_base.curve(radius, angle)

def rotate(graus):
    hub = PrimeHub(top_side=Axis.X, front_side=Axis.Z)
    drive_base.use_gyro(True)
    drive_base.settings(350, 400, 300, 300)
    drive_base.turn(graus)
    drive_base.reset()
    


