from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from bip import bipar
from Consts import openn,close,closeClawLeft,closeClawRight
from Drive_Train import andar,rotate,andarSlow,turn,rotate_closed,clawE,andarSlow2


hub = PrimeHub()

#Missão 1  rota I / Coletar formas geométricas
def rotaI_missao1():
    
    openn()
    wait(100)
    close()
    andar(18)

    rotate_closed(-85,300)
    andar(7)
    rotate_closed(-130,300)
    
#Missão 1 rota II / Depositar Formas geométricas
def rotaII_missao1():

    andar(24)
    rotate_closed(-92,300)
    andar(18)
    openn()

    andar(-25)
    wait(100)
    closeClawRight(-100)
    rotate(-90)
    andar(15)

#Missão 2  rota III / Empurrar carrinho    
def rotaIII_missao2():

    andarSlow(84)
    andar(-85)


#Missão 3 rota IV / pegar blocos de construção e depositar
def rotaIV_missao3():

    crema = Motor(Port.E)
    def cremaLow():
        crema.run_angle(2000,370)

    def cremaMid():
        crema.run_angle(2000,160)

    def cremaHigh():
        crema.run_angle(2000,-400)

    andarSlow(130)
    rotate(50)
    andar(-20)
    rotate(43)

    cremaLow()
    andarSlow2(10)
    cremaHigh()

    rotate(185)
    andar(12)
    rotate(-80)

    andar(16)
    rotate(90)
    andarSlow(2)
    cremaLow()
    wait(100)
    cremaHigh()
    andar(-8)

    andar(-5)
    rotate(-70)
    andar(50)
    rotate(-80)
    andar(60)

    
    

#missão 4 e 5 rota V / derrubar rampa subir ela
def rotaV_missao4():

    andarSlow(150)
    rotate_closed(-10,200)
    andarSlow(16)
    closeClawLeft(250)
    wait(800)
    closeClawLeft(-250)
    wait(100)
    closeClawLeft(250)

    andar(-10)
    wait(100)
    rotate_closed(-70,150)
    wait(100)
    andar(-20)
    rotate(90)
    andar(40)
    rotate(-105)
    andar(40)

