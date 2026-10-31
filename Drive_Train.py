from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Axis

hub = PrimeHub(top_side=Axis.Z, front_side=Axis.Y)
me = Motor(Port.A, Direction.COUNTERCLOCKWISE)
md = Motor(Port.B)
clawE = Motor(Port.D)
clawD = Motor(Port.C)
drive_base = DriveBase(me, md,69, 140)

drive_base.use_gyro(True)

#Controle PID
drive_base.heading_control.pid(81242,0,7310,4,8)
drive_base.distance_control.pid(81242,0,7310,5,10)


def andar(dist):
    drive_base.heading_control.pid(81242,0,7310,4,8)
    drive_base.distance_control.pid(81242,0,7310,5,10)
    drive_base.use_gyro(True)
    drive_base.settings(400, 400, 400, 400)
    drive_base.straight(dist*10)
    drive_base.reset()

def andarSpeed(dist):
    
    drive_base.use_gyro(True)
    drive_base.settings(600, 600, 400, 400)
    drive_base.straight(dist*10)
    drive_base.reset()

#Andar mais Lento
def andarSlow(dist):
    
    drive_base.use_gyro(True)
    drive_base.settings(350,280, 400, 400)
    drive_base.straight(dist*10)
    drive_base.reset()

def andarSlow2(dist):
    
    drive_base.use_gyro(True)
    drive_base.settings(60,60, 400, 400)
    drive_base.straight(dist*10)
    drive_base.reset()


def turn(radius, angle):
    
    drive_base.use_gyro(True)
    drive_base.settings(200, 200, 200, 200)
    drive_base.curve(radius, angle)

#Rotação padrão
def rotate(graus):

    drive_base.reset()

    #Controle PID
    drive_base.heading_control.pid(81242,0,7310,4,8)
    drive_base.distance_control.pid(81242,0,7310,5,10)

    print("heading: " , hub.imu.heading())
    drive_base.use_gyro(True)
    drive_base.settings(400, 400, 100, 150)
    drive_base.turn(graus)

#Rotação mais Controlada
def rotate_closed(graus,speed):

    #Controle PID
    drive_base.heading_control.pid(81242,0,7310,4,8)
    drive_base.distance_control.pid(81242,0,7310,5,10)
    
    while abs(hub.imu.heading() - graus)>2:
        print("heading " , hub.imu.heading())
        erro = graus - hub.imu.heading()
        direcao = 1 if erro > 0 else - 1
        me.run(direcao * speed)
        md.run(-direcao * speed)
        wait(10)

    me.brake()
    md.brake()
    
