from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

me = Motor(Port.A, Direction.COUNTERCLOCKWISE)
md = Motor(Port.B)


drive_base = DriveBase(me, md, 54, 82) #a definir.
drive_base.use_gyro(True)


def andar(dist):
    drive_base.settings(350, 350, 220, 220)
    drive_base.straight(dist*10)

def turn(radius, angle):
    drive_base.settings(200, 200, 200, 200)
    drive_base.curve(radius, angle)

def rotate(graus):
    drive_base.use_gyro(false)
    drive_base.settings(220, 220, 200, 220)
    drive_base.turn(graus)
    drive_base.use_gyro(true)


def andar_pid(dist_cm, velocidade=300):
    KP = 2.5
    KI = 0.01
    KD = 1.5

    dist_mm      = dist_cm * 10
    heading_alvo = drive_base.heading()

    erro_anterior = 0
    integral      = 0
    timer         = StopWatch()
    dt_anterior   = 0

    drive_base.reset()

    while drive_base.distance() < dist_mm:
        agora = timer.time()
        dt    = max((agora - dt_anterior) / 1000, 0.001)
        dt_anterior = agora

        erro      = heading_alvo - drive_base.heading()
        integral  += erro * dt
        derivada   = (erro - erro_anterior) / dt
        correcao   = (KP * erro) + (KI * integral) + (KD * derivada)
        erro_anterior = erro

        # aplica correção diretamente nos motores
        me.dc(min(100, max(-100, (velocidade + correcao) / 10)))
        md.dc(min(100, max(-100, (velocidade - correcao) / 10)))

        wait(10)

    me.brake()
    md.brake()
