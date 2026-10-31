from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait, StopWatch
from Drive_Train import md,me
from umath import pi
from pybricks.parameters import Axis

hub = PrimeHub(top_side=Axis.Z, front_side=Axis.Y)


WHEEL_DIAMETER = 54  

class PID:
    def __init__(self, kp, ki, kd, integral_limit=None):
        self.kp, self.ki, self.kd = kp, ki, kd
        self.integral_limit = integral_limit
        self.integral = 0
        self.last_error = 0

    def reset(self):
        self.integral = 0
        self.last_error = 0

    def update(self, error, dt):
        self.integral += error * dt
        if self.integral_limit is not None:
            self.integral = max(-self.integral_limit, min(self.integral_limit, self.integral))
        derivative = (error - self.last_error) / dt if dt > 0 else 0
        self.last_error = error
        return self.kp * error + self.ki * self.integral + self.kd * derivative




def move_straight(hub, left_motor, right_motor, distance_mm, speed, target_heading):
    heading_pid = PID(kp=8, ki=0, kd=0, integral_limit=0)
    # SEM reset_heading aqui — usamos a referência global da rota

    me.reset_angle(0)
    md.reset_angle(0)
    target_angle = (distance_mm / (pi * WHEEL_DIAMETER)) * 360

    timer = StopWatch()
    last_time = timer.time()

    while (abs(me.angle()) + abs(md.angle())) / 2 < target_angle:
        now = timer.time()
        dt = (now - last_time) / 1000
        last_time = now

        error = target_heading - hub.imu.heading()

        if abs(error) < 1.0:
            error = 0

        correction = heading_pid.update(error, dt)

        me.run(speed + correction)
        md.run(speed - correction)
        wait(10)

    me.brake()
    md.brake()


def turn_to_heading(hub, left_motor, right_motor, target_heading, speed=150, tolerance=2):
    while abs(target_heading - hub.imu.heading()) > tolerance:
        error = target_heading - hub.imu.heading()
        direcao = 1 if error > 0 else -1
        me.run(direcao * speed)
        md.run(-direcao * speed)
        wait(10)
    me.brake()
    md.brake()

def run_route(hub, left_motor, right_motor):
    hub.imu.reset_heading(0)  # Única vez, no começo da rota inteira

    route = [
        ("move", 100),   # anda 10cm mirando heading 0°
        ("turn", 90),    # gira até heading absoluto 90°
        ("move", 200),   # anda 20cm mirando heading 90° (não "0 relativo")
    ]

    current_heading = 0
    for step_type, value in route:
        if step_type == "move":
            move_straight(hub, me, md, value, 150, current_heading)
        elif step_type == "turn":
            current_heading = value
            turn_to_heading(hub, me, md, current_heading)

#move_straight(hub,me,md,800,500,0)

def andar(distancia,heading_alvo=0):
    move_straight(hub,me,md,distancia,200,target_heading=heading_alvo)

andar(600,90)
