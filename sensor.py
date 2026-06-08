from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from Drive_Train import drive_base

hub = PrimeHub()

sensor = ForceSensor(Port.A)

while true:
    forca = sensor.force()

    if forca >= 5:
        print("Objeto detectado")
        #adicionar a rota de desvio
        break

    wait(10)
