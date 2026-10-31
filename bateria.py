from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from Drive_Train import andar, rotate, turn



hub = PrimeHub()


while True:
    battery_voltage = hub.battery.voltage()
    print("Nivel da bateria", battery_voltage / 1000, "V")
    wait(1000) 

